# Layout model benchmark — pqsvxnstssmh.pdf

Canonical input: `layout_bench/page.png` (1754x2480). 20 models tested. Each folder has `overlay.png` + `detections.json`.

| Model | #Regions | #Classes | Notes |
|---|--:|--:|---|
| `rapidlayout-pp_doc_layoutv2` | 4 | 3 | table:2, number:1, figure_title:1 |
| `rapidlayout-pp_doc_layoutv3` | 3 | 2 | table:2, number:1 |
| `rapidlayout-doclayout_docstructbench` | 3 | 3 | title:1, abandon:1, figure:1 |
| `rapidlayout-doclayout_docsynth` | 3 | 3 | Table:1, Section-header:1, Page-footer:1 |
| `rapidlayout-doclayout_d4la` | 1 | 1 | RegionList:1 |
| `docling-heron-101` | 20 | 4 | Text:11, Section-header:7, Page-footer:1, Picture:1 |
| `docling-egret-medium` | 15 | 3 | Section-header:8, Text:6, Page-footer:1 |
| `docling-heron` | 15 | 3 | section_header:8, text:6, page_footer:1 |
| `docling-egret-xlarge` | 14 | 3 | Section-header:7, Text:6, Page-footer:1 |
| `docling-egret-large` | 10 | 3 | Text:5, Section-header:4, Page-footer:1 |
| `aryn-deformable-detr-DocLayNet` | 1 | 1 | Page-footer:1 |
| `rapidlayout-yolov8n_layout_paper` | 8 | 5 | Equation:3, Text:2, Table caption:1, Header:1, Title:1 |
| `unstructured-yolox` | 4 | 3 | Table:2, Page-footer:1, Caption:1 |
| `rapidlayout-yolov8n_layout_general6` | 2 | 2 | Title:1, Text:1 |
| `rapidlayout-yolov8n_layout_report` | 2 | 2 | Table:1, Title:1 |
| `rapidlayout-yolov8n_layout_publaynet` | 0 | 0 |  |
| `rapidlayout-pp_layout_cdla` | 3 | 3 | header:1, footer:1, text:1 |
| `rapidlayout-pp_layout_publaynet` | 3 | 3 | table:1, figure:1, title:1 |
| `rapidlayout-pp_layout_table` | 2 | 1 | table:2 |
| `table-transformer-detection` | 1 | 1 | table rotated:1 |