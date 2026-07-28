# Layout model benchmark — qtsmnthhhrpd.pdf

Canonical input: `layout_bench/page.png` (1754x2480). 20 models tested. Each folder has `overlay.png` + `detections.json`.

| Model | #Regions | #Classes | Notes |
|---|--:|--:|---|
| `rapidlayout-pp_doc_layoutv3` | 15 | 5 | text:11, table:1, header_image:1, paragraph_title:1, number:1 |
| `rapidlayout-pp_doc_layoutv2` | 14 | 4 | text:11, table:1, number:1, paragraph_title:1 |
| `rapidlayout-doclayout_docsynth` | 15 | 6 | List-item:6, Text:5, Section-header:1, Page-footer:1, Picture:1 |
| `rapidlayout-doclayout_d4la` | 12 | 4 | ListText:5, ParaText:4, Table:2, TableName:1 |
| `rapidlayout-doclayout_docstructbench` | 10 | 4 | plain text:6, title:2, table:1, abandon:1 |
| `docling-heron` | 35 | 7 | text:21, list_item:5, section_header:3, key_value_region:2, form:2 |
| `docling-egret-large` | 33 | 8 | Text:21, List-item:5, Section-header:2, Picture:1, Page-footer:1 |
| `docling-heron-101` | 32 | 6 | Text:21, List-item:5, Section-header:2, Form:2, Picture:1 |
| `docling-egret-medium` | 28 | 7 | Text:17, List-item:5, Section-header:2, Picture:1, Page-footer:1 |
| `docling-egret-xlarge` | 18 | 6 | Text:8, List-item:5, Section-header:2, Picture:1, Table:1 |
| `aryn-deformable-detr-DocLayNet` | 7 | 3 | Text:4, List-item:2, Page-footer:1 |
| `unstructured-yolox` | 14 | 5 | Text:6, List-item:5, Picture:1, Table:1, Section-header:1 |
| `rapidlayout-yolov8n_layout_general6` | 8 | 3 | Text:6, Table:1, Title:1 |
| `rapidlayout-yolov8n_layout_report` | 8 | 4 | Text:5, Figure:1, Table:1, Footer:1 |
| `rapidlayout-yolov8n_layout_paper` | 3 | 3 | Table:1, Title:1, Text:1 |
| `rapidlayout-yolov8n_layout_publaynet` | 2 | 1 | Text:2 |
| `rapidlayout-pp_layout_cdla` | 11 | 5 | text:4, reference:4, header:1, footer:1, figure:1 |
| `rapidlayout-pp_layout_publaynet` | 8 | 2 | text:6, list:2 |
| `rapidlayout-pp_layout_table` | 1 | 1 | table:1 |
| `table-transformer-detection` | 1 | 1 | table:1 |