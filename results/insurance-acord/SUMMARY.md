# Layout model benchmark — insurance-acord.pdf

Canonical input: one rendered page (1917x2480). 20 models tested. Each folder holds `overlay.png` + `detections.json`.

| Model | #Regions | #Classes | Top classes |
|---|--:|--:|---|
| `rapidlayout-pp_doc_layoutv2` | 9 | 5 | table:3, footer:2, header:2, header_image:1, vision_footnote:1 |
| `rapidlayout-pp_doc_layoutv3` | 9 | 5 | table:3, footer:2, header:2, header_image:1, vision_footnote:1 |
| `rapidlayout-doclayout_d4la` | 10 | 5 | Table:3, TableName:3, PageFooter:2, OtherText:1, Figure:1 |
| `rapidlayout-doclayout_docsynth` | 8 | 4 | Section-header:5, Page-footer:1, Picture:1, Title:1 |
| `rapidlayout-doclayout_docstructbench` | 5 | 2 | abandon:3, table:2 |
| `docling-heron-101` | 43 | 7 | text:26, section_header:7, form:4, page_footer:3, picture:1 |
| `docling-heron` | 43 | 7 | text:25, section_header:6, form:4, table:3, page_footer:3 |
| `docling-egret-medium` | 42 | 7 | text:25, section_header:6, form:5, page_footer:3, table:1 |
| `docling-egret-large` | 36 | 7 | text:21, section_header:6, page_footer:3, table:2, form:2 |
| `docling-egret-xlarge` | 36 | 8 | text:17, section_header:6, form:4, page_footer:3, table:2 |
| `aryn-deformable-detr-DocLayNet` | 0 | 0 |  |
| `unstructured-yolox` | 13 | 7 | Table:3, Text:3, Section-header:3, Page-header:1, Caption:1 |
| `rapidlayout-yolov8n_layout_report` | 10 | 5 | Table:3, Footer:2, Text:2, Title:2, Figure:1 |
| `rapidlayout-yolov8n_layout_paper` | 7 | 3 | Reference:5, Title:1, Table:1 |
| `rapidlayout-yolov8n_layout_general6` | 4 | 3 | Title:2, Table:1, Text:1 |
| `rapidlayout-yolov8n_layout_publaynet` | 1 | 1 | Table:1 |
| `rapidlayout-pp_layout_cdla` | 8 | 6 | table:2, header:2, table_caption:1, reference:1, figure:1 |
| `rapidlayout-pp_layout_publaynet` | 5 | 3 | figure:2, text:2, table:1 |
| `rapidlayout-pp_layout_table` | 1 | 1 | table:1 |
| `table-transformer-detection` | 2 | 1 | table:2 |