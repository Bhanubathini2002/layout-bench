# Layout model benchmark — jkcyqtjgpqgq.pdf

Canonical input: `layout_bench/page.png` (1754x2480). 20 models tested. Each folder has `overlay.png` + `detections.json`.

| Model | #Regions | #Classes | Notes |
|---|--:|--:|---|
| `rapidlayout-pp_doc_layoutv2` | 18 | 4 | text:15, header:1, image:1, header_image:1 |
| `rapidlayout-pp_doc_layoutv3` | 14 | 3 | text:10, header:2, image:2 |
| `rapidlayout-doclayout_docsynth` | 17 | 5 | Text:10, List-item:3, Picture:2, Title:1, Section-header:1 |
| `rapidlayout-doclayout_d4la` | 15 | 8 | Figure:4, LetterDear:3, ListText:3, RegionKV:1, FigureName:1 |
| `rapidlayout-doclayout_docstructbench` | 12 | 3 | plain text:9, abandon:2, title:1 |
| `docling-egret-large` | 33 | 5 | Text:20, Page-header:8, Picture:2, Form:2, Key-Value Region:1 |
| `docling-heron-101` | 33 | 5 | Text:21, Page-header:8, Picture:2, Key-Value Region:1, Form:1 |
| `docling-heron` | 32 | 4 | text:20, page_header:8, picture:3, key_value_region:1 |
| `docling-egret-xlarge` | 19 | 6 | Text:7, List-item:4, Picture:3, Page-header:3, Key-Value Region:1 |
| `docling-egret-medium` | 15 | 3 | Text:12, Picture:2, Section-header:1 |
| `aryn-deformable-detr-DocLayNet` | 3 | 2 | Text:2, Picture:1 |
| `rapidlayout-yolov8n_layout_report` | 14 | 3 | Text:10, Figure:2, Title:2 |
| `unstructured-yolox` | 11 | 3 | Text:9, Picture:1, Section-header:1 |
| `rapidlayout-yolov8n_layout_general6` | 6 | 3 | Text:4, Figure:1, Title:1 |
| `rapidlayout-yolov8n_layout_paper` | 6 | 5 | Text:2, Title:1, Header:1, Figure:1, Figure caption:1 |
| `rapidlayout-yolov8n_layout_publaynet` | 2 | 2 | Figure:1, Text:1 |
| `rapidlayout-pp_layout_publaynet` | 11 | 1 | text:11 |
| `rapidlayout-pp_layout_cdla` | 5 | 3 | header:3, text:1, figure:1 |
| `rapidlayout-pp_layout_table` | 0 | 0 |  |
| `table-transformer-detection` | 1 | 1 | table:1 |