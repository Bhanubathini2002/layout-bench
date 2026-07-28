# Layout model benchmark — cnpkkjdkyhhw.pdf

Canonical input: `layout_bench/page.png` (1754x2480). 20 models tested. Each folder has `overlay.png` + `detections.json`.

| Model | #Regions | #Classes | Notes |
|---|--:|--:|---|
| `rapidlayout-pp_doc_layoutv2` | 67 | 10 | text:25, paragraph_title:22, image:11, footer:2, table:2 |
| `rapidlayout-pp_doc_layoutv3` | 60 | 5 | text:33, paragraph_title:15, image:10, doc_title:1, footer:1 |
| `rapidlayout-doclayout_docsynth` | 45 | 4 | Section-header:19, Picture:9, Text:9, List-item:8 |
| `rapidlayout-doclayout_docstructbench` | 39 | 4 | title:19, plain text:13, figure:5, abandon:2 |
| `rapidlayout-doclayout_d4la` | 15 | 7 | Figure:4, Table:2, ParaText:2, RegionList:2, RegionTitle:2 |
| `docling-egret-xlarge` | 142 | 6 | Text:81, Picture:24, Section-header:24, Key-Value Region:6, Page-footer:6 |
| `docling-heron` | 131 | 6 | text:61, picture:30, section_header:21, key_value_region:8, page_footer:6 |
| `docling-egret-medium` | 124 | 5 | Text:65, Picture:27, Section-header:23, Key-Value Region:5, Page-footer:4 |
| `docling-heron-101` | 122 | 8 | Text:68, Picture:22, Section-header:22, Key-Value Region:6, Page-footer:1 |
| `docling-egret-large` | 109 | 6 | Text:57, Picture:24, Section-header:17, Key-Value Region:5, Page-footer:5 |
| `aryn-deformable-detr-DocLayNet` | 12 | 3 | Picture:5, Section-header:5, Text:2 |
| `unstructured-yolox` | 45 | 6 | Section-header:20, Text:12, List-item:6, Picture:5, Table:1 |
| `rapidlayout-yolov8n_layout_general6` | 44 | 5 | Text:21, Title:12, Figure:8, Table:2, Caption:1 |
| `rapidlayout-yolov8n_layout_report` | 28 | 6 | Text:7, Table caption:6, Figure:5, Title:5, Table:4 |
| `rapidlayout-yolov8n_layout_paper` | 22 | 6 | Table caption:6, Text:4, Figure:3, Table:3, Reference:3 |
| `rapidlayout-yolov8n_layout_publaynet` | 2 | 2 | Text:1, Figure:1 |
| `rapidlayout-pp_layout_cdla` | 6 | 5 | text:2, figure:1, header:1, title:1, reference:1 |
| `rapidlayout-pp_layout_table` | 3 | 1 | table:3 |
| `rapidlayout-pp_layout_publaynet` | 2 | 2 | figure:1, title:1 |
| `table-transformer-detection` | 0 | 0 |  |