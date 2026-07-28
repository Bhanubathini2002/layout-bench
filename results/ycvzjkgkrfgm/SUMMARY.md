# Layout model benchmark — ycvzjkgkrfgm.pdf

Canonical input: `layout_bench/page.png` (1754x2480). 20 models tested. Each folder has `overlay.png` + `detections.json`.

| Model | #Regions | #Classes | Notes |
|---|--:|--:|---|
| `rapidlayout-pp_doc_layoutv2` | 46 | 7 | text:19, paragraph_title:13, chart:9, image:2, display_formula:1 |
| `rapidlayout-pp_doc_layoutv3` | 46 | 7 | text:19, paragraph_title:13, chart:6, image:4, doc_title:2 |
| `rapidlayout-doclayout_docsynth` | 39 | 5 | Text:13, Section-header:13, List-item:7, Picture:5, Title:1 |
| `rapidlayout-doclayout_d4la` | 36 | 9 | Figure:8, ListText:7, ParaText:6, RegionTitle:4, Table:3 |
| `rapidlayout-doclayout_docstructbench` | 33 | 4 | plain text:15, title:15, abandon:2, figure:1 |
| `docling-egret-medium` | 61 | 5 | Text:20, Section-header:19, Picture:11, List-item:9, Formula:2 |
| `docling-egret-large` | 58 | 5 | Text:25, Section-header:16, List-item:10, Picture:6, Title:1 |
| `docling-egret-xlarge` | 57 | 5 | Text:17, Section-header:16, List-item:12, Picture:11, Formula:1 |
| `docling-heron` | 55 | 5 | text:18, section_header:17, picture:11, list_item:8, formula:1 |
| `docling-heron-101` | 54 | 5 | Section-header:16, Text:15, Picture:11, List-item:11, Formula:1 |
| `aryn-deformable-detr-DocLayNet` | 28 | 5 | Section-header:11, Text:6, List-item:5, Picture:5, Formula:1 |
| `unstructured-yolox` | 40 | 5 | Section-header:13, Text:11, List-item:8, Picture:7, Title:1 |
| `rapidlayout-yolov8n_layout_general6` | 30 | 4 | Title:12, Text:9, Figure:8, Table:1 |
| `rapidlayout-yolov8n_layout_paper` | 21 | 5 | Text:10, Figure:5, Title:4, Equation:1, Footer:1 |
| `rapidlayout-yolov8n_layout_report` | 21 | 5 | Title:8, Text:6, Figure:5, Figure caption:1, Table:1 |
| `rapidlayout-yolov8n_layout_publaynet` | 1 | 1 | Figure:1 |
| `rapidlayout-pp_layout_cdla` | 7 | 4 | title:2, text:2, footer:2, figure:1 |
| `rapidlayout-pp_layout_publaynet` | 1 | 1 | figure:1 |
| `rapidlayout-pp_layout_table` | 0 | 0 |  |
| `table-transformer-detection` | 1 | 1 | table:1 |