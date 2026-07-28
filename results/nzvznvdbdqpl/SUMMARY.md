# Layout model benchmark — nzvznvdbdqpl.pdf

Canonical input: `layout_bench/page.png` (1754x2480). 20 models tested. Each folder has `overlay.png` + `detections.json`.

| Model | #Regions | #Classes | Notes |
|---|--:|--:|---|
| `rapidlayout-pp_doc_layoutv3` | 18 | 9 | text:5, paragraph_title:4, image:2, footnote:2, header:1 |
| `rapidlayout-pp_doc_layoutv2` | 17 | 8 | text:6, paragraph_title:4, image:2, header:1, number:1 |
| `rapidlayout-doclayout_d4la` | 18 | 9 | ParaText:6, Figure:2, ParaTitle:2, Author:2, DocTitle:2 |
| `rapidlayout-doclayout_docstructbench` | 17 | 4 | plain text:9, abandon:3, title:3, figure:2 |
| `rapidlayout-doclayout_docsynth` | 17 | 5 | Text:9, Section-header:3, Picture:2, Page-footer:2, Page-header:1 |
| `docling-egret-large` | 23 | 5 | Text:11, Page-footer:5, Section-header:4, Picture:2, Page-header:1 |
| `docling-egret-medium` | 21 | 5 | Text:8, Page-footer:6, Section-header:4, Picture:2, Page-header:1 |
| `docling-heron` | 21 | 5 | text:8, page_footer:6, section_header:4, picture:2, page_header:1 |
| `docling-egret-xlarge` | 20 | 5 | Text:8, Page-footer:5, Section-header:4, Picture:2, Page-header:1 |
| `docling-heron-101` | 20 | 5 | Text:8, Page-footer:5, Section-header:4, Picture:2, Page-header:1 |
| `aryn-deformable-detr-DocLayNet` | 14 | 5 | Text:6, Picture:3, Section-header:3, Page-header:1, Page-footer:1 |
| `rapidlayout-yolov8n_layout_report` | 20 | 5 | Text:9, Title:6, Figure:2, Footer:2, Header:1 |
| `rapidlayout-yolov8n_layout_paper` | 18 | 6 | Text:8, Title:4, Figure:2, Header:2, Reference:1 |
| `unstructured-yolox` | 18 | 5 | Text:9, Section-header:4, Picture:2, Footnote:2, Page-header:1 |
| `rapidlayout-yolov8n_layout_general6` | 14 | 3 | Text:7, Title:5, Figure:2 |
| `rapidlayout-yolov8n_layout_publaynet` | 9 | 3 | Text:6, Title:2, Figure:1 |
| `rapidlayout-pp_layout_cdla` | 20 | 7 | text:8, title:4, header:2, figure:2, footer:2 |
| `rapidlayout-pp_layout_publaynet` | 14 | 2 | text:9, title:5 |
| `rapidlayout-pp_layout_table` | 0 | 0 |  |
| `table-transformer-detection` | 0 | 0 |  |