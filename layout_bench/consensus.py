"""Score every model against a consensus pseudo-ground-truth built from all of them.

    python -m layout_bench.consensus                 # markdown table over results/
    python -m layout_bench.consensus --format json   # same numbers, machine readable

There is no human-labeled ground truth in this benchmark, so the ranking uses a
consensus proxy, exactly as described in docs/analysis.md:

  1. per document, pool the boxes of every model and cluster them at IoU > 0.6
  2. a cluster backed by >= 6 distinct models is accepted as a consensus region
  3. each model is then scored for precision / recall against that region set

Precision and recall are averaged per document and then across documents, so a dense
page does not outweigh a sparse one. F1 is the harmonic mean of the two averages. A
document the model ran on but detected nothing in counts as a zero, which is why the
`Docs` column (documents with any output) is reported alongside.

Byte-identical PDFs are scored once (`Testdataset.pdf` is a copy of `kjgpnnkvvjcm.pdf`),
otherwise the duplicated page would get double weight in every average.

Stdlib only — runs in the `base` venv, or any Python 3.9+.
"""
import argparse
import glob
import hashlib
import json
import os
import sys
from collections import defaultdict

from . import paths

IOU_CLUSTER = 0.6      # boxes above this are the same region
IOU_MATCH = 0.6        # a detection matches a consensus region above this
MIN_MODELS = 6         # cluster support needed to become a consensus region
IOU_DUP = 0.5          # a model's own box duplicating another of its own
CONTAIN_NEST = 0.9     # fraction of a box's area swallowed by a larger own box
MIN_BOXES_FOR_GEOM = 20  # below this, dup% / nest% are noise — reported as "—"


def normalize_label(label):
    """`Section-header`, `section_header` and `Key-Value Region` are one class, not three.

    The docling models take their class names from the checkpoint config, and the
    casing of those names has changed between transformers releases — so the same
    model spells a class differently depending on when its results were generated.
    Vocabulary size is meant to measure semantics, so fold the spellings together.
    """
    return label.strip().lower().replace("-", "_").replace(" ", "_")


def _area(b):
    return max(0.0, b[2] - b[0]) * max(0.0, b[3] - b[1])


def _inter(a, b):
    w = min(a[2], b[2]) - max(a[0], b[0])
    h = min(a[3], b[3]) - max(a[1], b[1])
    return w * h if w > 0 and h > 0 else 0.0


def _iou(a, b):
    i = _inter(a, b)
    u = _area(a) + _area(b) - i
    return i / u if u > 0 else 0.0


def _contained(inner, outer):
    """Fraction of `inner` that lies inside `outer`."""
    a = _area(inner)
    return _inter(inner, outer) / a if a > 0 else 0.0


def load_corpus(results_dir, pdf_dir):
    """{doc: {model: [detection, ...]}}, byte-identical documents collapsed to one."""
    corpus = {}
    for summary in sorted(glob.glob(os.path.join(results_dir, "*", "SUMMARY.md"))):
        doc = os.path.basename(os.path.dirname(summary))
        models = {}
        for dj in sorted(glob.glob(os.path.join(results_dir, doc, "*", "detections.json"))):
            try:
                with open(dj, encoding="utf-8") as f:
                    d = json.load(f)
            except (OSError, ValueError) as exc:
                print(f"  !! unreadable {dj}: {exc}", file=sys.stderr)
                continue
            models[d["model"]] = d.get("detections", [])
        if models:
            corpus[doc] = models
    return _drop_duplicate_docs(corpus, pdf_dir)


def _drop_duplicate_docs(corpus, pdf_dir):
    """Keep one result folder per distinct PDF, preferring the first name alphabetically."""
    by_digest = defaultdict(list)
    for doc in corpus:
        pdf = os.path.join(pdf_dir, doc + ".pdf")
        if not os.path.exists(pdf):
            by_digest[f"__nopdf__{doc}"].append(doc)
            continue
        with open(pdf, "rb") as f:
            by_digest[hashlib.sha256(f.read()).hexdigest()].append(doc)

    dropped = []
    for docs in by_digest.values():
        for doc in sorted(docs, key=str.lower)[1:]:
            dropped.append(doc)
            corpus.pop(doc, None)
    if dropped:
        print(f"  -- duplicate document(s) scored once: {', '.join(sorted(dropped))}",
              file=sys.stderr)
    return corpus


def consensus_regions(models, iou=IOU_CLUSTER, min_models=MIN_MODELS):
    """Cluster every model's boxes together; keep the clusters enough models agree on.

    Greedy single-representative clustering seeded by descending confidence, so the
    most certain box anchors each region rather than whichever model was read first.
    Boxes without a score sort last; ties break on coordinates to stay deterministic.
    """
    boxes = sorted(
        ((m, det["box"], det.get("score")) for m, dets in models.items() for det in dets),
        key=lambda mbs: (-(mbs[2] if mbs[2] is not None else 0.0), mbs[1], mbs[0]),
    )
    clusters = []  # [representative box, {model, ...}]
    for model, box, _score in boxes:
        for rep, backers in clusters:
            if _iou(rep, box) > iou:
                backers.add(model)
                break
        else:
            clusters.append([box, {model}])
    return [rep for rep, backers in clusters if len(backers) >= min_models]


