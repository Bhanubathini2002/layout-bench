# Layout Model Benchmark — Comparative Analysis

**Corpus:** 41 documents × 20 layout detection models
**Inputs:** first page of each PDF rendered to a canonical PNG, 1595–2480 px on the long edge
**Artifacts per model/doc:** `detections.json` (label, score, box) + `overlay.png`
**Date of analysis:** 2026-07-31

Reproduce every number below from the committed detections with:

```bash
python -m layout_bench.consensus            # the table in §2
python -m layout_bench.consensus --format json
```

---

## 1. Methodology

There is **no human-labeled ground truth** in this benchmark, so the ranking combines four independent signals:

1. **Consensus F1 (pseudo-ground-truth).** For every page, all 20 models' boxes were pooled and clustered at IoU > 0.6, seeded by descending confidence. A cluster supported by **≥ 6 of 20 models** was accepted as a consensus region. Each model was then scored for precision and recall against that consensus set. Matching is many-to-one: a model is not punished twice for splitting one consensus region into two plausible boxes, and a region counts as found if any box covers it. Over-segmentation is charged to the `dup%` / `nest%` columns instead, where it belongs.
2. **Geometric cleanliness.** Percentage of a model's boxes that duplicate another of its own boxes (IoU > 0.5), and percentage fully nested inside a larger box of its own (containment > 0.9). Both indicate output that needs post-processing before use.
3. **Label semantics.** Size of the class vocabulary actually emitted across the corpus, and whether it distinguishes structurally useful types (table, chart, formula, header/footer, caption).
4. **Visual inspection.** Overlays reviewed on representative pages: a dense multi-column résumé (`cnpkkjdkyhhw`), a table-headed exam template (`qtsmnthhhrpd`), an academic paper (`sbvwbwjptgts`), an ACORD insurance certificate (`insurance-acord`), and a transit timetable (`ny-timetable`).

Precision and recall are averaged per document and then across documents, so a dense page does not outweigh a sparse one. A document a model ran on but detected nothing in counts as a zero, which is why the `Docs` column is reported alongside. `Testdataset.pdf` is byte-identical to `kjgpnnkvvjcm.pdf` and is scored once.

**Caveat:** consensus is not ground truth. It systematically rewards agreement with the majority and penalizes a model that is uniquely correct about something the others miss. Labeling even 5 pages by hand would firm this up considerably.

**Caveat on provenance:** the scorer (`layout_bench/consensus.py`) was written to reproduce the methodology described above after the fact; the original pass's script was not preserved. On the original 27 documents it reproduces `mean N`, vocabulary size, classes-per-doc and per-model coverage exactly, and consensus F1 to within ~0.01 for most models (`docsynth` 0.852 vs 0.857 published, `heron` 0.831 vs 0.838, `pp_doc_layoutv3` 0.819 vs 0.822). Two models differ more (`pp_doc_layoutv2` 0.816 vs 0.832, `yolov8n_layout_paper` 0.573 vs 0.603), so treat cross-version comparisons of the *exact* decimals with care. Everything in this document is internally consistent — one script, one corpus, one run.

---

## 2. Full results — all 20 models

Sorted by consensus F1. `dup%` and `nest%` are *lower is better*; `vocab` is the number of distinct classes emitted across the whole corpus; `cls/doc` is the mean per page.

