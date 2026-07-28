# Layout model benchmark — ktfcrhncpqkr.pdf

Canonical input: `layout_bench/page.png` (1754x2480). 20 models tested. Each folder has `overlay.png` + `detections.json`.

| Model | #Regions | #Classes | Notes |
|---|--:|--:|---|
| `rapidlayout-pp_doc_layoutv2` | 31 | 6 | text:21, paragraph_title:4, doc_title:2, header:2, image:1 |
| `rapidlayout-pp_doc_layoutv3` | 31 | 6 | text:21, paragraph_title:4, doc_title:2, header:2, image:1 |
| `rapidlayout-doclayout_d4la` | 30 | 7 | ParaText:18, ParaTitle:4, OtherText:3, DocTitle:2, Date:1 |
| `rapidlayout-doclayout_docsynth` | 30 | 3 | Text:20, Section-header:7, Page-header:3 |
| `rapidlayout-doclayout_docstructbench` | 29 | 3 | plain text:20, title:6, abandon:3 |
| `docling-egret-medium` | 35 | 4 | Text:24, Section-header:6, Page-header:3, Picture:2 |
| `docling-heron` | 34 | 4 | text:22, section_header:7, page_header:3, picture:2 |
| `docling-egret-large` | 33 | 4 | Text:22, Section-header:5, Page-header:3, Picture:3 |
| `docling-heron-101` | 33 | 4 | Text:22, Section-header:6, Page-header:3, Picture:2 |
| `docling-egret-xlarge` | 31 | 4 | Text:21, Section-header:6, Page-header:3, Picture:1 |
| `aryn-deformable-detr-DocLayNet` | 27 | 3 | Text:19, Section-header:5, Page-header:3 |
| `rapidlayout-yolov8n_layout_paper` | 34 | 3 | Text:25, Title:6, Header:3 |
| `rapidlayout-yolov8n_layout_report` | 32 | 3 | Text:24, Title:5, Header:3 |
| `unstructured-yolox` | 30 | 3 | Text:21, Section-header:6, Page-header:3 |
| `rapidlayout-yolov8n_layout_general6` | 27 | 2 | Text:21, Title:6 |
| `rapidlayout-yolov8n_layout_publaynet` | 23 | 2 | Text:18, Title:5 |
| `rapidlayout-pp_layout_publaynet` | 26 | 2 | text:22, title:4 |
| `rapidlayout-pp_layout_cdla` | 25 | 3 | text:14, header:6, title:5 |
| `rapidlayout-pp_layout_table` | 0 | 0 |  |
| `table-transformer-detection` | 0 | 0 |  |