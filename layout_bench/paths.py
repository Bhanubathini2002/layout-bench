"""Repo-relative paths, all overridable by environment variable.

The driver (`bench.py`) sets LB_PDF / LB_PAGE / LB_OUTROOT / LB_DOC before invoking
each runner, so the runners themselves stay path-agnostic and can be run standalone.
"""
import os
from pathlib import Path

REPO = Path(__file__).resolve().parent.parent

# Where the input corpus lives, and where per-document results are written.
PDF_DIR = Path(os.environ.get("LB_PDF_DIR", REPO / "data" / "pdfs"))
RESULTS = Path(os.environ.get("LB_RESULTS", REPO / "results"))

# Set per document by bench.py.
PDF = os.environ.get("LB_PDF")                       # absolute path to the PDF being run
DOC = os.environ.get("LB_DOC", "document")           # human label used in the report
PAGE = Path(os.environ.get("LB_PAGE", REPO / ".cache" / "page.png"))
OUTROOT = Path(os.environ.get("LB_OUTROOT", RESULTS / "current"))


def results_dir_for(pdf_path) -> Path:
    """results/<pdf stem>/ — one folder per document."""
    return RESULTS / Path(pdf_path).stem
