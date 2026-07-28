# Layout model benchmark — wjcpdmrspdzt.pdf

Canonical input: `layout_bench/page.png` (2480x1850). 20 models tested. Each folder has `overlay.png` + `detections.json`.

| Model | #Regions | #Classes | Notes |
|---|--:|--:|---|
| `rapidlayout-pp_doc_layoutv2` | 56 | 10 | text:33, paragraph_title:13, footer:3, table:1, display_formula:1 |
| `rapidlayout-pp_doc_layoutv3` | 55 | 10 | text:32, paragraph_title:12, footer:3, figure_title:2, table:1 |
| `rapidlayout-doclayout_docsynth` | 57 | 8 | Text:19, List-item:16, Section-header:12, Picture:3, Page-footer:3 |
| `rapidlayout-doclayout_d4la` | 53 | 11 | ListText:16, ParaText:13, ParaTitle:7, DocTitle:4, Figure:3 |
| `rapidlayout-doclayout_docstructbench` | 49 | 8 | plain text:26, title:12, abandon:4, figure:2, isolate_formula:2 |
| `docling-egret-xlarge` | 65 | 9 | Text:24, List-item:17, Section-header:12, Picture:4, Page-footer:3 |
| `docling-heron-101` | 64 | 9 | Text:23, List-item:18, Section-header:12, Picture:3, Page-footer:3 |
| `docling-egret-large` | 63 | 10 | Text:20, List-item:17, Section-header:13, Picture:3, Page-footer:3 |
| `docling-egret-medium` | 63 | 9 | Text:24, List-item:15, Section-header:13, Picture:3, Page-footer:3 |
| `docling-heron` | 63 | 9 | text:20, list_item:17, section_header:14, picture:3, page_footer:3 |
| `aryn-deformable-detr-DocLayNet` | 53 | 7 | Text:18, List-item:15, Section-header:12, Picture:3, Page-footer:3 |
| `rapidlayout-yolov8n_layout_report` | 56 | 7 | Text:38, Title:9, Figure:3, Footer:3, Table:1 |
| `unstructured-yolox` | 55 | 8 | Text:27, Section-header:12, List-item:6, Page-footer:3, Picture:3 |
| `rapidlayout-yolov8n_layout_general6` | 48 | 5 | Text:31, Title:12, Figure:3, Table:1, Caption:1 |
| `rapidlayout-yolov8n_layout_paper` | 47 | 8 | Text:27, Title:8, Figure:4, Reference:2, Header:2 |
| `rapidlayout-yolov8n_layout_publaynet` | 18 | 2 | Text:11, Title:7 |
| `rapidlayout-pp_layout_cdla` | 35 | 8 | text:17, title:6, footer:3, header:2, figure:2 |
| `rapidlayout-pp_layout_publaynet` | 35 | 3 | text:22, title:12, list:1 |
| `rapidlayout-pp_layout_table` | 3 | 1 | table:3 |
| `table-transformer-detection` | 1 | 1 | table:1 |