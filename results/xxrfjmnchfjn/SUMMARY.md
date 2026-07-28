# Layout model benchmark — xxrfjmnchfjn.pdf

Canonical input: `layout_bench/page.png` (1754x2480). 20 models tested. Each folder has `overlay.png` + `detections.json`.

| Model | #Regions | #Classes | Notes |
|---|--:|--:|---|
| `rapidlayout-pp_doc_layoutv3` | 11 | 4 | text:7, doc_title:2, image:1, paragraph_title:1 |
| `rapidlayout-pp_doc_layoutv2` | 8 | 3 | text:6, paragraph_title:1, image:1 |
| `rapidlayout-doclayout_docsynth` | 9 | 1 | Text:9 |
| `rapidlayout-doclayout_docstructbench` | 6 | 2 | plain text:5, abandon:1 |
| `rapidlayout-doclayout_d4la` | 4 | 4 | RegionKV:1, Figure:1, OtherText:1, DocTitle:1 |
| `docling-egret-large` | 21 | 5 | Text:14, Section-header:4, Key-Value Region:1, Picture:1, Page-footer:1 |
| `docling-heron` | 20 | 6 | text:12, section_header:4, picture:1, key_value_region:1, page_footer:1 |
| `docling-egret-xlarge` | 19 | 6 | Text:11, Picture:2, Section-header:2, Title:2, Key-Value Region:1 |
| `docling-heron-101` | 18 | 6 | Text:11, Section-header:3, Picture:1, Key-Value Region:1, Title:1 |
| `docling-egret-medium` | 11 | 3 | Section-header:8, Text:2, Picture:1 |
| `aryn-deformable-detr-DocLayNet` | 1 | 1 | Picture:1 |
| `unstructured-yolox` | 12 | 4 | Text:9, Picture:1, Title:1, Table:1 |
| `rapidlayout-yolov8n_layout_report` | 9 | 4 | Text:6, Figure:1, Footer:1, Table:1 |
| `rapidlayout-yolov8n_layout_general6` | 5 | 3 | Text:3, Figure:1, Title:1 |
| `rapidlayout-yolov8n_layout_paper` | 5 | 2 | Text:4, Figure caption:1 |
| `rapidlayout-yolov8n_layout_publaynet` | 1 | 1 | Text:1 |
| `rapidlayout-pp_layout_cdla` | 6 | 3 | text:4, reference:1, figure:1 |
| `rapidlayout-pp_layout_publaynet` | 6 | 2 | text:4, title:2 |
| `rapidlayout-pp_layout_table` | 0 | 0 |  |
| `table-transformer-detection` | 0 | 0 |  |