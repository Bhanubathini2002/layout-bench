# Layout Model Benchmark — Comparative Analysis

**Corpus:** 27 documents (`layout_bench_outputs -*`) × 20 layout detection models
**Inputs:** first page of each PDF rendered to `layout_bench/page.png`, sizes 1595–2480 px on the long edge
**Artifacts per model/doc:** `detections.json` (label, score, box) + `overlay.png`
**Date of analysis:** 2026-07-26

---

## 1. Methodology

There is **no human-labeled ground truth** in this benchmark, so the ranking combines four independent signals:

1. **Consensus F1 (pseudo-ground-truth).** For every page, all 20 models' boxes were pooled and clustered at IoU > 0.6. A cluster supported by **≥ 6 of 20 models** was accepted as a consensus region. Each model was then scored for precision and recall against that consensus set.
2. **Geometric cleanliness.** Percentage of a model's boxes that duplicate another of its own boxes (IoU > 0.5), and percentage fully nested inside a larger box of its own (containment > 0.9). Both indicate output that needs post-processing before use.
3. **Label semantics.** Size of the class vocabulary actually emitted across the corpus, and whether it distinguishes structurally useful types (table, chart, formula, header/footer, caption).
4. **Visual inspection.** Overlays reviewed on three representative pages: a dense multi-column résumé (`cnpkkjdkyhhw`, ~67 regions), a table-headed exam template (`qtsmnthhhrpd`), and an academic paper (`sbvwbwjptgts`).

**Caveat:** consensus is not ground truth. It systematically rewards agreement with the majority and penalizes a model that is uniquely correct about something the others miss. Labeling even 5 pages by hand would firm this up considerably.

---

## 2. Full results — all 20 models

Sorted by consensus F1. `dup%` and `nest%` are *lower is better*; `vocab` is the number of distinct classes emitted across the whole corpus; `cls/doc` is the mean per page.

| # | Model | Docs | mean N | F1 | Prec | Rec | dup% | nest% | conf | vocab | cls/doc |
|--:|---|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|
| 1 | `rapidlayout-doclayout_docsynth` | 27/27 | 20.9 | **0.857** | 0.938 | 0.789 | 6.7 | 1.6 | 0.77 | 11 | 4.0 |
| 2 | `docling-heron` | 27/27 | 35.7 | 0.838 | 0.768 | **0.922** | 24.8 | 20.6 | 0.76 | 15 | 5.4 |
| 3 | **`rapidlayout-pp_doc_layoutv2`** | 27/27 | 25.1 | 0.832 | 0.833 | 0.830 | **0.0** | 2.2 | **0.84** | 20 | 5.6 |
| 4 | `docling-heron-101` | 27/27 | 36.2 | 0.829 | 0.757 | 0.917 | 26.7 | 19.4 | 0.77 | 14 | 5.4 |
| 5 | `docling-egret-xlarge` | 27/27 | 33.0 | 0.829 | 0.806 | 0.853 | 20.9 | 14.8 | 0.78 | 13 | 5.0 |
| 6 | `rapidlayout-pp_doc_layoutv3` | 27/27 | 23.7 | 0.822 | 0.865 | 0.783 | 0.0 | 0.2 | 0.75 | 18 | 4.9 |
| 7 | `unstructured-yolox` | 27/27 | 20.5 | 0.817 | 0.864 | 0.775 | 0.0 | 2.4 | 0.63 | 11 | 4.0 |
| 8 | `docling-egret-medium` | 27/27 | 33.3 | 0.806 | 0.763 | 0.855 | 14.2 | 19.6 | 0.75 | 13 | 4.6 |
| 9 | `docling-egret-large` | 27/27 | 32.9 | 0.803 | 0.757 | 0.856 | 18.8 | 24.8 | 0.75 | 15 | 4.9 |
| 10 | `rapidlayout-doclayout_docstructbench` | 27/27 | 18.1 | 0.791 | 0.915 | 0.697 | 4.7 | 0.6 | 0.77 | 9 | 3.4 |
| 11 | `rapidlayout-yolov8n_layout_general6` | 27/27 | 16.2 | 0.748 | **0.946** | 0.618 | 3.9 | 1.5 | 0.68 | 6 | 2.8 |
| 12 | `rapidlayout-doclayout_d4la` | 27/27 | 18.1 | 0.709 | 0.823 | 0.623 | 6.4 | 3.7 | 0.75 | **25** | 6.9 |
| 13 | `rapidlayout-yolov8n_layout_report` | 27/27 | 18.7 | 0.706 | 0.800 | 0.631 | 6.8 | 9.5 | 0.68 | 8 | 3.8 |
| 14 | `aryn-deformable-detr-DocLayNet` | 25/27 | 13.9 | 0.617 | 0.868 | 0.478 | 0.0 | 0.0 | 0.73 | 11 | 3.0 |
| 15 | `rapidlayout-yolov8n_layout_paper` | 27/27 | 13.9 | 0.603 | 0.815 | 0.478 | 5.3 | 4.9 | 0.68 | 10 | 3.9 |
| 16 | `rapidlayout-pp_layout_cdla` | 27/27 | 11.3 | 0.557 | 0.726 | 0.452 | 19.9 | 6.3 | 0.76 | 10 | 3.9 |
| 17 | `rapidlayout-pp_layout_publaynet` | 26/27 | 9.3 | 0.556 | 0.781 | 0.432 | 8.7 | 12.3 | 0.69 | 5 | 2.0 |
| 18 | `rapidlayout-yolov8n_layout_publaynet` | 26/27 | 4.7 | 0.350 | 0.696 | 0.233 | 0.0 | 6.4 | 0.67 | 4 | 1.7 |
| 19 | `rapidlayout-pp_layout_table` | 6/27 | 0.5 | 0.043 | 0.123 | 0.026 | — | — | 0.60 | 1 | 0.2 |
| 20 | `table-transformer-detection` | 8/27 | 0.3 | 0.036 | 0.111 | 0.021 | — | — | 0.89 | 2 | 0.3 |

