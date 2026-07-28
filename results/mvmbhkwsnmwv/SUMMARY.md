# Layout model benchmark — mvmbhkwsnmwv.pdf

Canonical input: `layout_bench/page.png` (1754x2480). 20 models tested. Each folder has `overlay.png` + `detections.json`.

| Model | #Regions | #Classes | Notes |
|---|--:|--:|---|
| `rapidlayout-pp_doc_layoutv2` | 32 | 5 | text:17, image:8, paragraph_title:5, header_image:1, header:1 |
| `rapidlayout-pp_doc_layoutv3` | 25 | 3 | text:17, paragraph_title:6, image:2 |
| `rapidlayout-doclayout_docstructbench` | 23 | 3 | plain text:16, title:6, abandon:1 |
| `rapidlayout-doclayout_docsynth` | 22 | 5 | List-item:11, Section-header:5, Text:4, Picture:1, Title:1 |
| `rapidlayout-doclayout_d4la` | 12 | 6 | RegionTitle:5, Reference:2, RegionList:2, Figure:1, Author:1 |
| `docling-heron-101` | 38 | 5 | List-item:15, Text:11, Section-header:6, Picture:4, Key-Value Region:2 |
| `docling-heron` | 35 | 4 | list_item:14, text:9, picture:6, section_header:6 |
| `docling-egret-medium` | 34 | 4 | List-item:15, Text:8, Section-header:6, Picture:5 |
| `docling-egret-large` | 32 | 5 | List-item:11, Picture:9, Section-header:6, Text:5, Document Index:1 |
| `docling-egret-xlarge` | 30 | 4 | List-item:17, Section-header:6, Text:6, Picture:1 |
| `aryn-deformable-detr-DocLayNet` | 15 | 3 | List-item:10, Section-header:4, Picture:1 |
| `rapidlayout-yolov8n_layout_general6` | 25 | 3 | Text:18, Title:6, Figure:1 |
| `unstructured-yolox` | 24 | 4 | List-item:11, Section-header:10, Text:2, Picture:1 |
| `rapidlayout-yolov8n_layout_report` | 16 | 5 | Text:10, Table:2, Title:2, Figure:1, Table caption:1 |
| `rapidlayout-yolov8n_layout_paper` | 11 | 4 | Title:5, Reference:4, Figure:1, Text:1 |
| `rapidlayout-yolov8n_layout_publaynet` | 3 | 2 | Text:2, Figure:1 |
| `rapidlayout-pp_layout_cdla` | 17 | 4 | text:7, title:5, reference:4, figure:1 |
| `rapidlayout-pp_layout_publaynet` | 7 | 2 | title:4, list:3 |
| `rapidlayout-pp_layout_table` | 0 | 0 |  |
| `table-transformer-detection` | 0 | 0 |  |