# Layout model benchmark — hjbyjvncdmpx.pdf

Canonical input: `layout_bench/page.png` (1917x2480). 20 models tested. Each folder has `overlay.png` + `detections.json`.

| Model | #Regions | #Classes | Notes |
|---|--:|--:|---|
| `rapidlayout-pp_doc_layoutv2` | 29 | 8 | text:14, paragraph_title:7, footnote:3, doc_title:1, header:1 |
| `rapidlayout-pp_doc_layoutv3` | 28 | 7 | text:15, paragraph_title:7, footnote:2, doc_title:1, header:1 |
| `rapidlayout-doclayout_docsynth` | 30 | 5 | Text:24, Page-header:2, Section-header:2, List-item:1, Title:1 |
| `rapidlayout-doclayout_d4la` | 26 | 10 | ParaText:10, ParaTitle:5, ListText:3, OtherText:2, Table:1 |
| `rapidlayout-doclayout_docstructbench` | 24 | 3 | plain text:19, title:3, abandon:2 |
| `docling-heron` | 54 | 8 | text:31, section_header:8, list_item:6, footnote:4, page_header:2 |
| `docling-egret-xlarge` | 48 | 7 | Text:27, Section-header:11, List-item:3, Page-footer:3, Page-header:2 |
| `docling-heron-101` | 45 | 8 | Text:29, Section-header:6, List-item:3, Page-header:2, Footnote:2 |
| `docling-egret-medium` | 30 | 4 | Text:25, Section-header:3, Page-header:1, Title:1 |
| `docling-egret-large` | 22 | 4 | Text:18, Section-header:2, Title:1, List-item:1 |
| `aryn-deformable-detr-DocLayNet` | 14 | 4 | Text:6, Section-header:5, Page-header:2, List-item:1 |
| `unstructured-yolox` | 26 | 4 | Text:21, List-item:2, Page-header:2, Section-header:1 |
| `rapidlayout-yolov8n_layout_report` | 21 | 3 | Text:16, Title:4, Header:1 |
| `rapidlayout-yolov8n_layout_general6` | 15 | 2 | Text:12, Title:3 |
| `rapidlayout-yolov8n_layout_paper` | 15 | 4 | Text:9, Title:4, Header:1, Reference:1 |
| `rapidlayout-yolov8n_layout_publaynet` | 4 | 3 | Text:2, Title:1, Figure:1 |
| `rapidlayout-pp_layout_publaynet` | 16 | 3 | text:12, title:2, list:2 |
| `rapidlayout-pp_layout_cdla` | 12 | 5 | text:7, header:2, title:1, reference:1, figure:1 |
| `rapidlayout-pp_layout_table` | 0 | 0 |  |
| `table-transformer-detection` | 0 | 0 |  |