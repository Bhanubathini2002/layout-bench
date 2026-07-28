# Layout model benchmark — srfwgqcwqncf.pdf

Canonical input: `layout_bench/page.png` (2480x1395). 20 models tested. Each folder has `overlay.png` + `detections.json`.

| Model | #Regions | #Classes | Notes |
|---|--:|--:|---|
| `rapidlayout-pp_doc_layoutv3` | 4 | 3 | text:2, header_image:1, doc_title:1 |
| `rapidlayout-pp_doc_layoutv2` | 3 | 3 | header_image:1, text:1, paragraph_title:1 |
| `rapidlayout-doclayout_d4la` | 7 | 5 | OtherText:3, Author:1, DocTitle:1, Figure:1, PageHeader:1 |
| `rapidlayout-doclayout_docsynth` | 6 | 4 | Text:3, Picture:1, Section-header:1, Title:1 |
| `rapidlayout-doclayout_docstructbench` | 4 | 3 | plain text:2, title:1, abandon:1 |
| `docling-egret-large` | 10 | 3 | Text:7, Section-header:2, Picture:1 |
| `docling-heron-101` | 10 | 3 | Text:6, Section-header:3, Picture:1 |
| `docling-egret-xlarge` | 9 | 3 | Text:5, Section-header:3, Picture:1 |
| `docling-egret-medium` | 7 | 3 | Text:4, Section-header:2, Picture:1 |
| `docling-heron` | 6 | 3 | section_header:3, text:2, picture:1 |
| `aryn-deformable-detr-DocLayNet` | 0 | 0 |  |
| `rapidlayout-yolov8n_layout_general6` | 6 | 3 | Text:4, Figure:1, Title:1 |
| `rapidlayout-yolov8n_layout_report` | 6 | 3 | Title:3, Text:2, Figure:1 |
| `unstructured-yolox` | 4 | 3 | Text:2, Section-header:1, Picture:1 |
| `rapidlayout-yolov8n_layout_paper` | 1 | 1 | Title:1 |
| `rapidlayout-yolov8n_layout_publaynet` | 1 | 1 | Figure:1 |
| `rapidlayout-pp_layout_cdla` | 6 | 4 | title:3, text:1, figure:1, figure_caption:1 |
| `rapidlayout-pp_layout_publaynet` | 1 | 1 | figure:1 |
| `rapidlayout-pp_layout_table` | 0 | 0 |  |
| `table-transformer-detection` | 0 | 0 |  |