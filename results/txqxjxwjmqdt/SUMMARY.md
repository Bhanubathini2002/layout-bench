# Layout model benchmark — txqxjxwjmqdt.pdf

Canonical input: `layout_bench/page.png` (2480x1395). 20 models tested. Each folder has `overlay.png` + `detections.json`.

| Model | #Regions | #Classes | Notes |
|---|--:|--:|---|
| `rapidlayout-pp_doc_layoutv2` | 8 | 3 | text:4, image:3, doc_title:1 |
| `rapidlayout-pp_doc_layoutv3` | 6 | 3 | text:4, doc_title:1, image:1 |
| `rapidlayout-doclayout_docstructbench` | 7 | 3 | plain text:4, abandon:2, title:1 |
| `rapidlayout-doclayout_d4la` | 6 | 4 | Figure:3, FigureName:1, OtherText:1, DocTitle:1 |
| `rapidlayout-doclayout_docsynth` | 6 | 3 | Text:4, Picture:1, Title:1 |
| `docling-heron-101` | 9 | 4 | Text:5, Picture:2, Section-header:1, Title:1 |
| `docling-egret-large` | 8 | 3 | Text:4, Picture:3, Section-header:1 |
| `docling-egret-medium` | 8 | 3 | Text:4, Picture:3, Section-header:1 |
| `docling-egret-xlarge` | 8 | 3 | Text:4, Picture:3, Section-header:1 |
| `docling-heron` | 8 | 3 | text:4, picture:3, section_header:1 |
| `aryn-deformable-detr-DocLayNet` | 0 | 0 |  |
| `unstructured-yolox` | 7 | 3 | Text:4, Picture:2, Section-header:1 |
| `rapidlayout-yolov8n_layout_report` | 5 | 3 | Text:3, Figure:1, Title:1 |
| `rapidlayout-yolov8n_layout_general6` | 4 | 1 | Text:4 |
| `rapidlayout-yolov8n_layout_paper` | 3 | 3 | Title:1, Figure:1, Text:1 |
| `rapidlayout-yolov8n_layout_publaynet` | 1 | 1 | Figure:1 |
| `rapidlayout-pp_layout_publaynet` | 2 | 2 | figure:1, text:1 |
| `rapidlayout-pp_layout_cdla` | 1 | 1 | figure:1 |
| `rapidlayout-pp_layout_table` | 0 | 0 |  |
| `table-transformer-detection` | 0 | 0 |  |