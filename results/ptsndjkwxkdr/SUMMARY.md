# Layout model benchmark — ptsndjkwxkdr.pdf

Canonical input: `layout_bench/page.png` (1917x2480). 20 models tested. Each folder has `overlay.png` + `detections.json`.

| Model | #Regions | #Classes | Notes |
|---|--:|--:|---|
| `rapidlayout-pp_doc_layoutv3` | 24 | 7 | text:12, paragraph_title:6, figure_title:2, image:1, abstract:1 |
| `rapidlayout-pp_doc_layoutv2` | 23 | 7 | text:12, paragraph_title:6, abstract:1, image:1, figure_title:1 |
| `rapidlayout-doclayout_docsynth` | 25 | 4 | Text:17, Section-header:6, Picture:1, Title:1 |
| `rapidlayout-doclayout_docstructbench` | 23 | 5 | plain text:13, title:7, figure:1, abandon:1, figure_caption:1 |
| `rapidlayout-doclayout_d4la` | 21 | 8 | ParaText:8, ParaTitle:6, RegionList:2, Figure:1, Footer:1 |
| `docling-egret-xlarge` | 33 | 7 | Text:17, Section-header:10, Page-footer:2, Picture:1, Caption:1 |
| `docling-heron-101` | 32 | 5 | Text:18, Section-header:10, Footnote:2, Picture:1, Caption:1 |
| `docling-heron` | 29 | 6 | text:15, section_header:9, footnote:2, caption:1, picture:1 |
| `docling-egret-large` | 27 | 5 | Text:17, Section-header:7, Caption:1, Picture:1, Footnote:1 |
| `docling-egret-medium` | 26 | 5 | Text:16, Section-header:7, Picture:1, Caption:1, Footnote:1 |
| `aryn-deformable-detr-DocLayNet` | 24 | 4 | Text:14, Section-header:7, Footnote:2, Picture:1 |
| `rapidlayout-yolov8n_layout_report` | 31 | 4 | Text:22, Title:7, Figure:1, Table:1 |
| `rapidlayout-yolov8n_layout_paper` | 25 | 6 | Text:16, Title:5, Reference:1, Figure:1, Figure caption:1 |
| `rapidlayout-yolov8n_layout_general6` | 24 | 4 | Text:15, Title:7, Figure:1, Caption:1 |
| `unstructured-yolox` | 24 | 4 | Text:15, Section-header:7, Picture:1, Caption:1 |
| `rapidlayout-yolov8n_layout_publaynet` | 17 | 3 | Text:11, Title:5, Figure:1 |
| `rapidlayout-pp_layout_cdla` | 22 | 4 | text:14, title:6, reference:1, figure:1 |
| `rapidlayout-pp_layout_publaynet` | 22 | 3 | text:15, title:6, figure:1 |
| `rapidlayout-pp_layout_table` | 0 | 0 |  |
| `table-transformer-detection` | 1 | 1 | table:1 |