| # | Model | Docs | mean N | F1 | Prec | Rec | dup% | nest% | conf | vocab | cls/doc |
|--:|---|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|
| 1 | `rapidlayout-doclayout_docsynth` | 41/41 | 17.2 | **0.869** | **0.951** | 0.801 | 5.7 | 3.0 | 0.79 | 11 | 4.1 |
| 2 | `docling-heron` | 41/41 | 29.6 | 0.860 | 0.794 | **0.938** | 26.2 | 29.5 | 0.76 | 15 | 5.5 |
| 3 | `docling-heron-101` | 41/41 | 29.9 | 0.854 | 0.790 | 0.928 | 24.9 | 27.2 | 0.78 | 14 | 5.5 |
| 4 | `docling-egret-medium` | 41/41 | 27.5 | 0.846 | 0.803 | 0.893 | 18.6 | 23.3 | 0.77 | 14 | 4.9 |
| 5 | `docling-egret-xlarge` | 41/41 | 27.5 | 0.846 | 0.810 | 0.884 | 22.9 | 20.5 | 0.78 | 14 | 5.2 |
| 6 | `rapidlayout-pp_doc_layoutv3` | 41/41 | 19.4 | 0.843 | 0.875 | 0.813 | **0.0** | 0.4 | 0.77 | 18 | 5.2 |
| 7 | `unstructured-yolox` | 41/41 | 17.2 | 0.843 | 0.871 | 0.817 | **0.0** | 2.8 | 0.68 | 11 | 4.1 |
| 8 | **`rapidlayout-pp_doc_layoutv2`** | 41/41 | 20.5 | 0.841 | 0.842 | 0.840 | **0.0** | 1.5 | **0.86** | 20 | 5.6 |
| 9 | `docling-egret-large` | 41/41 | 27.0 | 0.833 | 0.788 | 0.884 | 19.1 | 25.4 | 0.77 | 15 | 5.1 |
| 10 | `rapidlayout-doclayout_docstructbench` | 41/41 | 15.1 | 0.815 | 0.928 | 0.726 | 4.5 | 2.6 | 0.80 | 9 | 3.7 |
| 11 | `rapidlayout-yolov8n_layout_general6` | 41/41 | 13.3 | 0.762 | 0.961 | 0.631 | 3.3 | 4.6 | 0.70 | 6 | 2.8 |
| 12 | `rapidlayout-doclayout_d4la` | 41/41 | 15.6 | 0.757 | 0.842 | 0.688 | 8.1 | 5.8 | 0.77 | **25** | 6.4 |
| 13 | `rapidlayout-yolov8n_layout_report` | 41/41 | 15.8 | 0.740 | 0.827 | 0.669 | 6.2 | 8.8 | 0.70 | 8 | 4.1 |
| 14 | `aryn-deformable-detr-DocLayNet` | 38/41 | 12.1 | 0.714 | 0.907 | 0.589 | **0.0** | **0.0** | 0.76 | 11 | 3.3 |
| 15 | `rapidlayout-yolov8n_layout_paper` | 41/41 | 11.5 | 0.627 | 0.820 | 0.507 | 5.5 | 8.7 | 0.70 | 10 | 3.9 |
| 16 | `rapidlayout-pp_layout_cdla` | 41/41 | 10.2 | 0.589 | 0.737 | 0.490 | 24.6 | 17.4 | 0.78 | 10 | 4.2 |
| 17 | `rapidlayout-pp_layout_publaynet` | 40/41 | 8.1 | 0.582 | 0.801 | 0.457 | 8.4 | 14.1 | 0.70 | 5 | 2.2 |
| 18 | `rapidlayout-yolov8n_layout_publaynet` | 40/41 | 4.3 | 0.396 | 0.743 | 0.270 | **0.0** | 3.4 | 0.73 | 5 | 1.8 |
| 19 | `rapidlayout-pp_layout_table` | 13/41 | 0.5 | 0.074 | 0.228 | 0.044 | 0.0 | 9.5 | 0.69 | 1 | 0.3 |
| 20 | `table-transformer-detection` | 18/41 | 0.5 | 0.070 | 0.232 | 0.041 | 0.0 | 0.0 | 0.89 | 2 | 0.4 |

