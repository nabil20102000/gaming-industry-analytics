
# Steam Market Analysis
## Data Quality Assessment

### 1. Dataset Overview

Five aggregate datasets were collected from the
Crawlora Steam Catalog Dataset (September 2026 snapshot).

Total rows inspected: 70

### 2. Initial Quality Checks

- Missing values: 0
- Duplicate rows: 0
- Duplicate key values: 0
- Percentage range violations: 0

### 3. Identified Limitations

**Genre Coverage**

The genre dataset contains 20 categories,
while the review-by-genre dataset contains 19.

The Violent category contains 19 games but
has no corresponding review summary.

**Release-Year Coverage**

Price-tier data totals 10,000 games.
Pricing-by-year data totals 9,928 titles.

The supplementary release-years dataset
includes 23 titles from 1997–2005 and
totals 9,951, leaving 49 titles unreconciled.

These discrepancies are documented rather
than artificially corrected.

### 4. Cleaning Decisions

- Original raw datasets retained unchanged.
- No records deleted.
- No missing values artificially imputed.
- Percentage values retained as decimals.
- Dataset aggregation differences documented.

### 5. Research Limitations

The dataset covers the top 10,000 Steam games
ranked by estimated ownership, not the complete
Steam catalogue.

Steam ownership figures are estimates.

Recent release-year observations have smaller
sample sizes and require cautious interpretation.

### 6. Source

Crawlora (2026).
Steam Catalog Dataset – State of Steam 2026.

https://github.com/Crawlora-org/steam-catalog-data

License: CC BY 4.0.
