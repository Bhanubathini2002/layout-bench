# Layout model benchmark — clinical-study.pdf

Canonical input: one rendered page (1917x2480). 20 models tested. Each folder holds `overlay.png` + `detections.json`.

| Model | #Regions | #Classes | Top classes |
|---|--:|--:|---|
| `rapidlayout-pp_doc_layoutv2` | 25 | 8 | text:14, paragraph_title:4, image:2, abstract:1, doc_title:1 |
| `rapidlayout-pp_doc_layoutv3` | 24 | 8 | text:13, paragraph_title:4, image:2, doc_title:1, header:1 |
| `rapidlayout-doclayout_docstructbench` | 24 | 4 | plain text:14, abandon:5, title:4, figure:1 |
| `rapidlayout-doclayout_docsynth` | 23 | 5 | Text:14, Section-header:5, Page-footer:2, Picture:1, Page-header:1 |
| `rapidlayout-doclayout_d4la` | 21 | 9 | ParaText:7, OtherText:4, ParaTitle:4, DocTitle:1, Author:1 |
| `docling-egret-xlarge` | 40 | 8 | text:20, section_header:8, page_footer:5, picture:2, list_item:2 |
| `docling-egret-medium` | 37 | 8 | text:19, section_header:7, page_footer:4, picture:3, page_header:1 |
| `docling-heron-101` | 37 | 8 | text:20, section_header:7, page_footer:4, picture:2, key_value_region:1 |
| `docling-heron` | 36 | 8 | text:18, section_header:7, picture:3, page_footer:3, list_item:2 |
| `docling-egret-large` | 32 | 6 | text:17, section_header:7, page_footer:4, picture:2, key_value_region:1 |
| `aryn-deformable-detr-DocLayNet` | 20 | 4 | Text:13, Section-header:4, Page-footer:2, Picture:1 |
| `rapidlayout-yolov8n_layout_report` | 25 | 5 | Text:16, Title:6, Figure:1, Footer:1, Figure caption:1 |
| `unstructured-yolox` | 22 | 4 | Text:15, Section-header:5, List-item:1, Picture:1 |
| `rapidlayout-yolov8n_layout_general6` | 21 | 3 | Text:13, Title:7, Figure:1 |
| `rapidlayout-yolov8n_layout_paper` | 17 | 5 | Text:8, Title:5, Reference:2, Figure:1, Header:1 |
| `rapidlayout-yolov8n_layout_publaynet` | 8 | 2 | Text:4, Title:4 |
| `rapidlayout-pp_layout_cdla` | 20 | 6 | text:7, title:6, reference:4, header:1, footer:1 |
| `rapidlayout-pp_layout_publaynet` | 10 | 2 | text:6, title:4 |
| `rapidlayout-pp_layout_table` | 0 | 0 |  |
| `table-transformer-detection` | 2 | 1 | table:2 |