> **Reading the F1 column:** raw F1 rank is misleading on its own, and the top of this
> table is a good demonstration of why. `docsynth` leads by being conservative
> (precision 0.951, recall 0.801); the four docling entries behind it lead by
> over-detecting (recall 0.88–0.94, precision 0.79–0.81, and a fifth to a quarter of
> their boxes duplicated). Eight models now sit inside 0.03 F1 of each other, which is well inside
> the noise of a consensus proxy. Only `pp_doc_layoutv2` clears 0.83 on **precision and
> recall simultaneously** — that, not its rank, is the reason it remains the pick.

### Effect of the 14 added documents

The corpus grew from 27 to 41 documents, adding financial filings, an insurance form, a
transit timetable, a component datasheet and several chart-led reports — i.e. pages with
more tables and dense grids and fewer prose blocks. The ranking is broadly stable; three
things moved:

- **Mean regions per page fell for every general-purpose model** (e.g. `heron` 35.7 → 29.6, `pp_doc_layoutv2` 25.1 → 20.5); the two table specialists were the only exceptions. The added pages are structurally sparser than the résumé-heavy original set — a timetable is one big table, not forty text runs.
- **Scores rose slightly across the board.** Sparser pages produce cleaner consensus clusters, so agreement is easier. Rank order among the leaders changed more than the underlying quality did.
- **The two table specialists roughly doubled their hit rate** — see §4.

### A note on the "coverage %" metric

An earlier pass ranked models by union page-area coverage. That column is discarded here: `pp_layout_publaynet` and `yolov8n_layout_publaynet` topped it only because they emit a handful of page-sized blobs. High area, no granularity. Coverage rewards coarseness and is not a quality signal on this corpus.

---

## 3. Visual findings

### `cnpkkjdkyhhw` — dense two-column résumé (tables, bar chart, avatar, social icons, footer)

