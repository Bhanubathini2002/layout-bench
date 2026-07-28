# Layout model benchmark — xqkjxvmrhmmp.pdf

Canonical input: `layout_bench/page.png` (1917x2480). 20 models tested. Each folder has `overlay.png` + `detections.json`.

| Model | #Regions | #Classes | Notes |
|---|--:|--:|---|
| `rapidlayout-pp_doc_layoutv2` | 4 | 3 | text:2, doc_title:1, footer:1 |
| `rapidlayout-pp_doc_layoutv3` | 4 | 2 | text:3, doc_title:1 |
| `rapidlayout-doclayout_docstructbench` | 6 | 3 | plain text:3, title:2, abandon:1 |
| `rapidlayout-doclayout_d4la` | 4 | 3 | OtherText:2, DocTitle:1, ParaText:1 |
| `rapidlayout-doclayout_docsynth` | 4 | 3 | Title:2, Text:1, Section-header:1 |
| `docling-egret-xlarge` | 7 | 4 | Text:3, Section-header:2, Title:1, Page-footer:1 |
| `docling-heron-101` | 7 | 3 | Text:3, Title:2, Section-header:2 |
| `docling-heron` | 7 | 3 | text:3, title:2, section_header:2 |
| `docling-egret-large` | 5 | 2 | Text:3, Section-header:2 |
| `docling-egret-medium` | 4 | 2 | Text:3, Title:1 |
| `aryn-deformable-detr-DocLayNet` | 2 | 1 | Text:2 |
| `rapidlayout-yolov8n_layout_general6` | 4 | 2 | Text:2, Title:2 |
| `unstructured-yolox` | 4 | 2 | Text:2, Title:2 |
| `rapidlayout-yolov8n_layout_paper` | 3 | 2 | Title:2, Text:1 |
| `rapidlayout-yolov8n_layout_report` | 3 | 2 | Title:2, Text:1 |
| `rapidlayout-yolov8n_layout_publaynet` | 1 | 1 | Title:1 |
| `rapidlayout-pp_layout_cdla` | 5 | 3 | text:3, title:1, header:1 |
| `rapidlayout-pp_layout_publaynet` | 4 | 2 | title:2, text:2 |
| `rapidlayout-pp_layout_table` | 0 | 0 |  |
| `table-transformer-detection` | 1 | 1 | table:1 |