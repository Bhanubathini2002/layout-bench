"""Shared output helpers: load the canonical page, draw labelled bbox overlays, dump JSON.

Only depends on Pillow, which is present in every venv, so all runners can share it.
"""
import colorsys
import json
import os

from PIL import Image, ImageDraw, ImageFont

from . import paths


def load_page():
    return Image.open(paths.PAGE).convert("RGB")


def _font(size):
    candidates = (
        r"C:\Windows\Fonts\arialbd.ttf",
        r"C:\Windows\Fonts\arial.ttf",
        "/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf",
        "/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf",
        "/System/Library/Fonts/Supplemental/Arial Bold.ttf",
    )
    for p in candidates:
        try:
            return ImageFont.truetype(p, size)
        except Exception:
            pass
    return ImageFont.load_default()


def _color_for(idx):
    # golden-ratio hue stepping -> visually distinct saturated colors
    h = (idx * 0.61803398875) % 1.0
    r, g, b = colorsys.hsv_to_rgb(h, 0.75, 0.95)
    return (int(r * 255), int(g * 255), int(b * 255))


def save_outputs(model_name, detections, raw=None, meta=None):
    """Write overlay.png + detections.json for one model.

    detections: list of {"label": str, "score": float|None, "box": [x0,y0,x1,y1]}
    in page.png pixel coordinates.
    """
    outdir = os.path.join(paths.OUTROOT, model_name)
    os.makedirs(outdir, exist_ok=True)

    # stable color per class label
    labels = []
    for d in detections:
        if d["label"] not in labels:
            labels.append(d["label"])
    cmap = {lab: _color_for(i) for i, lab in enumerate(sorted(labels))}

    img = load_page()
    draw = ImageDraw.Draw(img, "RGBA")
    font = _font(20)
    for d in detections:
        x0, y0, x1, y1 = [float(v) for v in d["box"]]
        col = cmap[d["label"]]
        draw.rectangle([x0, y0, x1, y1], outline=col + (255,), width=3)
        draw.rectangle([x0, y0, x1, y1], fill=col + (28,))
        sc = f" {d['score']:.2f}" if d.get("score") is not None else ""
        tag = f"{d['label']}{sc}"
        tb = draw.textbbox((0, 0), tag, font=font)
        tw, th = tb[2] - tb[0], tb[3] - tb[1]
        ly = max(0, y0 - th - 6)
        draw.rectangle([x0, ly, x0 + tw + 8, ly + th + 6], fill=col + (235,))
        draw.text((x0 + 4, ly + 2), tag, fill=(255, 255, 255), font=font)

    # legend, top-left
    ly = 8
    lf = _font(22)
    for lab in sorted(labels):
        col = cmap[lab]
        n = sum(1 for d in detections if d["label"] == lab)
        txt = f"{lab} ({n})"
        tb = draw.textbbox((0, 0), txt, font=lf)
        draw.rectangle([8, ly, 8 + (tb[2] - tb[0]) + 40, ly + (tb[3] - tb[1]) + 10],
                       fill=(255, 255, 255, 235))
        draw.rectangle([12, ly + 4, 32, ly + 24], fill=col + (255,))
        draw.text((40, ly + 3), txt, fill=(0, 0, 0), font=lf)
        ly += (tb[3] - tb[1]) + 14

    img.save(os.path.join(outdir, "overlay.png"))

    counts = {}
    for d in detections:
        counts[d["label"]] = counts.get(d["label"], 0) + 1
    with open(os.path.join(outdir, "detections.json"), "w", encoding="utf-8") as f:
        json.dump({
            "model": model_name,
            "meta": meta or {},
            "num_detections": len(detections),
            "class_counts": counts,
            "detections": detections,
        }, f, indent=2, ensure_ascii=False)
    if raw is not None:
        with open(os.path.join(outdir, "raw.json"), "w", encoding="utf-8") as f:
            json.dump(raw, f, indent=2, ensure_ascii=False, default=str)

    print(f"[{model_name}] {len(detections)} detections -> {outdir}")
    print(f"[{model_name}] classes: {counts}")
