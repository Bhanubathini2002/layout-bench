# Layout model benchmark — trzckszdbryk.pdf

Canonical input: `layout_bench/page.png` (1754x2480). 20 models tested. Each folder has `overlay.png` + `detections.json`.

| Model | #Regions | #Classes | Notes |
|---|--:|--:|---|
| `rapidlayout-pp_doc_layoutv2` | 19 | 6 | text:9, paragraph_title:3, header:3, footer:2, abstract:1 |
| `rapidlayout-pp_doc_layoutv3` | 19 | 6 | text:9, paragraph_title:3, header:3, footer:2, abstract:1 |
| `rapidlayout-doclayout_d4la` | 20 | 8 | ParaText:7, ParaTitle:3, OtherText:2, PageFooter:2, PageHeader:2 |
| `rapidlayout-doclayout_docsynth` | 20 | 5 | Text:10, Section-header:5, Page-footer:2, Page-header:2, Title:1 |
| `rapidlayout-doclayout_docstructbench` | 19 | 3 | plain text:10, abandon:5, title:4 |
| `docling-heron` | 34 | 5 | text:15, page_footer:9, section_header:5, page_header:3, key_value_region:2 |
| `docling-egret-large` | 26 | 5 | Text:14, Section-header:5, Page-footer:4, Page-header:2, Key-Value Region:1 |
| `docling-egret-medium` | 26 | 5 | Text:13, Section-header:5, Page-footer:5, Page-header:2, List-item:1 |
| `docling-heron-101` | 25 | 5 | Text:12, Section-header:5, Page-footer:4, Page-header:2, List-item:2 |
| `docling-egret-xlarge` | 20 | 4 | Text:11, Section-header:5, Page-header:2, Page-footer:2 |
| `aryn-deformable-detr-DocLayNet` | 15 | 4 | Text:9, Section-header:3, Page-header:2, Title:1 |
| `rapidlayout-yolov8n_layout_report` | 23 | 4 | Text:12, Title:4, Footer:4, Header:3 |
| `unstructured-yolox` | 19 | 4 | Text:12, Section-header:4, Page-header:2, Footnote:1 |
| `rapidlayout-yolov8n_layout_paper` | 17 | 3 | Text:11, Title:4, Reference:2 |
| `rapidlayout-yolov8n_layout_general6` | 15 | 2 | Text:11, Title:4 |
| `rapidlayout-yolov8n_layout_publaynet` | 12 | 2 | Text:8, Title:4 |
| `rapidlayout-pp_layout_cdla` | 18 | 4 | text:10, title:4, header:2, reference:2 |
| `rapidlayout-pp_layout_publaynet` | 14 | 2 | text:9, title:5 |
| `rapidlayout-pp_layout_table` | 0 | 0 |  |
| `table-transformer-detection` | 0 | 0 |  |