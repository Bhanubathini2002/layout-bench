# Layout model benchmark — qyzhpvcjqkxc.pdf

Canonical input: `layout_bench/page.png` (1917x2480). 20 models tested. Each folder has `overlay.png` + `detections.json`.

| Model | #Regions | #Classes | Notes |
|---|--:|--:|---|
| `rapidlayout-pp_doc_layoutv3` | 14 | 2 | text:13, header_image:1 |
| `rapidlayout-pp_doc_layoutv2` | 11 | 3 | text:9, header_image:1, header:1 |
| `rapidlayout-doclayout_d4la` | 11 | 8 | ParaText:4, LetterHead:1, Figure:1, DocTitle:1, Date:1 |
| `rapidlayout-doclayout_docstructbench` | 9 | 2 | plain text:8, abandon:1 |
| `rapidlayout-doclayout_docsynth` | 9 | 2 | Text:8, Picture:1 |
| `docling-heron-101` | 26 | 4 | Text:20, Key-Value Region:3, Section-header:2, Picture:1 |
| `docling-heron` | 26 | 4 | text:21, key_value_region:3, picture:1, section_header:1 |
| `docling-egret-xlarge` | 23 | 4 | Text:19, Key-Value Region:2, Picture:1, Section-header:1 |
| `docling-egret-medium` | 15 | 3 | Text:12, Section-header:2, Picture:1 |
| `aryn-deformable-detr-DocLayNet` | 9 | 3 | Text:6, Section-header:2, Picture:1 |
| `docling-egret-large` | 6 | 3 | Text:4, Picture:1, Section-header:1 |
| `rapidlayout-yolov8n_layout_report` | 13 | 2 | Text:12, Figure:1 |
| `rapidlayout-yolov8n_layout_general6` | 11 | 3 | Text:8, Title:2, Figure:1 |
| `unstructured-yolox` | 10 | 2 | Text:8, Picture:2 |
| `rapidlayout-yolov8n_layout_paper` | 9 | 3 | Text:7, Figure:1, Title:1 |
| `rapidlayout-yolov8n_layout_publaynet` | 5 | 1 | Text:5 |
| `rapidlayout-pp_layout_cdla` | 10 | 2 | text:8, header:2 |
| `rapidlayout-pp_layout_publaynet` | 7 | 1 | text:7 |
| `rapidlayout-pp_layout_table` | 0 | 0 |  |
| `table-transformer-detection` | 0 | 0 |  |