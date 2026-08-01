# layout-bench

**Which document layout detector should you actually use?**

`layout-bench` runs **20 document layout detection models** over the same page and
puts their output side by side — as labelled bounding-box overlays, as raw JSON, and
as a scrollable HTML gallery. It ships with results for a **41-document corpus**
(résumés, forms, exam papers, academic papers, reports, financial filings,
timetables, datasheets) and a written [comparative analysis](docs/analysis.md).

Every model sees a byte-identical input bitmap, so differences in the output are
differences in the model — not in the rendering.

## Headline result

Ranked by consensus F1 across 41 documents — top five, plus the recommended model at
its actual rank (full table and methodology in [`docs/analysis.md`](docs/analysis.md),
reproduce with `python -m layout_bench.consensus`):

| # | Model | F1 | Precision | Recall | dup% | Classes |
|--:|---|--:|--:|--:|--:|--:|
| 1 | `rapidlayout-doclayout_docsynth` | **0.869** | **0.951** | 0.801 | 5.7 | 11 |
| 2 | `docling-heron` | 0.860 | 0.794 | **0.938** | 26.2 | 15 |
| 3 | `docling-heron-101` | 0.854 | 0.790 | 0.928 | 24.9 | 14 |
| 4 | `docling-egret-medium` | 0.846 | 0.803 | 0.893 | 18.6 | 14 |
| 5 | `docling-egret-xlarge` | 0.846 | 0.810 | 0.884 | 22.9 | 14 |
| 8 | **`rapidlayout-pp_doc_layoutv2`** | 0.841 | 0.842 | 0.840 | **0.0** | 20 |

**Recommendation: `rapidlayout-pp_doc_layoutv2`.** Raw F1 rank is the wrong thing to
read here: the models above it buy their score on a single axis, by abstaining
(`docsynth`, recall 0.801) or by over-detecting (`heron`, precision 0.794). `v2` is
still the **only model above 0.83 on precision *and* recall at once**, it emits **zero
duplicate boxes** (no NMS pass needed downstream), and it has the richest useful
vocabulary — the only family that separates charts from images and headers from
footers. Reach for `docling-heron` instead when recall matters more than cleanliness,
but budget for a dedup pass: a quarter of its boxes overlap each other.

## Models covered

| Family | Models | Venv |
|---|---|---|
| **RapidLayout** (ONNX) | `pp_doc_layoutv2`, `pp_doc_layoutv3`, `pp_layout_cdla`, `pp_layout_publaynet`, `pp_layout_table`, `doclayout_docstructbench`, `doclayout_d4la`, `doclayout_docsynth`, `yolov8n_layout_{paper,report,general6,publaynet}` | `onnx` |
| **Docling / Aryn** (HF) | `docling-layout-heron`, `heron-101`, `egret-medium`, `egret-large`, `egret-xlarge`, `Aryn/deformable-detr-DocLayNet` | `torch` |
| **Table Transformer** | `microsoft/table-transformer-detection` | `torch` |
| **Unstructured** | `yolox_l` | `unstructured` |

## Quickstart

Requires Python 3.9+ (3.12 recommended). All model weights download automatically on
first run — budget ~4 GB of disk and a slow first pass.

```bash
git clone https://github.com/Bhanubathini2002/layout-bench.git
cd layout-bench
```

**1. Create the virtualenvs**

```powershell
powershell -ExecutionPolicy Bypass -File setup.ps1     # Windows
```

```bash
./setup.sh                                             # macOS / Linux
```

This builds four isolated venvs under `.venvs/` — `base`, `onnx`, `torch`,
`unstructured`. They are separate on purpose: `rapid-layout` and
`unstructured-inference` pin conflicting `onnxruntime` and `torch` versions, so a
single environment cannot hold all 20 models.

**2. Run the benchmark**

```bash
python bench.py --all                          # every PDF in data/pdfs/
python bench.py data/pdfs/sbvwbwjptgts.pdf     # a single document
python bench.py --all --force                  # redo docs that already have results
```

**3. Look at the results**

```bash
start results/sbvwbwjptgts/index.html          # Windows
open  results/sbvwbwjptgts/index.html          # macOS
```

Each document folder gets:

```
results/<document>/
├── index.html                    # gallery: all 20 overlays, grouped by model family
├── SUMMARY.md                    # region and class counts per model
└── <model-name>/
    ├── overlay.png               # the page with colour-coded, labelled boxes
    └── detections.json           # {label, score, box:[x0,y0,x1,y1]} in page pixels
```

