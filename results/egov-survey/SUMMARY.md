# Layout model benchmark — egov-survey.pdf

Canonical input: one rendered page (1917x2480). 20 models tested. Each folder holds `overlay.png` + `detections.json`.

| Model | #Regions | #Classes | Top classes |
|---|--:|--:|---|
| `rapidlayout-pp_doc_layoutv2` | 9 | 7 | text:3, chart:1, figure_title:1, header:1, aside_text:1 |
| `rapidlayout-pp_doc_layoutv3` | 9 | 7 | text:3, chart:1, figure_title:1, aside_text:1, header:1 |
| `rapidlayout-doclayout_docstructbench` | 10 | 5 | abandon:4, plain text:3, figure:1, table_footnote:1, figure_caption:1 |
| `rapidlayout-doclayout_docsynth` | 7 | 4 | Text:3, Page-header:2, Picture:1, Page-footer:1 |
| `rapidlayout-doclayout_d4la` | 6 | 4 | ParaText:3, Figure:1, PageNumber:1, ParaTitle:1 |
| `docling-egret-xlarge` | 12 | 6 | text:6, page_header:2, picture:1, caption:1, page_footer:1 |
| `docling-egret-large` | 11 | 6 | text:5, page_header:2, picture:1, caption:1, page_footer:1 |
| `docling-egret-medium` | 11 | 6 | text:5, page_header:2, caption:1, picture:1, page_footer:1 |
| `docling-heron-101` | 11 | 6 | text:5, page_header:2, picture:1, caption:1, page_footer:1 |
| `docling-heron` | 11 | 6 | text:5, page_header:2, picture:1, caption:1, page_footer:1 |
| `aryn-deformable-detr-DocLayNet` | 8 | 6 | Text:3, Page-footer:1, Page-header:1, Picture:1, Caption:1 |
| `rapidlayout-yolov8n_layout_report` | 9 | 4 | Text:5, Header:2, Figure:1, Footer:1 |
| `unstructured-yolox` | 9 | 4 | Text:4, Page-header:3, Picture:1, Caption:1 |
| `rapidlayout-yolov8n_layout_paper` | 8 | 5 | Text:3, Reference:2, Header:1, Figure:1, Footer:1 |
| `rapidlayout-yolov8n_layout_general6` | 5 | 2 | Text:4, Figure:1 |
| `rapidlayout-yolov8n_layout_publaynet` | 5 | 2 | Text:4, Table:1 |
| `rapidlayout-pp_layout_cdla` | 8 | 5 | text:4, figure:1, reference:1, footer:1, header:1 |
| `rapidlayout-pp_layout_publaynet` | 6 | 2 | text:5, table:1 |
| `rapidlayout-pp_layout_table` | 0 | 0 |  |
| `table-transformer-detection` | 0 | 0 |  |