# Layout model benchmark — finance-10k.pdf

Canonical input: one rendered page (1917x2480). 20 models tested. Each folder holds `overlay.png` + `detections.json`.

| Model | #Regions | #Classes | Top classes |
|---|--:|--:|---|
| `rapidlayout-pp_doc_layoutv2` | 6 | 5 | paragraph_title:2, table:1, footer:1, vision_footnote:1, header:1 |
| `rapidlayout-pp_doc_layoutv3` | 4 | 4 | table:1, footer:1, vision_footnote:1, paragraph_title:1 |
| `rapidlayout-doclayout_d4la` | 11 | 6 | RegionTitle:3, TableName:3, ParaText:2, PageFooter:1, RegionList:1 |
| `rapidlayout-doclayout_docsynth` | 6 | 4 | Section-header:2, Text:2, Table:1, Page-footer:1 |
| `rapidlayout-doclayout_docstructbench` | 3 | 3 | table:1, abandon:1, plain text:1 |
| `docling-egret-large` | 7 | 5 | text:2, section_header:2, table:1, page_footer:1, page_header:1 |
| `docling-heron-101` | 7 | 5 | text:2, section_header:2, table:1, page_footer:1, page_header:1 |
| `docling-heron` | 7 | 5 | text:2, section_header:2, table:1, page_footer:1, page_header:1 |
| `aryn-deformable-detr-DocLayNet` | 6 | 4 | Text:2, Section-header:2, Table:1, Page-footer:1 |
| `docling-egret-medium` | 6 | 4 | text:2, section_header:2, table:1, page_footer:1 |
| `docling-egret-xlarge` | 6 | 4 | text:2, section_header:2, table:1, page_footer:1 |
| `rapidlayout-yolov8n_layout_report` | 6 | 5 | Text:2, Table:1, Footer:1, Title:1, Header:1 |
| `unstructured-yolox` | 6 | 3 | Text:3, Section-header:2, Table:1 |
| `rapidlayout-yolov8n_layout_general6` | 4 | 3 | Title:2, Table:1, Text:1 |
| `rapidlayout-yolov8n_layout_paper` | 4 | 4 | Header:1, Table caption:1, Footer:1, Figure:1 |
| `rapidlayout-yolov8n_layout_publaynet` | 1 | 1 | Table:1 |
| `rapidlayout-pp_layout_cdla` | 6 | 5 | text:2, table:1, footer:1, table_caption:1, header:1 |
| `rapidlayout-pp_layout_publaynet` | 6 | 3 | text:4, table:1, title:1 |
| `rapidlayout-pp_layout_table` | 1 | 1 | table:1 |
| `table-transformer-detection` | 1 | 1 | table:1 |