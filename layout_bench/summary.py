"""Scan one result folder's */detections.json -> SUMMARY.md + index.html gallery.

    python -m layout_bench.summary [result-dir]
"""
import argparse
import glob
import html
import json
import os
import sys

from . import paths


def _page_dims():
    try:
        from PIL import Image
        w, h = Image.open(paths.PAGE).size
        return f"{w}x{h}"
    except Exception:
        return "?"


def _family(m):
    """Group models so the gallery reads by architecture family, not alphabetically."""
    if m.startswith("rapidlayout-pp_doc"):
        return "1. PP-DocLayout (modern, PaddleOCR)"
    if m.startswith("rapidlayout-doclayout"):
        return "2. DocLayout-YOLO"
    if m.startswith("docling") or m.startswith("aryn"):
        return "3. Docling (heron / egret)"
    if m.startswith("rapidlayout-yolov8") or m.startswith("unstructured"):
        return "4. YOLOv8 layout"
    if m.startswith("rapidlayout-pp_layout"):
        return "5. Classic Paddle (PubLayNet / CDLA / Table)"
    if m.startswith("table-transformer"):
        return "6. Table Transformer"
    return "9. Other"


def collect(outroot):
    rows = []
    for dj in sorted(glob.glob(os.path.join(outroot, "*", "detections.json"))):
        d = json.load(open(dj, encoding="utf-8"))
        rows.append({
            "model": d["model"],
            "n": d["num_detections"],
            "classes": d["class_counts"],
            "nclasses": len(d["class_counts"]),
            "meta": d.get("meta", {}),
            "img": f"{d['model']}/overlay.png",
        })
    rows.sort(key=lambda r: (_family(r["model"]), -r["n"]))
    return rows


def write_markdown(outroot, rows, doc, dims):
    md = [f"# Layout model benchmark — {doc}\n",
          f"Canonical input: one rendered page ({dims}). {len(rows)} models tested. "
          "Each folder holds `overlay.png` + `detections.json`.\n",
          "| Model | #Regions | #Classes | Top classes |",
          "|---|--:|--:|---|"]
    for r in rows:
        top = ", ".join(f"{k}:{v}" for k, v in
                        sorted(r["classes"].items(), key=lambda x: -x[1])[:5])
        md.append(f"| `{r['model']}` | {r['n']} | {r['nclasses']} | {top} |")
    with open(os.path.join(outroot, "SUMMARY.md"), "w", encoding="utf-8") as f:
        f.write("\n".join(md))


def write_gallery(outroot, rows, doc):
    h = ["<!doctype html><meta charset=utf-8><title>Layout model comparison</title>",
         "<style>body{font-family:system-ui,Arial;margin:24px;background:#0f1115;color:#e6e6e6}",
         "h1{font-size:22px}h2{margin:28px 0 8px;color:#8ec6ff;border-bottom:1px solid #333;padding-bottom:4px}",
         ".card{margin:16px 0;background:#181b20;border:1px solid #2a2f37;border-radius:10px;padding:14px}",
         ".meta{font-size:13px;color:#9aa4b2;margin:2px 0 8px}",
         ".tag{display:inline-block;background:#242a33;border-radius:5px;padding:2px 7px;margin:2px;font-size:12px}",
         "img{width:100%;border-radius:6px;border:1px solid #333;cursor:zoom-in}",
         "a{color:#8ec6ff}</style>",
         f"<h1>Layout model comparison — {html.escape(doc)} ({len(rows)} models)</h1>",
         "<p class=meta>Click any image to open full-res. "
         "Boxes are colored per class, with a legend at the top-left of each overlay.</p>"]
    cur = None
    for r in rows:
        fam = _family(r["model"])
        if fam != cur:
            cur = fam
            h.append(f"<h2>{html.escape(fam[3:])}</h2>")
        tags = "".join(f"<span class=tag>{html.escape(k)}: {v}</span>"
                       for k, v in sorted(r["classes"].items(), key=lambda x: -x[1]))
        mt = r["meta"].get("model_type") or r["meta"].get("repo") or ""
        el = r["meta"].get("elapse_s")
        els = f" · {el}s" if el else ""
        h.append(f"<div class=card><b>{html.escape(r['model'])}</b> "
                 f"<span class=meta>— {r['n']} regions, {r['nclasses']} classes{els} · "
                 f"{html.escape(str(mt))}</span>"
                 f"<div class=meta>{tags}</div>"
                 f"<a href='{r['img']}' target=_blank><img loading=lazy src='{r['img']}'></a></div>")
    with open(os.path.join(outroot, "index.html"), "w", encoding="utf-8") as f:
        f.write("\n".join(h))


def main(argv=None):
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("outroot", nargs="?", default=str(paths.OUTROOT),
                    help="result folder to summarise (default: $LB_OUTROOT)")
    ap.add_argument("--doc", default=paths.DOC, help="document label for the title")
    args = ap.parse_args(argv)

    rows = collect(args.outroot)
    if not rows:
        print(f"no detections.json found under {args.outroot}")
        return 1

    dims = _page_dims()
    write_markdown(args.outroot, rows, args.doc, dims)
    write_gallery(args.outroot, rows, args.doc)

    print(f"Wrote SUMMARY.md and index.html for {len(rows)} models -> {args.outroot}")
    for r in rows:
        print(f"  {r['model']:<40} {r['n']:>4} regions  {r['nclasses']} classes")
    return 0


if __name__ == "__main__":
    sys.exit(main())
