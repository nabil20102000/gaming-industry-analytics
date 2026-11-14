# Steam Market Analysis
### A Data Analytics Project Exploring the Steam Gaming Market

## Project Overview

This independent data analytics project investigates the Steam gaming market using publicly available aggregate datasets covering a selected group of 10,000 games ranked by estimated ownership.

The project examines game pricing, genre representation, estimated ownership concentration, release-year pricing trends and genre-level review indicators.

The objective is to demonstrate practical data analytics skills through data collection, cleaning, exploratory analysis, visualisation and interactive dashboard development.

## Research Objectives

- Analyse the distribution of Steam games across price categories.
- Identify the most frequently represented game genres.
- Investigate estimated ownership concentration.
- Explore historical game pricing and free-to-play trends.
- Compare genre-level review indicators.
- Communicate findings through interactive Power BI dashboards.

## Tools and Technologies

| Tool | Application |
|---|---|
| Microsoft Excel | Data preparation, Power Query, formulas and charts |
| Python | Data cleaning, exploratory analysis and visualisation |
| Pandas | Data manipulation and analysis |
| Matplotlib | Python visualisations |
| Power BI | Interactive dashboard development |
| DAX | KPI calculations and analytical measures |
| GitHub | Version control and project documentation |
| Google Colab | Cloud-based Python development |

## Data Sources

Primary source: [Crawlora – Steam Catalog Dataset](https://github.com/Crawlora-org/steam-catalog-data)

The project uses five aggregate CSV datasets:

1. `genres.csv`
2. `price-tiers.csv`
3. `ownership-concentration.csv`
4. `pricing-by-year.csv`
5. `review-by-genre.csv`

The source dataset covers the top 10,000 Steam games ranked by estimated ownership. It does not represent the entire Steam catalogue.

## Project Workflow

### 1. Data Collection and Preparation
- Collected five CSV datasets.
- Retained original files in the raw data directory.
- Inspected missing values, duplicates and data types.
- Validated numerical ranges and summary-table consistency.
- Exported cleaned datasets.

### 2. Excel Analysis
- Imported data using Power Query.
- Created structured Excel tables.
- Calculated category percentages and genre rankings.
- Applied custom sorting.
- Developed initial charts.

### 3. Python Exploratory Data Analysis
- Used Pandas for data inspection and analysis.
- Calculated descriptive statistics.
- Generated visualisations using Matplotlib.
- Investigated market patterns across the five datasets.

### 4. Power BI Dashboard
Developed a three-page dashboard using DAX measures and interactive visualisations.

The report contains:

- Steam Market Overview
- Pricing Trends and Market Evolution
- Genre and Player Reception

## Key Findings

### Pricing Distribution

The downloaded price-tier dataset contains 10,000 games.

| Price Category | Games | Share |
|---|---:|---:|
| Free | 2,007 | 20.07% |
| Under $5 | 3,528 | 35.28% |
| $5–$15 | 2,627 | 26.27% |
| $15–$30 | 1,429 | 14.29% |
| $30–$60 | 382 | 3.82% |
| Over $60 | 27 | 0.27% |

### Genre Representation

The most frequently assigned genres are:

| Genre | Assignments |
|---|---:|
| Indie | 5,940 |
| Action | 4,797 |
| Adventure | 4,091 |

These three categories account for approximately 52.53% of all genre assignments.

### Ownership Concentration

The top 25% of games account for 80.50% of estimated ownership within the analysed dataset.

### Pricing Trends

The annual pricing analysis includes 9,928 titles.

For 2024, the median paid price was $9.99 and the mean paid price was $14.51.

The 2025 and 2026 observations have smaller samples, and 2026 represents a partial-year observation.

### Genre and Review Indicators

The review-by-genre dataset contains 19 categories. Some genres have median positive-review ratios of 100%, while the Free To Play genre category reports 77%.

## Power BI Dashboard

The final dashboard contains three analytical pages.

### Page 1 – Steam Market Overview

![Top 10 Steam Genres](outputs/charts/genre_distribution_top10.png)

![Steam Price Distribution](outputs/charts/price_tier_distribution.png)

![Ownership Concentration](outputs/charts/ownership_concentration.png)

### Page 2 – Pricing Trends

![Pricing Trends](outputs/charts/pricing_trends.png)

![Free-to-Play Trends](outputs/charts/free_to_play_trends.png)

![Release-Year Distribution](outputs/charts/releases_by_year.png)

### Page 3 – Genre and Player Reception

![Review Scores by Genre](outputs/charts/review_scores_by_genre.png)

![Free-to-Play Share by Genre](outputs/charts/free_share_by_genre.png)

![Free-to-Play Share vs Review Score](outputs/charts/free_share_vs_review_score.png)

## Data Quality and Limitations

- The dataset represents the top 10,000 games by estimated ownership, not the entire Steam catalogue.
- Ownership values are estimates rather than verified sales figures.
- Games can belong to multiple genres, so genre counts represent assignments rather than unique games.
- The pricing-by-year dataset contains 9,928 titles rather than 10,000.
- The review-by-genre dataset excludes the Violent category.
- The recent release-year observations have smaller sample sizes.
- The exact version of the downloaded CSV files requires confirmation against the source repository.
- The scatter analysis is exploratory and does not establish causation.

## Repository Structure

```text
Project_1_Steam_Market_Analysis/
│
├── data/
│   ├── raw/
│   └── cleaned/
│
├── excel/
├── python/
├── powerbi/
├── outputs/
│   └── charts/
├── report/
├── sources/
└── README.md
```

## Reproducibility

The project includes:

- Original and cleaned CSV datasets.
- Excel analysis workbook.
- Python EDA notebook and scripts.
- Power BI dashboard file.
- Exported visualisations.
- Research report and data-quality documentation.

Python analysis can be reproduced using Google Colab or a compatible local Python environment with the required libraries installed.

## References and Attribution

Crawlora (2026). *Steam Catalog Dataset – State of Steam 2026*.

https://github.com/Crawlora-org/steam-catalog-data

Dataset licence: Creative Commons Attribution 4.0 International (CC BY 4.0).

This project is an independent educational and portfolio project. All analysis, transformations, visualisations and interpretations were developed for this project using the referenced data source.