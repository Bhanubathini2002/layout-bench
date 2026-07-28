# Layout model benchmark — ykctxqgxptrs.pdf

Canonical input: `layout_bench/page.png` (1917x2480). 20 models tested. Each folder has `overlay.png` + `detections.json`.

| Model | #Regions | #Classes | Notes |
|---|--:|--:|---|
| `rapidlayout-pp_doc_layoutv2` | 27 | 6 | text:13, paragraph_title:8, footnote:3, doc_title:1, header:1 |
| `rapidlayout-pp_doc_layoutv3` | 26 | 6 | text:12, paragraph_title:8, footnote:3, doc_title:1, header:1 |
| `rapidlayout-doclayout_docstructbench` | 23 | 3 | plain text:16, title:4, abandon:3 |
| `rapidlayout-doclayout_docsynth` | 23 | 3 | Text:20, Page-header:2, Title:1 |
| `rapidlayout-doclayout_d4la` | 16 | 7 | ParaText:7, ParaTitle:3, OtherText:2, DocTitle:1, Date:1 |
| `docling-heron` | 45 | 8 | text:25, section_header:7, list_item:5, footnote:3, page_header:2 |
| `docling-egret-xlarge` | 44 | 6 | Text:26, Section-header:8, List-item:4, Page-footer:3, Page-header:2 |
| `docling-egret-large` | 41 | 6 | Text:31, Section-header:3, List-item:3, Title:2, Page-header:1 |
| `docling-egret-medium` | 41 | 5 | Text:28, Section-header:6, List-item:4, Page-header:2, Title:1 |
| `docling-heron-101` | 41 | 6 | Text:22, Section-header:10, List-item:4, Page-header:2, Footnote:2 |
| `aryn-deformable-detr-DocLayNet` | 22 | 4 | Text:11, Section-header:8, Page-header:2, Footnote:1 |
| `unstructured-yolox` | 27 | 4 | Text:15, Section-header:7, List-item:3, Page-header:2 |
| `rapidlayout-yolov8n_layout_paper` | 17 | 4 | Text:13, Title:2, Reference:1, Header:1 |
| `rapidlayout-yolov8n_layout_general6` | 14 | 2 | Text:9, Title:5 |
| `rapidlayout-yolov8n_layout_report` | 9 | 4 | Text:5, Title:2, Header:1, Table:1 |
| `rapidlayout-yolov8n_layout_publaynet` | 3 | 2 | Text:2, Title:1 |
| `rapidlayout-pp_layout_publaynet` | 28 | 2 | text:18, title:10 |
| `rapidlayout-pp_layout_cdla` | 17 | 4 | text:13, reference:2, title:1, header:1 |
| `rapidlayout-pp_layout_table` | 0 | 0 |  |
| `table-transformer-detection` | 0 | 0 |  |