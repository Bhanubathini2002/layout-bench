# Layout model benchmark — settlement-agreement.pdf

Canonical input: one rendered page (1917x2480). 20 models tested. Each folder holds `overlay.png` + `detections.json`.

| Model | #Regions | #Classes | Top classes |
|---|--:|--:|---|
| `rapidlayout-pp_doc_layoutv2` | 6 | 3 | text:4, table:1, number:1 |
| `rapidlayout-pp_doc_layoutv3` | 6 | 3 | text:4, table:1, number:1 |
| `rapidlayout-doclayout_docsynth` | 7 | 4 | Text:4, Table:1, Page-footer:1, Title:1 |
| `rapidlayout-doclayout_d4la` | 6 | 4 | ListText:3, ParaText:1, PageNumber:1, Table:1 |
| `rapidlayout-doclayout_docstructbench` | 6 | 3 | plain text:4, table:1, abandon:1 |
| `docling-egret-xlarge` | 10 | 4 | text:4, list_item:4, table:1, page_footer:1 |
| `docling-egret-large` | 9 | 4 | text:4, list_item:3, table:1, page_footer:1 |
| `docling-egret-medium` | 9 | 4 | text:4, list_item:3, table:1, page_footer:1 |
| `docling-heron` | 9 | 4 | text:4, list_item:3, table:1, page_footer:1 |
| `docling-heron-101` | 8 | 4 | text:3, list_item:3, table:1, page_footer:1 |
| `aryn-deformable-detr-DocLayNet` | 6 | 3 | Text:4, Page-footer:1, Table:1 |
| `rapidlayout-yolov8n_layout_paper` | 6 | 3 | Text:4, Table:1, Footer:1 |
| `rapidlayout-yolov8n_layout_report` | 6 | 3 | Text:4, Table:1, Footer:1 |
| `unstructured-yolox` | 6 | 3 | Text:4, Table:1, Page-footer:1 |
| `rapidlayout-yolov8n_layout_general6` | 5 | 2 | Text:4, Table:1 |
| `rapidlayout-yolov8n_layout_publaynet` | 4 | 1 | Text:4 |
| `rapidlayout-pp_layout_cdla` | 6 | 3 | text:4, table:1, footer:1 |
| `rapidlayout-pp_layout_publaynet` | 6 | 3 | text:3, table:2, list:1 |
| `rapidlayout-pp_layout_table` | 1 | 1 | table:1 |
| `table-transformer-detection` | 1 | 1 | table:1 |