# Layout model benchmark — hhwxyzvcrpgk.pdf

Canonical input: `layout_bench/page.png` (1917x2480). 20 models tested. Each folder has `overlay.png` + `detections.json`.

| Model | #Regions | #Classes | Notes |
|---|--:|--:|---|
| `rapidlayout-pp_doc_layoutv2` | 22 | 6 | text:9, aside_text:7, header:3, doc_title:1, paragraph_title:1 |
| `rapidlayout-pp_doc_layoutv3` | 22 | 6 | text:8, aside_text:7, header:4, doc_title:1, paragraph_title:1 |
| `rapidlayout-doclayout_d4la` | 13 | 5 | ParaText:7, OtherText:3, ParaTitle:1, DocTitle:1, PageHeader:1 |
| `rapidlayout-doclayout_docstructbench` | 13 | 3 | plain text:8, abandon:3, title:2 |
| `rapidlayout-doclayout_docsynth` | 13 | 3 | Text:7, Section-header:5, Page-footer:1 |
| `docling-egret-large` | 18 | 4 | Text:14, Section-header:2, Title:1, Page-footer:1 |
| `docling-egret-xlarge` | 18 | 4 | Text:13, Section-header:3, Page-footer:1, Page-header:1 |
| `docling-heron` | 18 | 4 | text:12, section_header:4, page_footer:1, page_header:1 |
| `docling-egret-medium` | 16 | 4 | Text:11, Section-header:3, Page-footer:1, Page-header:1 |
| `docling-heron-101` | 16 | 4 | Text:11, Section-header:3, Page-footer:1, Page-header:1 |
| `aryn-deformable-detr-DocLayNet` | 10 | 3 | Text:7, Section-header:2, Page-footer:1 |
| `rapidlayout-yolov8n_layout_report` | 20 | 2 | Text:17, Title:3 |
| `unstructured-yolox` | 17 | 3 | Text:10, Section-header:6, Page-footer:1 |
| `rapidlayout-yolov8n_layout_general6` | 15 | 2 | Text:12, Title:3 |
| `rapidlayout-yolov8n_layout_paper` | 15 | 3 | Text:10, Title:3, Header:2 |
| `rapidlayout-yolov8n_layout_publaynet` | 5 | 3 | List:2, Title:2, Text:1 |
| `rapidlayout-pp_layout_cdla` | 12 | 4 | text:4, header:4, title:2, footer:2 |
| `rapidlayout-pp_layout_publaynet` | 10 | 3 | text:6, list:2, title:2 |
| `rapidlayout-pp_layout_table` | 0 | 0 |  |
| `table-transformer-detection` | 1 | 1 | table:1 |