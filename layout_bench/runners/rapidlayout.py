"""RapidLayout ONNX family — 12 model types, one output folder each.

    python -m layout_bench.runners.rapidlayout [name-filter]

Needs the `onnx` venv. Weights download to the rapid_layout cache on first use.
"""
import sys
import traceback

import numpy as np
from rapid_layout import ModelType, RapidLayout, RapidLayoutInput

from .. import overlay

CONF_THRESH = 0.4

TYPES = [
    ModelType.PP_DOC_LAYOUTV2, ModelType.PP_DOC_LAYOUTV3,
    ModelType.PP_LAYOUT_CDLA, ModelType.PP_LAYOUT_PUBLAYNET, ModelType.PP_LAYOUT_TABLE,
    ModelType.DOCLAYOUT_DOCSTRUCTBENCH, ModelType.DOCLAYOUT_D4LA, ModelType.DOCLAYOUT_DOCSYNTH,
    ModelType.YOLOV8N_LAYOUT_PAPER, ModelType.YOLOV8N_LAYOUT_REPORT,
    ModelType.YOLOV8N_LAYOUT_GENERAL6, ModelType.YOLOV8N_LAYOUT_PUBLAYNET,
]


def run_one(mt, arr):
    name = "rapidlayout-" + mt.name.lower()
    print(f"\n=== {name} ===")
    engine = RapidLayout(RapidLayoutInput(model_type=mt, conf_thresh=CONF_THRESH))
    out = engine(arr)
    dets = []
    if out.boxes is not None:
        for box, cls, sc in zip(out.boxes, out.class_names, out.scores):
            x0, y0, x1, y1 = [float(v) for v in box]
            dets.append({"label": str(cls), "score": float(sc),
                         "box": [round(x0, 1), round(y0, 1), round(x1, 1), round(y1, 1)]})
    dets.sort(key=lambda d: -d["score"])
    overlay.save_outputs(name, dets, meta={"model_type": mt.name,
                                           "conf_thresh": CONF_THRESH,
                                           "elapse_s": round(float(out.elapse), 3)})


def main(argv=None):
    argv = sys.argv[1:] if argv is None else argv
    only = argv[0] if argv else None

    img = overlay.load_page()
    arr = np.array(img)[:, :, ::-1]  # RGB -> BGR for the opencv-style input

    failed = 0
    for mt in TYPES:
        if only and only.lower() not in mt.name.lower():
            continue
        try:
            run_one(mt, arr)
        except Exception:
            failed += 1
            print(f"!! FAILED {mt.name}")
            traceback.print_exc()
    return 0 if failed == 0 else 1


if __name__ == "__main__":
    sys.exit(main())
