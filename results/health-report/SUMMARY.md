# Layout model benchmark — health-report.pdf

Canonical input: one rendered page (1860x2480). 20 models tested. Each folder holds `overlay.png` + `detections.json`.

| Model | #Regions | #Classes | Top classes |
|---|--:|--:|---|
| `rapidlayout-pp_doc_layoutv2` | 10 | 5 | figure_title:3, chart:2, footer:2, vision_footnote:2, number:1 |
| `rapidlayout-pp_doc_layoutv3` | 10 | 5 | figure_title:3, chart:2, footer:2, vision_footnote:2, number:1 |
| `rapidlayout-doclayout_d4la` | 15 | 6 | OtherText:6, ParaText:4, Figure:2, RegionKV:1, PageNumber:1 |
| `rapidlayout-doclayout_docstructbench` | 10 | 4 | abandon:3, plain text:3, figure:2, figure_caption:2 |
| `rapidlayout-doclayout_docsynth` | 7 | 4 | Picture:3, Text:2, Page-header:1, Caption:1 |
| `docling-heron-101` | 29 | 6 | text:17, key_value_region:5, picture:2, caption:2, page_footer:2 |
| `docling-heron` | 26 | 6 | text:16, key_value_region:3, picture:2, caption:2, page_footer:2 |
| `docling-egret-xlarge` | 21 | 6 | text:12, page_footer:3, picture:2, caption:2, page_header:1 |
| `docling-egret-medium` | 19 | 6 | text:9, picture:4, caption:2, key_value_region:2, page_header:1 |
| `docling-egret-large` | 18 | 6 | text:10, picture:2, caption:2, key_value_region:2, page_footer:1 |
| `aryn-deformable-detr-DocLayNet` | 8 | 5 | Picture:2, Text:2, Caption:2, Page-footer:1, Page-header:1 |
| `unstructured-yolox` | 14 | 5 | Text:8, Picture:2, Section-header:2, Page-header:1, List-item:1 |
| `rapidlayout-yolov8n_layout_report` | 11 | 5 | Text:5, Figure:2, Figure caption:2, Footer:1, Title:1 |
| `rapidlayout-yolov8n_layout_paper` | 8 | 5 | Figure:2, Figure caption:2, Header:2, Footer:1, Text:1 |
| `rapidlayout-yolov8n_layout_general6` | 7 | 3 | Text:4, Figure:2, Caption:1 |
| `rapidlayout-yolov8n_layout_publaynet` | 3 | 2 | Text:2, Figure:1 |
| `rapidlayout-pp_layout_cdla` | 6 | 4 | figure:2, text:2, header:1, figure_caption:1 |
| `rapidlayout-pp_layout_publaynet` | 6 | 2 | text:4, figure:2 |
| `rapidlayout-pp_layout_table` | 0 | 0 |  |
| `table-transformer-detection` | 0 | 0 |  |