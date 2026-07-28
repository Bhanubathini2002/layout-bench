# Layout model benchmark — sbvwbwjptgts.pdf

Canonical input: `layout_bench/page.png` (1839x2480). 20 models tested. Each folder has `overlay.png` + `detections.json`.

| Model | #Regions | #Classes | Notes |
|---|--:|--:|---|
| `rapidlayout-pp_doc_layoutv2` | 36 | 8 | text:28, footnote:2, abstract:1, doc_title:1, paragraph_title:1 |
| `rapidlayout-pp_doc_layoutv3` | 36 | 8 | text:28, footnote:2, abstract:1, doc_title:1, footer:1 |
| `rapidlayout-doclayout_d4la` | 39 | 12 | ListText:22, ParaText:4, OtherText:4, Footer:1, DocTitle:1 |
| `rapidlayout-doclayout_docsynth` | 37 | 7 | List-item:23, Text:8, Footnote:2, Page-footer:1, Title:1 |
| `rapidlayout-doclayout_docstructbench` | 17 | 3 | plain text:10, abandon:4, title:3 |
| `docling-egret-medium` | 43 | 8 | List-item:21, Text:12, Footnote:3, Page-footer:2, Section-header:2 |
| `docling-heron-101` | 42 | 6 | List-item:21, Text:14, Page-footer:2, Footnote:2, Section-header:2 |
| `docling-heron` | 41 | 7 | list_item:21, text:12, footnote:2, page_footer:2, section_header:2 |
| `docling-egret-large` | 40 | 7 | List-item:21, Text:10, Section-header:3, Page-footer:2, Footnote:2 |
| `docling-egret-xlarge` | 40 | 7 | List-item:22, Text:10, Page-footer:2, Footnote:2, Section-header:2 |
| `aryn-deformable-detr-DocLayNet` | 37 | 7 | List-item:21, Text:9, Page-footer:2, Footnote:2, Page-header:1 |
| `unstructured-yolox` | 37 | 5 | List-item:23, Text:10, Title:2, Page-header:1, Section-header:1 |
| `rapidlayout-yolov8n_layout_report` | 35 | 3 | Text:32, Title:2, Header:1 |
| `rapidlayout-yolov8n_layout_general6` | 21 | 2 | Text:19, Title:2 |
| `rapidlayout-yolov8n_layout_paper` | 14 | 3 | Text:10, Title:3, Figure:1 |
| `rapidlayout-yolov8n_layout_publaynet` | 2 | 2 | Text:1, Figure:1 |
| `rapidlayout-pp_layout_cdla` | 18 | 5 | text:10, reference:3, title:2, footer:2, header:1 |
| `rapidlayout-pp_layout_publaynet` | 14 | 3 | text:10, list:2, title:2 |
| `rapidlayout-pp_layout_table` | 0 | 0 |  |
| `table-transformer-detection` | 0 | 0 |  |