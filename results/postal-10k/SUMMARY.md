# Layout model benchmark — postal-10k.pdf

Canonical input: one rendered page (1917x2480). 20 models tested. Each folder holds `overlay.png` + `detections.json`.

| Model | #Regions | #Classes | Top classes |
|---|--:|--:|---|
| `rapidlayout-pp_doc_layoutv2` | 6 | 6 | table:1, text:1, paragraph_title:1, footer:1, number:1 |
| `rapidlayout-pp_doc_layoutv3` | 5 | 5 | table:1, paragraph_title:1, text:1, footer:1, number:1 |
| `rapidlayout-doclayout_d4la` | 5 | 5 | PageFooter:1, DocTitle:1, RegionList:1, ParaText:1, RegionTitle:1 |
| `rapidlayout-doclayout_docstructbench` | 4 | 4 | table:1, abandon:1, title:1, table_caption:1 |
| `rapidlayout-doclayout_docsynth` | 4 | 4 | Page-footer:1, Table:1, Section-header:1, Text:1 |
| `aryn-deformable-detr-DocLayNet` | 4 | 4 | Page-footer:1, Table:1, Text:1, Section-header:1 |
| `docling-egret-large` | 4 | 4 | table:1, text:1, page_footer:1, section_header:1 |
| `docling-egret-medium` | 4 | 4 | table:1, section_header:1, text:1, page_footer:1 |
| `docling-egret-xlarge` | 4 | 4 | table:1, text:1, page_footer:1, section_header:1 |
| `docling-heron-101` | 4 | 4 | table:1, text:1, page_footer:1, section_header:1 |
| `docling-heron` | 4 | 4 | table:1, text:1, section_header:1, page_footer:1 |
| `unstructured-yolox` | 9 | 4 | List-item:5, Text:2, Table:1, Section-header:1 |
| `rapidlayout-yolov8n_layout_general6` | 3 | 2 | Title:2, Table:1 |
| `rapidlayout-yolov8n_layout_report` | 3 | 3 | Table:1, Footer:1, Title:1 |
| `rapidlayout-yolov8n_layout_paper` | 2 | 2 | Table:1, Header:1 |
| `rapidlayout-yolov8n_layout_publaynet` | 1 | 1 | Table:1 |
| `rapidlayout-pp_layout_cdla` | 5 | 3 | table:2, table_caption:2, footer:1 |
| `rapidlayout-pp_layout_publaynet` | 2 | 2 | table:1, text:1 |
| `rapidlayout-pp_layout_table` | 1 | 1 | table:1 |
| `table-transformer-detection` | 1 | 1 | table:1 |