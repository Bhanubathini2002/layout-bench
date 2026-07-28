"""HuggingFace object-detection layout models (Docling, Aryn, Table Transformer).

    python -m layout_bench.runners.transformers_det [name-filter]

Needs the `torch` venv. Uses CUDA when available and falls back to CPU per model.
One model failing does not stop the rest.
"""
import sys
import traceback

import torch
from transformers import AutoImageProcessor, AutoModelForObjectDetection

from .. import overlay

# (output folder name, HF repo, score threshold)
MODELS = [
    ("aryn-deformable-detr-DocLayNet", "Aryn/deformable-detr-DocLayNet", 0.5),
    ("docling-heron",                  "ds4sd/docling-layout-heron",     0.5),
    ("docling-heron-101",              "ds4sd/docling-layout-heron-101", 0.5),
    ("docling-egret-medium",           "docling-project/docling-layout-egret-medium", 0.5),
    ("docling-egret-large",            "docling-project/docling-layout-egret-large",  0.5),
    ("docling-egret-xlarge",           "docling-project/docling-layout-egret-xlarge", 0.5),
    ("table-transformer-detection",    "microsoft/table-transformer-detection",       0.6),
]

DEVICE = "cuda" if torch.cuda.is_available() else "cpu"


def run_one(name, repo, thr):
    print(f"\n=== {name}  ({repo}) ===")
    proc = AutoImageProcessor.from_pretrained(repo)
    model = AutoModelForObjectDetection.from_pretrained(repo).eval()
    img = overlay.load_page()
    inputs = proc(images=img, return_tensors="pt")

    dev = DEVICE
    try:
        model.to(dev)
        inputs = {k: v.to(dev) for k, v in inputs.items()}
        with torch.no_grad():
            outputs = model(**inputs)
    except RuntimeError as e:
        print(f"  {dev} forward failed ({e}); retrying on CPU")
        dev = "cpu"
        model.to("cpu")
        inputs = {k: v.to("cpu") for k, v in inputs.items()}
        with torch.no_grad():
            outputs = model(**inputs)

    W, H = img.size
    res = proc.post_process_object_detection(outputs, target_sizes=[(H, W)], threshold=thr)[0]
    id2label = model.config.id2label
    dets = []
    for score, label, box in zip(res["scores"], res["labels"], res["boxes"]):
        x0, y0, x1, y1 = [float(v) for v in box.tolist()]
        dets.append({
            "label": id2label.get(int(label), str(int(label))),
            "score": float(score),
            "box": [round(x0, 1), round(y0, 1), round(x1, 1), round(y1, 1)],
        })
    dets.sort(key=lambda d: -d["score"])
    overlay.save_outputs(name, dets, meta={"repo": repo, "threshold": thr, "device": dev,
                                           "num_classes": len(id2label)})


def main(argv=None):
    argv = sys.argv[1:] if argv is None else argv
    only = argv[0] if argv else None
    print(f"device: {DEVICE}")

    failed = 0
    for name, repo, thr in MODELS:
        if only and only not in name:
            continue
        try:
            run_one(name, repo, thr)
        except Exception:
            failed += 1
            print(f"!! FAILED {name}")
            traceback.print_exc()
    return 0 if failed == 0 else 1


if __name__ == "__main__":
    sys.exit(main())
