# Layout model benchmark — zdwfjfszkcgj.pdf

Canonical input: `layout_bench/page.png` (1754x2480). 20 models tested. Each folder has `overlay.png` + `detections.json`.

| Model | #Regions | #Classes | Notes |
|---|--:|--:|---|
| `rapidlayout-pp_doc_layoutv3` | 18 | 4 | text:13, header:2, footer:2, header_image:1 |
| `rapidlayout-pp_doc_layoutv2` | 16 | 4 | text:13, header:1, footer:1, header_image:1 |
| `rapidlayout-doclayout_d4la` | 14 | 8 | RegionKV:4, OtherText:3, ParaText:2, Figure:1, Date:1 |
| `rapidlayout-doclayout_docstructbench` | 12 | 3 | plain text:8, abandon:2, title:2 |
| `rapidlayout-doclayout_docsynth` | 11 | 3 | Text:8, Picture:2, Page-header:1 |
| `docling-egret-large` | 27 | 6 | Text:11, Page-footer:10, Picture:2, Key-Value Region:2, Section-header:1 |
| `docling-heron-101` | 24 | 5 | Text:9, Page-footer:7, Key-Value Region:4, Picture:2, Page-header:2 |
| `docling-heron` | 20 | 5 | text:10, page_footer:6, picture:2, key_value_region:1, section_header:1 |
| `docling-egret-medium` | 15 | 3 | Text:9, Page-footer:4, Picture:2 |
| `aryn-deformable-detr-DocLayNet` | 8 | 4 | Text:4, Picture:2, Page-header:1, Page-footer:1 |
| `docling-egret-xlarge` | 7 | 3 | Text:4, Picture:2, Section-header:1 |
| `rapidlayout-yolov8n_layout_report` | 22 | 4 | Text:18, Header:2, Figure:1, Title:1 |
| `rapidlayout-yolov8n_layout_paper` | 14 | 3 | Text:8, Header:5, Title:1 |
| `unstructured-yolox` | 14 | 4 | Text:10, Section-header:2, Picture:1, Page-header:1 |
| `rapidlayout-yolov8n_layout_general6` | 9 | 3 | Text:7, Figure:1, Title:1 |
| `rapidlayout-yolov8n_layout_publaynet` | 6 | 2 | Text:4, Title:2 |
| `rapidlayout-pp_layout_cdla` | 15 | 6 | text:7, header:4, reference:1, title:1, footer:1 |
| `rapidlayout-pp_layout_publaynet` | 5 | 2 | text:4, title:1 |
| `rapidlayout-pp_layout_table` | 0 | 0 |  |
| `table-transformer-detection` | 0 | 0 |  |