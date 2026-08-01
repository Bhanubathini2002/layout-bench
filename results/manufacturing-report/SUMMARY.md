# Layout model benchmark — manufacturing-report.pdf

Canonical input: one rendered page (1917x2480). 20 models tested. Each folder holds `overlay.png` + `detections.json`.

| Model | #Regions | #Classes | Top classes |
|---|--:|--:|---|
| `rapidlayout-pp_doc_layoutv2` | 8 | 5 | image:2, figure_title:2, vision_footnote:2, number:1, header:1 |
| `rapidlayout-pp_doc_layoutv3` | 8 | 6 | image:2, figure_title:2, vision_footnote:1, header:1, number:1 |
| `rapidlayout-doclayout_d4la` | 8 | 3 | ParaText:4, Figure:2, PageNumber:2 |
| `rapidlayout-doclayout_docstructbench` | 8 | 4 | figure_caption:3, figure:2, plain text:2, abandon:1 |
| `rapidlayout-doclayout_docsynth` | 8 | 4 | Text:4, Picture:2, Page-footer:1, Caption:1 |
| `docling-heron` | 15 | 5 | text:7, page_header:3, picture:2, caption:2, page_footer:1 |
| `docling-egret-large` | 14 | 5 | text:6, page_header:3, picture:2, caption:2, page_footer:1 |
| `docling-egret-xlarge` | 11 | 6 | page_header:3, picture:2, caption:2, text:2, page_footer:1 |
| `docling-heron-101` | 11 | 5 | text:4, picture:2, caption:2, page_header:2, page_footer:1 |
| `docling-egret-medium` | 10 | 5 | page_header:3, picture:2, caption:2, text:2, page_footer:1 |
| `aryn-deformable-detr-DocLayNet` | 6 | 4 | Picture:2, Text:2, Page-footer:1, Page-header:1 |
| `unstructured-yolox` | 8 | 6 | Picture:2, Text:2, Page-footer:1, Section-header:1, Caption:1 |
| `rapidlayout-yolov8n_layout_general6` | 6 | 3 | Caption:3, Figure:2, Text:1 |
| `rapidlayout-yolov8n_layout_report` | 6 | 3 | Text:3, Figure:2, Footer:1 |
| `rapidlayout-yolov8n_layout_paper` | 3 | 2 | Figure:2, Reference:1 |
| `rapidlayout-yolov8n_layout_publaynet` | 3 | 2 | Text:2, Title:1 |
| `rapidlayout-pp_layout_cdla` | 9 | 5 | figure_caption:3, figure:2, reference:2, header:1, footer:1 |
| `rapidlayout-pp_layout_publaynet` | 6 | 2 | text:4, figure:2 |
| `rapidlayout-pp_layout_table` | 0 | 0 |  |
| `table-transformer-detection` | 0 | 0 |  |