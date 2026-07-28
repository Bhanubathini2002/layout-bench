# Layout model benchmark — yyvqfsbsmssm.pdf

Canonical input: `layout_bench/page.png` (1595x2480). 20 models tested. Each folder has `overlay.png` + `detections.json`.

| Model | #Regions | #Classes | Notes |
|---|--:|--:|---|
| `rapidlayout-pp_doc_layoutv2` | 7 | 4 | text:4, footer:1, paragraph_title:1, image:1 |
| `rapidlayout-pp_doc_layoutv3` | 3 | 2 | text:2, footer:1 |
| `rapidlayout-doclayout_docstructbench` | 6 | 3 | plain text:4, abandon:1, title:1 |
| `rapidlayout-doclayout_docsynth` | 6 | 2 | Text:4, Section-header:2 |
| `rapidlayout-doclayout_d4la` | 3 | 3 | RegionKV:1, OtherText:1, DocTitle:1 |
| `docling-egret-large` | 9 | 3 | Text:5, Section-header:2, Picture:2 |
| `docling-heron` | 7 | 3 | text:4, section_header:2, page_footer:1 |
| `docling-egret-medium` | 5 | 2 | Text:4, Page-footer:1 |
| `docling-heron-101` | 5 | 2 | Text:4, Page-footer:1 |
| `docling-egret-xlarge` | 3 | 1 | Text:3 |
| `aryn-deformable-detr-DocLayNet` | 1 | 1 | Text:1 |
| `rapidlayout-yolov8n_layout_report` | 7 | 3 | Text:4, Title:2, Figure:1 |
| `unstructured-yolox` | 5 | 3 | Text:3, Picture:1, Page-header:1 |
| `rapidlayout-yolov8n_layout_general6` | 4 | 2 | Text:3, Title:1 |
| `rapidlayout-yolov8n_layout_paper` | 2 | 2 | Figure caption:1, Title:1 |
| `rapidlayout-yolov8n_layout_publaynet` | 1 | 1 | Figure:1 |
| `rapidlayout-pp_layout_cdla` | 2 | 2 | figure:1, figure_caption:1 |
| `rapidlayout-pp_layout_publaynet` | 1 | 1 | figure:1 |
| `rapidlayout-pp_layout_table` | 0 | 0 |  |
| `table-transformer-detection` | 0 | 0 |  |