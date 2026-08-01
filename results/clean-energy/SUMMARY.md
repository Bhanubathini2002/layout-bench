# Layout model benchmark — clean-energy.pdf

Canonical input: one rendered page (2480x1754). 20 models tested. Each folder holds `overlay.png` + `detections.json`.

| Model | #Regions | #Classes | Top classes |
|---|--:|--:|---|
| `rapidlayout-pp_doc_layoutv2` | 14 | 8 | chart:6, header:2, paragraph_title:1, footer_image:1, number:1 |
| `rapidlayout-pp_doc_layoutv3` | 14 | 7 | chart:6, header:2, vision_footnote:2, paragraph_title:1, footer_image:1 |
| `rapidlayout-doclayout_docstructbench` | 10 | 5 | abandon:5, table_footnote:2, figure:1, title:1, figure_caption:1 |
| `rapidlayout-doclayout_d4la` | 7 | 7 | Figure:1, PageNumber:1, PageHeader:1, OtherText:1, DocTitle:1 |
| `rapidlayout-doclayout_docsynth` | 7 | 5 | Page-header:2, Section-header:2, Page-footer:1, Text:1, Picture:1 |
| `docling-egret-xlarge` | 14 | 7 | page_header:3, text:3, section_header:2, picture:2, page_footer:2 |
| `docling-heron` | 14 | 7 | text:4, page_header:2, picture:2, page_footer:2, key_value_region:2 |
| `docling-egret-medium` | 13 | 6 | text:3, page_footer:3, picture:2, section_header:2, page_header:2 |
| `docling-egret-large` | 11 | 5 | text:3, section_header:2, picture:2, page_header:2, page_footer:2 |
| `docling-heron-101` | 11 | 5 | text:3, section_header:2, page_footer:2, page_header:2, picture:2 |
| `aryn-deformable-detr-DocLayNet` | 4 | 4 | Text:1, Page-footer:1, Section-header:1, Picture:1 |
| `unstructured-yolox` | 9 | 6 | Page-footer:2, Page-header:2, Text:2, Picture:1, Caption:1 |
| `rapidlayout-yolov8n_layout_report` | 8 | 7 | Figure:2, Header:1, Text:1, Footer:1, Figure caption:1 |
| `rapidlayout-yolov8n_layout_paper` | 5 | 4 | Header:2, Figure:1, Title:1, Text:1 |
| `rapidlayout-yolov8n_layout_general6` | 3 | 3 | Figure:1, Title:1, Text:1 |
| `rapidlayout-yolov8n_layout_publaynet` | 3 | 3 | Figure:1, Text:1, Title:1 |
| `rapidlayout-pp_layout_cdla` | 6 | 5 | footer:2, figure:1, figure_caption:1, header:1, text:1 |
| `rapidlayout-pp_layout_publaynet` | 4 | 2 | text:3, figure:1 |
| `rapidlayout-pp_layout_table` | 0 | 0 |  |
| `table-transformer-detection` | 0 | 0 |  |