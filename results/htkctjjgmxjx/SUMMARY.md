# Layout model benchmark — htkctjjgmxjx.pdf

Canonical input: `layout_bench/page.png` (2480x1754). 20 models tested. Each folder has `overlay.png` + `detections.json`.

| Model | #Regions | #Classes | Notes |
|---|--:|--:|---|
| `rapidlayout-pp_doc_layoutv2` | 7 | 5 | image:2, text:2, display_formula:1, figure_title:1, table:1 |
| `rapidlayout-pp_doc_layoutv3` | 2 | 1 | image:2 |
| `rapidlayout-doclayout_d4la` | 7 | 6 | DocTitle:2, Figure:1, FigureName:1, Number:1, RegionList:1 |
| `rapidlayout-doclayout_docstructbench` | 2 | 2 | plain text:1, figure:1 |
| `rapidlayout-doclayout_docsynth` | 2 | 1 | Picture:2 |
| `docling-egret-medium` | 19 | 4 | Picture:11, Text:5, Section-header:2, Page-header:1 |
| `docling-heron-101` | 19 | 8 | Picture:5, Text:4, List-item:3, Section-header:2, Table:2 |
| `docling-egret-xlarge` | 17 | 6 | Picture:6, Text:4, Section-header:3, List-item:2, Caption:1 |
| `docling-heron` | 16 | 7 | picture:4, text:3, formula:2, page_header:2, list_item:2 |
| `docling-egret-large` | 4 | 3 | Picture:2, Text:1, Section-header:1 |
| `aryn-deformable-detr-DocLayNet` | 2 | 1 | Picture:2 |
| `rapidlayout-yolov8n_layout_paper` | 6 | 3 | Text:3, Figure:2, Figure caption:1 |
| `unstructured-yolox` | 6 | 3 | Caption:3, Picture:2, Table:1 |
| `rapidlayout-yolov8n_layout_general6` | 2 | 1 | Figure:2 |
| `rapidlayout-yolov8n_layout_publaynet` | 2 | 1 | Figure:2 |
| `rapidlayout-yolov8n_layout_report` | 2 | 1 | Figure:2 |
| `rapidlayout-pp_layout_cdla` | 9 | 4 | figure:4, text:3, figure_caption:1, reference:1 |
| `rapidlayout-pp_layout_publaynet` | 0 | 0 |  |
| `rapidlayout-pp_layout_table` | 0 | 0 |  |
| `table-transformer-detection` | 0 | 0 |  |