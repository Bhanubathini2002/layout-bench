# Layout model benchmark — zhzvgdbvpypg.pdf

Canonical input: `layout_bench/page.png` (1754x2480). 20 models tested. Each folder has `overlay.png` + `detections.json`.

| Model | #Regions | #Classes | Notes |
|---|--:|--:|---|
| `rapidlayout-pp_doc_layoutv2` | 2 | 2 | table:1, footer:1 |
| `rapidlayout-pp_doc_layoutv3` | 2 | 2 | footer:1, table:1 |
| `rapidlayout-doclayout_d4la` | 6 | 3 | OtherText:4, Table:1, RegionKV:1 |
| `rapidlayout-doclayout_docsynth` | 2 | 2 | Picture:1, Text:1 |
| `rapidlayout-doclayout_docstructbench` | 1 | 1 | figure:1 |
| `docling-egret-medium` | 9 | 2 | Text:8, Section-header:1 |
| `docling-egret-large` | 3 | 2 | Page-footer:2, Picture:1 |
| `docling-heron-101` | 3 | 3 | Picture:1, Text:1, Page-footer:1 |
| `docling-heron` | 2 | 2 | picture:1, page_footer:1 |
| `aryn-deformable-detr-DocLayNet` | 1 | 1 | Picture:1 |
| `docling-egret-xlarge` | 1 | 1 | Picture:1 |
| `rapidlayout-yolov8n_layout_report` | 3 | 3 | Figure:1, Text:1, Footer:1 |
| `rapidlayout-yolov8n_layout_publaynet` | 2 | 2 | Figure:1, Text:1 |
| `unstructured-yolox` | 2 | 2 | Picture:1, Text:1 |
| `rapidlayout-yolov8n_layout_general6` | 1 | 1 | Figure:1 |
| `rapidlayout-yolov8n_layout_paper` | 1 | 1 | Figure:1 |
| `rapidlayout-pp_layout_cdla` | 2 | 2 | figure:1, figure_caption:1 |
| `rapidlayout-pp_layout_publaynet` | 2 | 2 | figure:1, text:1 |
| `rapidlayout-pp_layout_table` | 0 | 0 |  |
| `table-transformer-detection` | 0 | 0 |  |