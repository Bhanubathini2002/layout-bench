# Layout model benchmark — njhmmgjpfbvf.pdf

Canonical input: `layout_bench/page.png` (1754x2480). 20 models tested. Each folder has `overlay.png` + `detections.json`.

| Model | #Regions | #Classes | Notes |
|---|--:|--:|---|
| `rapidlayout-pp_doc_layoutv3` | 15 | 7 | header:4, paragraph_title:3, text:2, algorithm:2, table:2 |
| `rapidlayout-pp_doc_layoutv2` | 14 | 6 | paragraph_title:5, header:4, algorithm:2, text:1, number:1 |
| `rapidlayout-doclayout_d4la` | 14 | 6 | OtherText:5, Table:4, RegionKV:2, ParaText:1, Date:1 |
| `rapidlayout-doclayout_docstructbench` | 14 | 4 | plain text:4, title:4, abandon:3, table:3 |
| `rapidlayout-doclayout_docsynth` | 12 | 4 | Text:5, Section-header:5, Table:1, Caption:1 |
| `docling-heron` | 26 | 9 | section_header:6, page_header:6, text:3, code:3, picture:3 |
| `docling-egret-xlarge` | 25 | 7 | Page-header:7, Text:5, Section-header:5, Table:3, Code:2 |
| `docling-heron-101` | 24 | 7 | Section-header:7, Page-header:5, Text:4, Code:4, List-item:2 |
| `docling-egret-large` | 21 | 6 | Section-header:7, Page-header:5, Text:4, Code:3, Page-footer:1 |
| `docling-egret-medium` | 19 | 8 | Section-header:6, Page-header:5, Code:2, List-item:2, Text:1 |
| `aryn-deformable-detr-DocLayNet` | 6 | 3 | Section-header:3, Text:2, Page-footer:1 |
| `rapidlayout-yolov8n_layout_report` | 16 | 4 | Text:8, Title:4, Table:3, Table caption:1 |
| `unstructured-yolox` | 14 | 5 | Text:8, Section-header:2, Table:2, Page-footer:1, Caption:1 |
| `rapidlayout-yolov8n_layout_general6` | 12 | 3 | Text:8, Title:3, Table:1 |
| `rapidlayout-yolov8n_layout_paper` | 10 | 5 | Text:4, Figure:2, Title:2, Figure caption:1, Equation:1 |
| `rapidlayout-yolov8n_layout_publaynet` | 3 | 3 | Text:1, Title:1, Figure:1 |
| `rapidlayout-pp_layout_cdla` | 12 | 2 | text:10, header:2 |
| `rapidlayout-pp_layout_publaynet` | 5 | 2 | text:3, title:2 |
| `rapidlayout-pp_layout_table` | 4 | 1 | table:4 |
| `table-transformer-detection` | 0 | 0 |  |