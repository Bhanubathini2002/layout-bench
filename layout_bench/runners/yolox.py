"""Unstructured's YOLOX layout model.

    python -m layout_bench.runners.yolox

Needs the `unstructured` venv. Downloads yolox_l.onnx on first use.
"""
import sys

import numpy as np
from unstructured_inference.models.base import get_model

from .. import overlay


def _collect(res):
    dets = []

    def add(x0, y0, x1, y1, label, score):
        dets.append({"label": str(label),
                     "score": (float(score) if score is not None else None),
                     "box": [round(float(x0), 1), round(float(y0), 1),
                             round(float(x1), 1), round(float(y1), 1)]})

    # Newer unstructured-inference: LayoutElements with parallel numpy arrays
    if hasattr(res, "element_coords"):
        coords = np.asarray(res.element_coords)
        probs = getattr(res, "element_probs", None)
        class_ids = getattr(res, "element_class_ids", None)
        id2name = getattr(res, "element_class_id_map", None) or {}
        for i, (x0, y0, x1, y1) in enumerate(coords):
            cid = int(class_ids[i]) if class_ids is not None else -1
            add(x0, y0, x1, y1, id2name.get(cid, str(cid)),
                float(probs[i]) if probs is not None else None)
    else:
        # Older form: iterable of LayoutElement objects with .bbox / .type / .prob
        for el in res:
            b = el.bbox
            add(b.x1, b.y1, b.x2, b.y2, getattr(el, "type", "?"), getattr(el, "prob", None))
    return dets


def main(argv=None):
    img = overlay.load_page()
    model = get_model("yolox")
    res = model(img)
    print("return type:", type(res))

    dets = _collect(res)
    dets.sort(key=lambda d: -(d["score"] or 0))
    overlay.save_outputs("unstructured-yolox", dets, meta={"model": "yolox (yolox_l)"})
    return 0


if __name__ == "__main__":
    sys.exit(main())
