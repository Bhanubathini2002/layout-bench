# Layout model benchmark — trgqjpwnmtgv.pdf

Canonical input: `layout_bench/page.png` (1754x2480). 20 models tested. Each folder has `overlay.png` + `detections.json`.

| Model | #Regions | #Classes | Notes |
|---|--:|--:|---|
| `rapidlayout-pp_doc_layoutv2` | 79 | 6 | text:44, image:18, paragraph_title:14, chart:1, figure_title:1 |
| `rapidlayout-pp_doc_layoutv3` | 67 | 4 | text:33, image:18, paragraph_title:15, chart:1 |
| `rapidlayout-doclayout_docsynth` | 39 | 4 | Text:15, Section-header:14, List-item:6, Picture:4 |
| `rapidlayout-doclayout_d4la` | 38 | 12 | OtherText:10, ListText:7, RegionTitle:6, ParaText:3, DocTitle:3 |
| `rapidlayout-doclayout_docstructbench` | 30 | 4 | plain text:16, title:12, figure:1, abandon:1 |
| `docling-heron-101` | 116 | 6 | Picture:35, Text:29, List-item:25, Section-header:22, Key-Value Region:3 |
| `docling-egret-medium` | 106 | 5 | Picture:35, Text:34, Section-header:29, List-item:7, Key-Value Region:1 |
| `docling-egret-large` | 102 | 5 | Text:45, Section-header:27, Picture:20, List-item:9, Table:1 |
| `docling-heron` | 84 | 7 | section_header:27, text:27, list_item:14, picture:12, checkbox_unselected:2 |
| `docling-egret-xlarge` | 72 | 5 | Section-header:27, Text:20, List-item:17, Picture:7, Key-Value Region:1 |
| `aryn-deformable-detr-DocLayNet` | 11 | 2 | Section-header:10, List-item:1 |
| `unstructured-yolox` | 54 | 5 | Text:23, Section-header:21, List-item:7, Picture:2, Table:1 |
| `rapidlayout-yolov8n_layout_report` | 26 | 6 | Title:10, Text:9, Table:3, Figure:2, Figure caption:1 |
| `rapidlayout-yolov8n_layout_general6` | 20 | 4 | Title:12, Text:5, Figure:2, Table:1 |
| `rapidlayout-yolov8n_layout_paper` | 20 | 3 | Title:12, Text:6, Figure:2 |
| `rapidlayout-yolov8n_layout_publaynet` | 1 | 1 | Figure:1 |
| `rapidlayout-pp_layout_cdla` | 6 | 5 | text:2, title:1, table:1, table_caption:1, figure:1 |
| `rapidlayout-pp_layout_publaynet` | 4 | 2 | text:3, figure:1 |
| `rapidlayout-pp_layout_table` | 1 | 1 | table:1 |
| `table-transformer-detection` | 0 | 0 |  |