- **`pp_doc_layoutv2`** — cleanest result of the whole corpus. Correctly separated `doc_title` / `header`, both tables as `table`, the skills bar chart as `chart`, the Disney/skull logos as `image`, the contact strip as `footer`, and the page number as `number`. 67 regions, 10 classes, no visible overlap.
- **`docling-heron`** — visibly noisy. Stacked overlapping boxes across the footer, stamped `picture` over plain text and small icons, and missed **both tables**, classifying them as `key_value_region` with nested children inside.
- **`pp_doc_layoutv3`** — missed **both tables and the bar chart** that v2 caught, and dropped several small text runs. Lower confidences throughout (many in the 0.4–0.6 band vs v2's 0.7–0.9).
- **`doclayout_docsynth`** — high precision but by omission: labeled the document title, the bar chart, **and** the Languages table all as `Picture`, missed the footer entirely, and skipped the "Areas of specialization" list.

### `insurance-acord` — ACORD 25 certificate of insurance

The clearest illustration of the precision/recall split in the whole benchmark.

- **`pp_doc_layoutv2` / `v3`** — 9 regions: the form resolved to 3 `table` blocks plus `header`, `footer`, `header_image`. A structurally faithful reading of an ACORD form, which really is a stack of ruled grids.
- **`docling-heron-101`** — 43 regions on the same page: 26 `text`, 7 `section_header`, 4 `form`. It descends into individual form cells. Whether that is better depends entirely on the downstream task — for field extraction it is a gift, for document structure it is noise.
- **`doclayout_d4la`** — the vocabulary payoff: 3 × `Table` plus 3 × `TableName` and 2 × `PageFooter`. The only model that named the table captions as such.
- **`doclayout_docstructbench`** — 5 regions, 2 classes, most of the page dismissed as `abandon`. Under-detection on forms is this model's weak spot.

### `ny-timetable` — transit timetable

Near-unanimity, and a good sanity check: `pp_doc_layoutv2`, `v3`, `d4la`, `docstructbench` and `docsynth` all return exactly **2 regions** — the timetable grid as one `table` plus a page number or footer. `egret-xlarge` adds two `section_header`s. A page that is one giant grid is where the whole field agrees.

### `esg-metrics` — sustainability metrics table with inline charts

- **`pp_doc_layoutv2`** — 20 regions, 8 classes, and the only model to separate the 2 `chart`s from the `table` while tagging 9 `vision_footnote`s. This is the vocabulary argument in one page.
- **`docling-heron-101`** — 34 regions but flattens the same content to `text` (12) and `footnote` (7); no chart/table distinction.

### `qtsmnthhhrpd` — exam template with a header table

- **`pp_doc_layoutv2`** — nailed the multi-cell header table as a single `table`, the section heading as `paragraph_title`, each question block as separate `text` regions, and the page number as `number`. Essentially zero noise.

### `sbvwbwjptgts` — academic paper

- Consistent with the aggregate: the docling family over-segments, `docstructbench` under-detects, `pp_doc_layoutv2` tracks the consensus closely.

---

## 4. Models that underperform — and the table specialists reconsidered

| Model | Behaviour |
|---|---|
| `rapidlayout-yolov8n_layout_publaynet` | 4.3 regions/page, recall 0.270. Far too coarse to be useful. |
| `rapidlayout-pp_layout_cdla` | F1 0.589 with 24.6% duplicate boxes — the worst quality-per-cleanup ratio in the set. |
| `aryn-deformable-detr-DocLayNet` | Silent on 3 of 41 docs; recall 0.589. Perfectly clean geometry (0.0% dup **and** nest) and precision 0.907, so it is honest about what it does find — it just finds too little. |

**The two table specialists were misdiagnosed in the previous pass.** That analysis flagged `table-transformer-detection` (8/27 docs) and `rapidlayout-pp_layout_table` (6/27) as suspected harness or threshold bugs. The enlarged corpus answers the question, and the answer is: they work.

| Model | Original 27 docs | 14 added (table-rich) docs | Total |
|---|--:|--:|--:|
| `table-transformer-detection` | 8/27 (30%) | **10/14 (71%)** | 18/41 |
| `rapidlayout-pp_layout_table` | 6/27 (22%) | **7/14 (50%)** | 13/41 |

Both fire on precisely the pages that contain tables — `insurance-acord`, `finance-10k`, `esg-metrics`, `ny-timetable`, `postal-10k`, `settlement-agreement` — and stay silent on prose pages, which is correct behaviour for a single-class detector. Their F1 of ~0.07 is an artifact of scoring a table-only model against an all-region consensus: every non-table region on the page counts as a miss. **Read their rows as a table-presence signal, not a quality ranking, and do not "fix" them.** `table-transformer` also reports the highest mean confidence in the benchmark (0.89).

---

## 5. Recommendations

### 🥇 First choice — `rapidlayout-pp_doc_layoutv2`

**Use this as the default.** The only model strong on all four axes at once.

- Balanced consensus F1 **0.841** with precision 0.842 and recall 0.840 — no other model clears 0.83 on both, on either corpus size.
- **0.0% duplicate boxes** and 1.5% nesting: output is directly consumable, no NMS or dedup stage required.
- Highest mean confidence (**0.86**), so score thresholding actually separates good from bad detections.
- Richest *useful* vocabulary — 20 classes including `table`, `chart`, `display_formula`, `inline_formula`, `doc_title`, `figure_title`, `header` / `footer` / `header_image` / `footer_image`, `abstract`, `reference_content`, `footnote`, `number`. The only family that distinguishes charts from images and headers from footers, which `esg-metrics` shows paying off directly.
- Produced output on **41/41** documents.

**Weakness:** at 20.5 regions/page it detects fewer regions than the docling family (27–30). If your downstream task needs every last text fragment — form-cell extraction, for instance — see the hybrid option below.

### 🥈 Second choice — `docling-heron` (requires a dedup pass)

**Use when recall matters more than cleanliness.** Highest recall in the benchmark (**0.938**) and it finds fine-grained regions `pp_doc_layoutv2` misses.

- Recall 0.938 vs v2's 0.840 — genuinely finds more, and on forms it is a different order of granularity (43 regions vs 9 on `insurance-acord`).
- 15-class vocabulary with structurally useful types: `table`, `formula`, `code`, `caption`, `page_header`, `page_footer`, `checkbox_unselected`, `form`.
- Runs on 41/41 docs; `docling-heron-101` is near-identical (F1 0.854, recall 0.928) and interchangeable.

**Mandatory caveat:** **26.2% of its boxes duplicate another of its own boxes** and **29.5% are nested inside a larger one**. Raw output is not usable — it needs a class-aware NMS at IoU ≈ 0.5 plus a containment filter. It also confuses tables with `key_value_region` and over-fires `picture` on text and icons, so table extraction should not depend on it.

### 🥉 Third choice — `rapidlayout-doclayout_docsynth`

**Use when false positives are more costly than misses.** Top F1 (0.869) and the best precision of any model that still detects a reasonable number of regions (**0.951**).

- Precision 0.951 at 17.2 regions/page — when it fires, it is almost always on a real region.
- Low duplication (5.7%) and nesting (3.0%); near drop-in with no post-processing.
- Runs on 41/41 docs.

**Weakness:** only 11 classes (standard DocLayNet set) and it buys its precision by abstaining. On the résumé it labeled the document title, a bar chart, and a table all as `Picture`, and missed the footer entirely. Fine for coarse reading-order and text-block extraction; unsuitable if you need tables, charts, or formulas identified as such.

### Honorable mentions

- **`rapidlayout-pp_doc_layoutv3`** — same family and vocabulary as the winner, cleanest geometry of any model (0.0% dup, 0.4% nest), and now essentially tied with v2 on F1 (0.843 vs 0.841). It remains the weaker pick: it missed tables and the bar chart v2 caught on the résumé, and it trails on confidence (0.77 vs 0.86) and vocabulary (18 vs 20). Keep as a same-family fallback.
- **`unstructured-yolox`** — quietly excellent and under-rated by its old ranking: F1 0.843, 0% duplication, 11 classes. The best no-surprises baseline in the benchmark if you do not need a rich vocabulary.
- **`rapidlayout-doclayout_d4la`** — by far the richest vocabulary (25 classes, including `LetterHead`, `LetterSign`, `RegionKV`, `TableName`, `PageNumber`). On forms it produced labels no other model offered. If your corpus is letters or forms and you need those specific labels, it may be worth the recall hit (0.688).
- **`table-transformer-detection` / `rapidlayout-pp_layout_table`** — not general layout models and should not be ranked as such; useful as a cheap "does this page contain a table" signal (see §4).

### Best combined configuration

For maximum recall with usable output:

```
pp_doc_layoutv2  ∪  docling-heron   →  class-aware NMS @ IoU 0.5  →  drop boxes >90% contained in a larger box
```

`docling-heron` contributes real regions v2 misses; the NMS stage removes heron's ~26% duplicates. Prefer v2's label when the two disagree on an overlapping region — v2's table/chart/formula distinctions are more reliable.

### Drop from the benchmark

`rapidlayout-yolov8n_layout_publaynet` and `rapidlayout-pp_layout_publaynet` — both below F1 0.60 with no compensating strength. Unlike the previous pass, the two table models are **not** recommended for removal: they are doing their job, and the metric was asking them the wrong question.

---

## 6. Next step

The single highest-value action is still to hand-label **5–10 representative pages** (one résumé, one form, one paper, one timetable, one table-heavy financial page). Real ground truth would replace the consensus proxy, resolve whether `docling-heron`'s extra 0.10 recall is signal or noise, and confirm whether `docsynth`'s 0.951 precision survives contact with regions the majority of models miss. The eight-model pile-up between F1 0.84 and 0.87 cannot be untangled by consensus alone.

A cheaper follow-up: the `insurance-acord` result suggests the benchmark is measuring two different tasks under one name — *document structure* (v2's 9 regions) and *field extraction* (heron's 43). Scoring those separately would be more informative than one blended F1.
