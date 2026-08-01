# Layout model benchmark — purchase-agreement.pdf

Canonical input: one rendered page (1917x2480). 20 models tested. Each folder holds `overlay.png` + `detections.json`.

| Model | #Regions | #Classes | Top classes |
|---|--:|--:|---|
| `rapidlayout-pp_doc_layoutv2` | 11 | 4 | text:7, paragraph_title:2, footer:1, header:1 |
| `rapidlayout-pp_doc_layoutv3` | 11 | 4 | text:7, paragraph_title:2, footer:1, header:1 |
| `rapidlayout-doclayout_d4la` | 12 | 4 | ParaText:6, OtherText:3, ParaTitle:2, DocTitle:1 |
| `rapidlayout-doclayout_docsynth` | 12 | 3 | Text:9, Section-header:2, Page-footer:1 |
| `rapidlayout-doclayout_docstructbench` | 9 | 3 | plain text:6, title:2, abandon:1 |
| `docling-egret-large` | 14 | 5 | text:9, section_header:2, page_footer:1, page_header:1, form:1 |
| `docling-egret-medium` | 14 | 5 | text:8, section_header:2, form:2, page_footer:1, title:1 |
| `docling-heron-101` | 13 | 5 | text:7, section_header:3, page_footer:1, form:1, page_header:1 |
| `docling-heron` | 13 | 3 | text:10, section_header:2, page_footer:1 |
| `docling-egret-xlarge` | 11 | 4 | text:7, section_header:2, page_footer:1, page_header:1 |
| `aryn-deformable-detr-DocLayNet` | 10 | 3 | Text:7, Section-header:2, Page-footer:1 |
| `rapidlayout-yolov8n_layout_paper` | 14 | 4 | Text:9, Title:2, Reference:2, Header:1 |
| `rapidlayout-yolov8n_layout_report` | 12 | 3 | Text:9, Title:2, Header:1 |
| `unstructured-yolox` | 10 | 2 | Text:8, Section-header:2 |
| `rapidlayout-yolov8n_layout_general6` | 9 | 2 | Text:7, Title:2 |
| `rapidlayout-yolov8n_layout_publaynet` | 6 | 1 | Text:6 |
| `rapidlayout-pp_layout_cdla` | 11 | 4 | text:6, title:2, reference:2, footer:1 |
| `rapidlayout-pp_layout_publaynet` | 9 | 2 | text:7, title:2 |
| `rapidlayout-pp_layout_table` | 0 | 0 |  |
| `table-transformer-detection` | 1 | 1 | table:1 |