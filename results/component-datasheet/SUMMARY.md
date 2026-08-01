# Layout model benchmark — component-datasheet.pdf

Canonical input: one rendered page (1754x2480). 20 models tested. Each folder holds `overlay.png` + `detections.json`.

| Model | #Regions | #Classes | Top classes |
|---|--:|--:|---|
| `rapidlayout-pp_doc_layoutv2` | 26 | 7 | text:19, image:2, header:1, doc_title:1, footer:1 |
| `rapidlayout-pp_doc_layoutv3` | 24 | 7 | text:18, image:1, header:1, footer:1, vision_footnote:1 |
| `rapidlayout-doclayout_d4la` | 26 | 8 | ListText:16, ParaText:2, OtherText:2, Figure:2, DocTitle:1 |
| `rapidlayout-doclayout_docsynth` | 25 | 6 | List-item:16, Text:4, Page-footer:2, Picture:1, Section-header:1 |
| `rapidlayout-doclayout_docstructbench` | 12 | 5 | plain text:6, abandon:3, figure:1, title:1, figure_caption:1 |
| `docling-heron-101` | 26 | 7 | list_item:16, text:4, page_footer:2, picture:1, section_header:1 |
| `docling-heron` | 26 | 7 | list_item:16, text:4, page_footer:2, section_header:1, page_header:1 |
| `aryn-deformable-detr-DocLayNet` | 25 | 7 | List-item:16, Text:3, Page-footer:2, Picture:1, Page-header:1 |
| `docling-egret-large` | 25 | 6 | list_item:16, text:4, page_footer:2, section_header:1, picture:1 |
| `docling-egret-medium` | 25 | 6 | list_item:16, text:4, page_footer:2, section_header:1, picture:1 |
| `docling-egret-xlarge` | 25 | 6 | list_item:16, text:4, page_footer:2, section_header:1, page_header:1 |
| `unstructured-yolox` | 24 | 5 | List-item:14, Text:7, Picture:1, Page-header:1, Section-header:1 |
| `rapidlayout-yolov8n_layout_general6` | 19 | 3 | Text:17, Figure:1, Title:1 |
| `rapidlayout-yolov8n_layout_report` | 19 | 5 | Text:15, Figure:1, Header:1, Footer:1, Title:1 |
| `rapidlayout-yolov8n_layout_paper` | 6 | 5 | Text:2, Title:1, Figure:1, Header:1, Reference:1 |
| `rapidlayout-yolov8n_layout_publaynet` | 4 | 3 | List:2, Text:1, Figure:1 |
| `rapidlayout-pp_layout_cdla` | 10 | 7 | figure:2, footer:2, reference:2, title:1, header:1 |
| `rapidlayout-pp_layout_publaynet` | 7 | 4 | text:3, list:2, figure:1, title:1 |
| `rapidlayout-pp_layout_table` | 0 | 0 |  |
| `table-transformer-detection` | 1 | 1 | table:1 |