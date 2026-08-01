# Layout model benchmark — catastrophe-recap.pdf

Canonical input: one rendered page (1917x2480). 20 models tested. Each folder holds `overlay.png` + `detections.json`.

| Model | #Regions | #Classes | Top classes |
|---|--:|--:|---|
| `rapidlayout-pp_doc_layoutv2` | 10 | 8 | text:2, figure_title:2, table:1, chart:1, footer:1 |
| `rapidlayout-pp_doc_layoutv3` | 10 | 8 | text:2, figure_title:2, table:1, chart:1, footer:1 |
| `rapidlayout-doclayout_d4la` | 11 | 8 | ParaText:2, RegionKV:2, OtherText:2, Table:1, Figure:1 |
| `rapidlayout-doclayout_docsynth` | 11 | 6 | Text:3, Picture:2, Page-footer:2, Section-header:2, Table:1 |
| `rapidlayout-doclayout_docstructbench` | 10 | 7 | plain text:2, abandon:2, table_caption:2, table:1, figure:1 |
| `docling-heron-101` | 14 | 7 | text:4, picture:2, page_footer:2, section_header:2, caption:2 |
| `docling-egret-large` | 13 | 7 | text:3, picture:2, page_footer:2, caption:2, section_header:2 |
| `docling-egret-xlarge` | 13 | 6 | text:5, picture:2, page_footer:2, caption:2, table:1 |
| `docling-egret-medium` | 12 | 7 | text:3, picture:2, page_footer:2, caption:2, table:1 |
| `docling-heron` | 12 | 6 | text:4, picture:2, page_footer:2, caption:2, table:1 |
| `aryn-deformable-detr-DocLayNet` | 8 | 6 | Text:2, Page-footer:2, Picture:1, Table:1, Caption:1 |
| `rapidlayout-yolov8n_layout_report` | 11 | 6 | Text:4, Figure:2, Footer:2, Table:1, Table caption:1 |
| `unstructured-yolox` | 9 | 4 | Text:4, Section-header:3, Table:1, Picture:1 |
| `rapidlayout-yolov8n_layout_general6` | 7 | 4 | Text:2, Figure:2, Caption:2, Table:1 |
| `rapidlayout-yolov8n_layout_paper` | 7 | 5 | Text:2, Header:2, Table:1, Figure:1, Table caption:1 |
| `rapidlayout-yolov8n_layout_publaynet` | 4 | 3 | Text:2, Title:1, Figure:1 |
| `rapidlayout-pp_layout_cdla` | 11 | 8 | text:3, reference:2, header:1, table:1, table_caption:1 |
| `rapidlayout-pp_layout_publaynet` | 6 | 4 | text:3, table:1, figure:1, title:1 |
| `rapidlayout-pp_layout_table` | 1 | 1 | table:1 |
| `table-transformer-detection` | 1 | 1 | table:1 |