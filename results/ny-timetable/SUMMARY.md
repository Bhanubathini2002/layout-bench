# Layout model benchmark — ny-timetable.pdf

Canonical input: one rendered page (1917x2480). 20 models tested. Each folder holds `overlay.png` + `detections.json`.

| Model | #Regions | #Classes | Top classes |
|---|--:|--:|---|
| `rapidlayout-pp_doc_layoutv2` | 2 | 2 | table:1, number:1 |
| `rapidlayout-pp_doc_layoutv3` | 2 | 2 | table:1, number:1 |
| `rapidlayout-doclayout_d4la` | 2 | 2 | Table:1, PageNumber:1 |
| `rapidlayout-doclayout_docstructbench` | 2 | 2 | table:1, abandon:1 |
| `rapidlayout-doclayout_docsynth` | 2 | 2 | Page-footer:1, Table:1 |
| `docling-egret-xlarge` | 4 | 3 | section_header:2, table:1, page_footer:1 |
| `aryn-deformable-detr-DocLayNet` | 2 | 2 | Page-footer:1, Table:1 |
| `docling-egret-large` | 2 | 2 | table:1, page_footer:1 |
| `docling-egret-medium` | 2 | 2 | table:1, page_footer:1 |
| `docling-heron-101` | 2 | 2 | table:1, page_footer:1 |
| `docling-heron` | 2 | 2 | table:1, page_footer:1 |
| `unstructured-yolox` | 4 | 2 | Section-header:3, Table:1 |
| `rapidlayout-yolov8n_layout_paper` | 3 | 3 | Table:1, Footer:1, Table caption:1 |
| `rapidlayout-yolov8n_layout_report` | 3 | 3 | Table:1, Footer:1, Table caption:1 |
| `rapidlayout-yolov8n_layout_general6` | 2 | 2 | Table:1, Text:1 |
| `rapidlayout-yolov8n_layout_publaynet` | 2 | 2 | Figure:1, Title:1 |
| `rapidlayout-pp_layout_publaynet` | 3 | 3 | table:1, title:1, text:1 |
| `rapidlayout-pp_layout_cdla` | 2 | 2 | table:1, footer:1 |
| `rapidlayout-pp_layout_table` | 1 | 1 | table:1 |
| `table-transformer-detection` | 1 | 1 | table rotated:1 |