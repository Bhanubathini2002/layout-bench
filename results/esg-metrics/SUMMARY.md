# Layout model benchmark — esg-metrics.pdf

Canonical input: one rendered page (2480x1917). 20 models tested. Each folder holds `overlay.png` + `detections.json`.

| Model | #Regions | #Classes | Top classes |
|---|--:|--:|---|
| `rapidlayout-pp_doc_layoutv2` | 20 | 8 | vision_footnote:9, text:3, chart:2, footer:2, table:1 |
| `rapidlayout-pp_doc_layoutv3` | 20 | 9 | vision_footnote:9, chart:2, footer:2, figure_title:2, table:1 |
| `rapidlayout-doclayout_docstructbench` | 15 | 8 | table_footnote:4, abandon:3, figure:2, figure_caption:2, table:1 |
| `rapidlayout-doclayout_docsynth` | 15 | 5 | Text:8, Section-header:3, Picture:2, Table:1, Page-header:1 |
| `rapidlayout-doclayout_d4la` | 11 | 7 | OtherText:4, ParaText:2, RegionList:1, Table:1, DocTitle:1 |
| `docling-heron-101` | 34 | 9 | text:12, footnote:7, section_header:5, picture:2, page_footer:2 |
| `docling-heron` | 31 | 8 | text:12, footnote:5, section_header:4, list_item:4, picture:2 |
| `docling-egret-xlarge` | 28 | 7 | text:9, list_item:7, section_header:5, page_footer:3, picture:2 |
| `docling-egret-medium` | 24 | 6 | text:11, section_header:5, picture:3, caption:3, table:1 |
| `docling-egret-large` | 23 | 7 | text:11, section_header:5, picture:2, caption:2, table:1 |
| `aryn-deformable-detr-DocLayNet` | 13 | 4 | Text:9, Picture:2, Table:1, Section-header:1 |
| `rapidlayout-yolov8n_layout_report` | 15 | 7 | Text:5, Footer:2, Figure:2, Title:2, Figure caption:2 |
| `rapidlayout-yolov8n_layout_general6` | 14 | 4 | Text:8, Title:3, Figure:2, Table:1 |
| `unstructured-yolox` | 10 | 4 | Text:5, Picture:2, Section-header:2, Table:1 |
| `rapidlayout-yolov8n_layout_paper` | 8 | 6 | Figure:2, Title:2, Table:1, Reference:1, Header:1 |
| `rapidlayout-yolov8n_layout_publaynet` | 4 | 3 | Text:2, Figure:1, Title:1 |
| `rapidlayout-pp_layout_publaynet` | 8 | 3 | text:5, title:2, table:1 |
| `rapidlayout-pp_layout_cdla` | 5 | 3 | table_caption:2, title:2, figure:1 |
| `rapidlayout-pp_layout_table` | 1 | 1 | table:1 |
| `table-transformer-detection` | 1 | 1 | table:1 |