## Useful flags

```bash
# only run one stage — handy when you have set up just one venv
python bench.py --all --stage render --stage rapidlayout --stage summary

# run one model family directly, with a name filter
.venvs/onnx/bin/python  -m layout_bench.runners.rapidlayout pp_doc
.venvs/torch/bin/python -m layout_bench.runners.transformers_det docling-heron

# rebuild a report from existing detections.json files
.venvs/base/bin/python -m layout_bench.summary results/sbvwbwjptgts

# re-derive the corpus-wide ranking from the committed detections (stdlib only)
python -m layout_bench.consensus
python -m layout_bench.consensus --format json
```

A missing venv is **skipped with a warning**, not treated as fatal — so you can set up
only `base` + `onnx` and still get 12 of the 20 models. Point the driver at existing
interpreters with `LB_PY_BASE`, `LB_PY_ONNX`, `LB_PY_TORCH`, `LB_PY_UNSTRUCTURED`.

## How it works

```
data/pdfs/doc.pdf
      │
      ├─ render     page 1 → .cache/page.png at a fixed 2480px long edge   [base venv]
      │
      ├─ rapidlayout    12 ONNX models     ─┐
      ├─ transformers    7 HF models        ├─ each writes overlay.png + detections.json
      ├─ yolox           1 ONNX model      ─┘
      │
      └─ summary    → results/doc/SUMMARY.md + index.html                  [base venv]
```

Rendering once up front is the point: a model that looks better because it was handed
a sharper bitmap has not told you anything. `bench.py` passes each stage its paths via
`LB_PDF` / `LB_PAGE` / `LB_OUTROOT` / `LB_DOC`, so every runner is also usable standalone.

## Adding a model

For a HuggingFace object-detection model, add one line to `MODELS` in
[`layout_bench/runners/transformers_det.py`](layout_bench/runners/transformers_det.py):

```python
("my-model", "org/my-layout-model", 0.5),   # (output folder, HF repo, score threshold)
```

For anything else, write a runner that produces a list of
`{"label": str, "score": float | None, "box": [x0, y0, x1, y1]}` in page-pixel
coordinates and hands it to `overlay.save_outputs(name, detections)`. Register it in
`STAGES` in `bench.py`. The report picks it up automatically.

## Caveats

- **There is no human-labeled ground truth here.** The ranking uses a consensus proxy:
  boxes from all 20 models pooled, clustered at IoU > 0.6, and a cluster backed by ≥ 6
  models accepted as a region. This rewards agreeing with the majority and punishes
  being uniquely right. Hand-labeling 5–10 pages is the highest-value next step.
- Only **page 1** of each PDF is benchmarked.
- The two table specialists are **not broken** — they are single-class models being
  scored against an all-region consensus, so their F1 is near zero by construction.
  Given table-heavy pages they fire reliably: `table-transformer-detection` hits 10 of
  the 14 table-rich documents added in the latest pass, against 8 of the original 27.
  Read their rows as "found the table", not as a quality ranking.
- The docling checkpoints take class names from their config, and the casing has
  changed between `transformers` releases — the same model spells `Section-header` or
  `section_header` depending on when its results were produced. Boxes are unaffected;
  the scorer folds the spellings together when counting vocabulary.
- The corpus in `data/pdfs/` is included so results are reproducible. It holds 42
  files but 41 unique documents — `Testdataset.pdf` is a byte-identical copy of
  `kjgpnnkvvjcm.pdf`, kept as a fixed smoke-test document, and is scored once.

## Repo layout

```
bench.py                  driver — stdlib only, runs with any Python 3.9+
layout_bench/
  paths.py                repo-relative paths, all env-overridable
  render.py               PDF → canonical PNG
  overlay.py              box drawing, colour assignment, JSON output
  summary.py              SUMMARY.md + index.html gallery
  consensus.py            corpus-wide ranking from the committed detections
  runners/                one module per model family
requirements/             one txt per venv
setup.ps1 / setup.sh      venv creation
data/pdfs/                the corpus — 42 files, 41 unique documents
results/                  committed results for every document
docs/analysis.md          full 20-model comparative analysis
```

## License

MIT — see [LICENSE](LICENSE). The models themselves carry their own licenses.