> **Reading the F1 column:** raw F1 rank is misleading on its own. `docsynth` tops it by being conservative, and `heron` places high by over-detecting — both are single-axis wins. Only `pp_doc_layoutv2` clears 0.83 on **precision and recall simultaneously**.

### A note on the "coverage %" metric

An earlier pass ranked models by union page-area coverage. That column is discarded here: `pp_layout_publaynet` (51.1%) and `yolov8n_layout_publaynet` (49.9%) top it only because they emit a handful of page-sized blobs. High area, no granularity. Coverage rewards coarseness and is not a quality signal on this corpus.

---

## 3. Visual findings

### `cnpkkjdkyhhw` — dense two-column résumé (tables, bar chart, avatar, social icons, footer)

- **`pp_doc_layoutv2`** — cleanest result of the whole corpus. Correctly separated `doc_title` / `header`, both tables as `table`, the skills bar chart as `chart`, the Disney/skull logos as `image`, the contact strip as `footer`, and the page number as `number`. 67 regions, 10 classes, no visible overlap.
- **`docling-heron`** — visibly noisy. Stacked overlapping boxes across the footer, stamped `picture` over plain text and small icons, and missed **both tables**, classifying them as `key_value_region` with nested children inside.
- **`pp_doc_layoutv3`** — missed **both tables and the bar chart** that v2 caught, and dropped several small text runs. Lower confidences throughout (many in the 0.4–0.6 band vs v2's 0.7–0.9).
- **`doclayout_docsynth`** — high precision but by omission: labeled the document title, the bar chart, **and** the Languages table all as `Picture`, missed the footer entirely, and skipped the "Areas of specialization" list.

### `qtsmnthhhrpd` — exam template with a header table

- **`pp_doc_layoutv2`** — nailed the multi-cell header table as a single `table`, the section heading as `paragraph_title`, each question block as separate `text` regions, and the page number as `number`. Essentially zero noise.

### `sbvwbwjptgts` — academic paper

- Consistent with the aggregate: the docling family over-segments, `docstructbench` under-detects, `pp_doc_layoutv2` tracks the consensus closely.

---

## 4. Models that failed

| Model | Failure |
|---|---|
| `table-transformer-detection` | Produced output on **8/27** docs, F1 0.036. Mean 0.3 regions/page. Effectively non-functional on this corpus. |
| `rapidlayout-pp_layout_table` | Output on **6/27** docs, F1 0.043. Same story. |
| `rapidlayout-yolov8n_layout_publaynet` | 4.7 regions/page, recall 0.23. Far too coarse to be useful. |
| `aryn-deformable-detr-DocLayNet` | Silent on 2 docs; recall 0.478. Also 6.2% degenerate/tiny boxes — the highest of any model. |

The two table-specialist models are worth a second look before discarding — a 6/27 and 8/27 hit rate suggests a possible preprocessing or threshold problem in the harness rather than genuine model incapacity, especially since `table-transformer` reported the highest mean confidence (0.89) on the few detections it did make.

---

## 5. Recommendations

### 🥇 First choice — `rapidlayout-pp_doc_layoutv2`

**Use this as the default.** The only model strong on all four axes at once.

- Balanced consensus F1 **0.832** with precision 0.833 and recall 0.830 — no other model clears 0.83 on both.
- **0.0% duplicate boxes** and 2.2% nesting: output is directly consumable, no NMS or dedup stage required.
- Highest mean confidence (**0.84**), so score thresholding actually separates good from bad detections.
- Richest *useful* vocabulary — 20 classes including `table`, `chart`, `display_formula`, `inline_formula`, `doc_title`, `figure_title`, `header` / `footer` / `header_image` / `footer_image`, `abstract`, `reference_content`, `footnote`, `number`. This is the only family that distinguishes charts from images and headers from footers.
- Produced output on **27/27** documents.

**Weakness:** at 25.1 regions/page it detects fewer regions than the docling family (33–36). If your downstream task needs every last text fragment, see the hybrid option below.

### 🥈 Second choice — `docling-heron` (requires a dedup pass)

**Use when recall matters more than cleanliness.** Highest recall in the benchmark (**0.922**) and it finds fine-grained regions `pp_doc_layoutv2` misses.

- Recall 0.922 vs v2's 0.830 — genuinely finds more.
- 15-class vocabulary with structurally useful types: `table`, `formula`, `code`, `caption`, `page_header`, `page_footer`, `checkbox_unselected`, `form`.
- Runs on 27/27 docs; `docling-heron-101` is near-identical (F1 0.829, recall 0.917) and interchangeable.

**Mandatory caveat:** **24.8% of its boxes duplicate another of its own boxes** and **20.6% are nested inside a larger one**. Raw output is not usable — it needs a class-aware NMS at IoU ≈ 0.5 plus a containment filter. It also confuses tables with `key_value_region` and over-fires `picture` on text and icons, so table extraction should not depend on it.

### 🥉 Third choice — `rapidlayout-doclayout_docsynth`

**Use when false positives are more costly than misses.** Highest F1 (0.857) and the best precision among models that still detect a reasonable number of regions (**0.938**).

- Precision 0.938 at 20.9 regions/page — when it fires, it is almost always on a real region.
- Low duplication (6.7%) and nesting (1.6%); near drop-in with no post-processing.
- Runs on 27/27 docs.

**Weakness:** only 11 classes (standard DocLayNet set) and it buys its precision by abstaining. On the résumé it labeled the document title, a bar chart, and a table all as `Picture`, and missed the footer entirely. Fine for coarse reading-order and text-block extraction; unsuitable if you need tables, charts, or formulas identified as such.

### Honorable mentions

- **`rapidlayout-pp_doc_layoutv3`** — same family and vocabulary as the winner, cleanest geometry of any model (0.0% dup, 0.2% nest), but **strictly worse than v2 on this corpus**: missed tables and charts v2 caught, fewer classes per page (4.9 vs 5.6), lower confidence (0.75 vs 0.84). Newer version number, not better results. Keep only as a same-family fallback.
- **`rapidlayout-doclayout_d4la`** — by far the richest vocabulary (25 classes, including `LetterHead`, `LetterSign`, `RegionKV`, `PageNumber`). If your corpus is letters or forms and you need those specific labels, it may be worth the recall hit (0.623).
- **`unstructured-yolox`** — unremarkable but honest: F1 0.817, 0% duplication, 11 classes. A reasonable no-surprises baseline.

### Best combined configuration

For maximum recall with usable output:

```
pp_doc_layoutv2  ∪  docling-heron   →  class-aware NMS @ IoU 0.5  →  drop boxes >90% contained in a larger box
```

`docling-heron` contributes real regions v2 misses; the NMS stage removes heron's ~25% duplicates. Prefer v2's label when the two disagree on an overlapping region — v2's table/chart/formula distinctions are more reliable.

### Drop from the benchmark

`table-transformer-detection`, `rapidlayout-pp_layout_table`, `rapidlayout-yolov8n_layout_publaynet`, `rapidlayout-pp_layout_publaynet` — all four are below F1 0.56, and the first two are functionally dead. Re-verify the two table models' harness configuration before permanently discarding them.

---

## 6. Next step

The single highest-value action is to hand-label **5–10 representative pages** (one résumé, one form, one paper, one slide, one table-heavy page). Real ground truth would replace the consensus proxy, resolve whether `docling-heron`'s extra 0.09 recall is signal or noise, and confirm whether `docsynth`'s 0.938 precision survives contact with regions the majority of models miss.