def score_document(models, regions, iou=IOU_MATCH):
    """Per-document precision and recall against the consensus set.

    Matching is many-to-one on purpose: a model is not punished twice for splitting one
    consensus region into two plausible boxes, and a region is covered if any box finds
    it. Over-segmentation shows up in the dup% / nest% columns instead.
    """
    out = {}
    for model, dets in models.items():
        hits = sum(1 for d in dets
                   if any(_iou(d["box"], g) > iou for g in regions))
        covered = sum(1 for g in regions
                      if any(_iou(d["box"], g) > iou for d in dets))
        out[model] = {
            "precision": hits / len(dets) if dets else 0.0,
            "recall": covered / len(regions) if regions else None,
        }
    return out


def geometry(dets):
    """(duplicate boxes, nested boxes) among one model's own output on one page."""
    boxes = [d["box"] for d in dets]
    dup = nest = 0
    for i, a in enumerate(boxes):
        if any(_iou(a, b) > IOU_DUP for j, b in enumerate(boxes) if i != j):
            dup += 1
        if any(_area(b) > _area(a) and _contained(a, b) > CONTAIN_NEST
               for j, b in enumerate(boxes) if i != j):
            nest += 1
    return dup, nest


def aggregate(corpus):
    """Per-model totals over the corpus, sorted by consensus F1."""
    stats = defaultdict(lambda: {
        "docs": 0, "docs_with_output": 0, "n": 0, "precisions": [], "recalls": [],
        "dup": 0, "nest": 0, "scores": [], "vocab": set(), "classes_per_doc": [],
    })
    all_models = sorted({m for models in corpus.values() for m in models})

    for models in corpus.values():
        regions = consensus_regions(models)
        scored = score_document(models, regions)
        for model in all_models:
            s = stats[model]
            s["docs"] += 1
            dets = models.get(model)
            if dets is None:
                continue          # model never ran on this document
            if dets:
                s["docs_with_output"] += 1
            s["n"] += len(dets)
            s["precisions"].append(scored[model]["precision"])
            if scored[model]["recall"] is not None:
                s["recalls"].append(scored[model]["recall"])
            dup, nest = geometry(dets)
            s["dup"] += dup
            s["nest"] += nest
            s["scores"] += [d["score"] for d in dets if d.get("score") is not None]
            labels = {normalize_label(d["label"]) for d in dets}
            s["vocab"] |= labels
            s["classes_per_doc"].append(len(labels))

    def mean(xs):
        return sum(xs) / len(xs) if xs else 0.0

    rows = []
    for model in all_models:
        s = stats[model]
        prec, rec = mean(s["precisions"]), mean(s["recalls"])
        f1 = 2 * prec * rec / (prec + rec) if prec + rec else 0.0
        geom_ok = s["n"] >= MIN_BOXES_FOR_GEOM
        rows.append({
            "model": model,
            "docs_with_output": s["docs_with_output"],
            "docs": s["docs"],
            "mean_n": s["n"] / s["docs"] if s["docs"] else 0.0,
            "f1": f1, "precision": prec, "recall": rec,
            "dup_pct": (100.0 * s["dup"] / s["n"]) if geom_ok else None,
            "nest_pct": (100.0 * s["nest"] / s["n"]) if geom_ok else None,
            "conf": sum(s["scores"]) / len(s["scores"]) if s["scores"] else None,
            "vocab": len(s["vocab"]),
            "classes": sorted(s["vocab"]),
            "cls_per_doc": (sum(s["classes_per_doc"]) / len(s["classes_per_doc"])
                            if s["classes_per_doc"] else 0.0),
        })
    rows.sort(key=lambda r: -r["f1"])
    return rows


def to_markdown(rows, ndocs):
    def pct(v):
        return "—" if v is None else f"{v:.1f}"

    out = ["| # | Model | Docs | mean N | F1 | Prec | Rec | dup% | nest% | conf | vocab | cls/doc |",
           "|--:|---|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|"]
    for i, r in enumerate(rows, 1):
        conf = "—" if r["conf"] is None else f"{r['conf']:.2f}"
        out.append(
            f"| {i} | `{r['model']}` | {r['docs_with_output']}/{ndocs} | {r['mean_n']:.1f} | "
            f"{r['f1']:.3f} | {r['precision']:.3f} | {r['recall']:.3f} | "
            f"{pct(r['dup_pct'])} | {pct(r['nest_pct'])} | {conf} | "
            f"{r['vocab']} | {r['cls_per_doc']:.1f} |")
    return "\n".join(out)


def main(argv=None):
    ap = argparse.ArgumentParser(description=__doc__,
                                 formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("results", nargs="?", default=str(paths.RESULTS),
                    help="results root to score (default: results/)")
    ap.add_argument("--pdf-dir", default=str(paths.PDF_DIR),
                    help="corpus directory, used to spot byte-identical documents")
    ap.add_argument("--format", choices=("md", "json"), default="md")
    args = ap.parse_args(argv)

    # the table uses em dashes; a cp1252 console would mangle them
    for stream in (sys.stdout, sys.stderr):
        if hasattr(stream, "reconfigure"):
            stream.reconfigure(encoding="utf-8")

    corpus = load_corpus(args.results, args.pdf_dir)
    if not corpus:
        print(f"no scored documents under {args.results}", file=sys.stderr)
        return 1
    rows = aggregate(corpus)

    if args.format == "json":
        json.dump({"documents": sorted(corpus), "models": rows},
                  sys.stdout, indent=2)
        sys.stdout.write("\n")
    else:
        print(f"Consensus ranking over {len(corpus)} documents "
              f"(IoU > {IOU_CLUSTER}, >= {MIN_MODELS} of {len(rows)} models agreeing)\n")
        print(to_markdown(rows, len(corpus)))
    return 0


if __name__ == "__main__":
    sys.exit(main())
