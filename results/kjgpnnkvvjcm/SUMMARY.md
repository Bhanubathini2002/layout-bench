# Layout model benchmark — kjgpnnkvvjcm.pdf

Canonical input: `layout_bench/page.png` (2480x1752). 20 models tested. Each folder has `overlay.png` + `detections.json`.

| Model | #Regions | #Classes | Notes |
|---|--:|--:|---|
| `rapidlayout-pp_doc_layoutv2` | 77 | 10 | text:46, paragraph_title:11, display_formula:7, header:4, footer:3 |
| `rapidlayout-pp_doc_layoutv3` | 72 | 9 | text:42, paragraph_title:12, display_formula:7, header:4, footer:3 |
| `rapidlayout-doclayout_docsynth` | 64 | 7 | Text:27, Section-header:14, List-item:13, Formula:5, Page-footer:3 |
| `rapidlayout-doclayout_docstructbench` | 59 | 7 | plain text:31, title:15, isolate_formula:7, abandon:3, table:1 |
| `rapidlayout-doclayout_d4la` | 47 | 11 | ParaText:18, ListText:12, RegionTitle:4, Equation:2, ParaTitle:2 |
| `docling-egret-large` | 104 | 10 | Text:48, Section-header:18, List-item:16, Formula:7, Picture:5 |
| `docling-egret-medium` | 102 | 10 | Text:47, Section-header:17, List-item:14, Formula:8, Page-header:8 |
| `docling-egret-xlarge` | 102 | 9 | Text:51, List-item:17, Section-header:12, Formula:9, Picture:5 |
| `docling-heron` | 100 | 9 | text:42, list_item:18, section_header:17, formula:7, picture:6 |
| `docling-heron-101` | 99 | 11 | Text:42, Section-header:19, List-item:15, Formula:7, Picture:5 |
| `aryn-deformable-detr-DocLayNet` | 52 | 5 | Text:22, List-item:14, Section-header:10, Formula:4, Page-footer:2 |
| `rapidlayout-yolov8n_layout_report` | 57 | 8 | Text:40, Title:10, Table:2, Figure:1, Figure caption:1 |
| `rapidlayout-yolov8n_layout_general6` | 51 | 5 | Text:33, Title:9, Equation:6, Figure:2, Table:1 |
| `unstructured-yolox` | 30 | 6 | Text:13, Section-header:9, Page-footer:3, Page-header:2, Table:2 |
| `rapidlayout-yolov8n_layout_paper` | 27 | 9 | Text:7, Title:6, Equation:6, Header:3, Table:1 |
| `rapidlayout-yolov8n_layout_publaynet` | 1 | 1 | Figure:1 |
| `rapidlayout-pp_layout_cdla` | 4 | 3 | header:2, figure:1, footer:1 |
| `rapidlayout-pp_layout_publaynet` | 2 | 2 | figure:1, title:1 |
| `rapidlayout-pp_layout_table` | 0 | 0 |  |
| `table-transformer-detection` | 0 | 0 |  |