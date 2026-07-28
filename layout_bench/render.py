"""Render page 1 of a PDF to one canonical PNG that every model is fed.

Rendering once and sharing the bitmap is what makes the comparison fair: no model
gets a sharper or differently-scaled input than another.

    python -m layout_bench.render [pdf] [-o page.png]
"""
import argparse
import sys
from pathlib import Path

import fitz  # PyMuPDF

from . import paths

# Fixed target so the longest side lands ~2480px: crisp for small text, still fast.
TARGET_LONG_EDGE = 2480.0


def render(pdf, out, page_index=0, target=TARGET_LONG_EDGE):
    doc = fitz.open(pdf)
    page = doc[page_index]
    w, h = page.rect.width, page.rect.height
    zoom = target / max(w, h)
    pix = page.get_pixmap(matrix=fitz.Matrix(zoom, zoom), alpha=False)
    out.parent.mkdir(parents=True, exist_ok=True)
    pix.save(out)
    print(f"rendered {pdf} -> {out}  {pix.width}x{pix.height}px  (zoom={zoom:.3f})")
    return out


def main(argv=None):
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("pdf", nargs="?", default=paths.PDF,
                    help="PDF to render (default: $LB_PDF)")
    ap.add_argument("-o", "--out", default=paths.PAGE,
                    help="output PNG (default: $LB_PAGE)")
    ap.add_argument("-p", "--page", type=int, default=0, help="0-based page index")
    args = ap.parse_args(argv)

    if not args.pdf:
        ap.error("no PDF given and $LB_PDF is not set")
    render(args.pdf, Path(args.out), args.page)
    return 0


if __name__ == "__main__":
    sys.exit(main())
