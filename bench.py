#!/usr/bin/env python3
"""layout-bench driver — render each PDF once, run every model on it, build a report.

    python bench.py --all                  # every PDF in data/pdfs/
    python bench.py data/pdfs/paper.pdf    # one PDF
    python bench.py --all --force          # redo documents that already have results
    python bench.py --all --stage rapidlayout --stage summary

The model stages each run in their own virtualenv because their dependency sets
conflict (rapid-layout pins onnxruntime, unstructured-inference pins an older torch).
A missing venv is skipped with a warning rather than being fatal, so you can set up
just one family and still get results.

Stdlib only — run it with any Python 3.9+.
"""
import argparse
import os
import subprocess
import sys
import time
from pathlib import Path

REPO = Path(__file__).resolve().parent
VENVS = REPO / ".venvs"
PDF_DIR = Path(os.environ.get("LB_PDF_DIR", REPO / "data" / "pdfs"))
RESULTS = Path(os.environ.get("LB_RESULTS", REPO / "results"))
PAGE = Path(os.environ.get("LB_PAGE", REPO / ".cache" / "page.png"))

# stage -> (venv name, module, human description)
STAGES = {
    "render":       ("base",         "layout_bench.render",                  "render page 1 -> page.png"),
    "rapidlayout":  ("onnx",         "layout_bench.runners.rapidlayout",     "RapidLayout (12 ONNX model types)"),
    "transformers": ("torch",        "layout_bench.runners.transformers_det", "Docling / Aryn / Table Transformer"),
    "yolox":        ("unstructured", "layout_bench.runners.yolox",           "Unstructured YOLOX"),
    "summary":      ("base",         "layout_bench.summary",                 "SUMMARY.md + index.html"),
}
DEFAULT_STAGES = list(STAGES)


def venv_python(name):
    """Resolve a venv's interpreter. LB_PY_<NAME> overrides; 'base' falls back to this one."""
    override = os.environ.get(f"LB_PY_{name.upper()}")
    if override:
        return Path(override)
    base = VENVS / name
    exe = base / ("Scripts/python.exe" if os.name == "nt" else "bin/python")
    if exe.exists():
        return exe
    if name == "base":
        return Path(sys.executable)
    return None


def run_stage(stage, env):
    venv, module, desc = STAGES[stage]
    py = venv_python(venv)
    if py is None:
        print(f"  -- SKIP {stage}: no '{venv}' venv "
              f"(create it with setup.ps1 / setup.sh, or set LB_PY_{venv.upper()})")
        return None
    print(f"  >> {stage}: {desc}")
    rc = subprocess.call([str(py), "-m", module], cwd=str(REPO), env=env)
    if rc != 0:
        print(f"  !! {stage} exited {rc}")
    return rc


def run_pdf(pdf, stages, force):
    outroot = RESULTS / pdf.stem
    marker = outroot / "SUMMARY.md"
    if marker.exists() and not force:
        print(f"SKIP {pdf.name} (already has results; --force to redo)")
        return True

    print(f"\n########## {pdf.name} -> {outroot} ##########")
    outroot.mkdir(parents=True, exist_ok=True)

    env = dict(os.environ)
    env.update({
        "LB_PDF": str(pdf),
        "LB_PAGE": str(PAGE),
        "LB_OUTROOT": str(outroot),
        "LB_DOC": pdf.name,
        "PYTHONPATH": str(REPO) + os.pathsep + env.get("PYTHONPATH", ""),
    })

    t0 = time.time()
    for stage in stages:
        run_stage(stage, env)
    ok = marker.exists()
    print(f"########## {'DONE' if ok else 'INCOMPLETE'} {pdf.name} "
          f"in {int(time.time() - t0)}s ##########")
    return ok


def main(argv=None):
    ap = argparse.ArgumentParser(
        description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("pdfs", nargs="*", type=Path, help="PDFs to benchmark")
    ap.add_argument("--all", action="store_true", help=f"benchmark every PDF in {PDF_DIR.name}/")
    ap.add_argument("--force", action="store_true", help="re-run documents that already have results")
    ap.add_argument("--stage", action="append", choices=list(STAGES), dest="stages",
                    help="run only these stages (repeatable)")
    args = ap.parse_args(argv)

    pdfs = list(args.pdfs)
    if args.all:
        pdfs += sorted(PDF_DIR.glob("*.pdf"))
    if not pdfs:
        ap.error(f"no PDFs given. Use --all to run everything in {PDF_DIR}")

    missing = [p for p in pdfs if not p.exists()]
    if missing:
        ap.error("not found: " + ", ".join(str(p) for p in missing))

    stages = args.stages or DEFAULT_STAGES
    print(f"layout-bench: {len(pdfs)} document(s), stages: {', '.join(stages)}")

    done = sum(run_pdf(p, stages, args.force) for p in pdfs)
    print(f"\n=== {done}/{len(pdfs)} document(s) completed -> {RESULTS} ===")
    return 0 if done == len(pdfs) else 1


if __name__ == "__main__":
    sys.exit(main())
