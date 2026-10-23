# Customer Shopping Behavior Analysis

<div align="center">

<a href="https://app.powerbi.com/groups/7c691d28-fc18-48d1-8397-29c2f00ef4c6/reports/be15c795-5fd2-47b5-b553-73db10cfb509?ctid=178c56e2-1838-460d-9e6e-9acdebb75afc&pbi_source=linkShare&bookmarkGuid=dc71acda-b354-4212-b123-60f301a838d9">
  <img src="https://img.shields.io/badge/Power%20BI-Live%20Dashboard-F2C811?style=for-the-badge&logo=powerbi&logoColor=black" alt="Power BI Live Dashboard">
</a>
<a href="https://www.python.org/">
  <img src="https://img.shields.io/badge/Python-Data%20Analysis-3776AB?style=for-the-badge&logo=python&logoColor=white" alt="Python Data Analysis">
</a>
<a href="https://www.microsoft.com/en-us/microsoft-365/excel">
  <img src="https://img.shields.io/badge/SQL-Analytics-4479A1?style=for-the-badge&logo=postgresql&logoColor=white" alt="SQL Analytics">
</a>

<br>
<br>

<img src="https://readme-typing-svg.demolab.com?font=Inter&weight=700&size=25&pause=1100&color=F2C811&center=true&vCenter=true&width=700&lines=Turning+shopping+data+into+business+insights;Exploring+customers%2C+products%2C+revenue%2C+and+retention;Designed+with+Python%2C+SQL%2C+and+Power+BI" alt="Animated project description">

<br>

**An end-to-end customer shopping behavior analysis project**

<br>

<a href="https://app.powerbi.com/groups/7c691d28-fc18-48d1-8397-29c2f00ef4c6/reports/be15c795-5fd2-47b5-b553-73db10cfb509?ctid=178c56e2-1838-460d-9e6e-9acdebb75afc&pbi_source=linkShare&bookmarkGuid=dc71acda-b354-4212-b123-60f301a838d9">
  <img src="https://img.shields.io/badge/%E2%96%B6%20View%20Live%20Dashboard-Open%20in%20Power%20BI-F2C811?style=for-the-badge&logo=powerbi&logoColor=black" alt="View live Power BI dashboard">
</a>

</div>

## Overview

This project explores customer purchase patterns from **3,900 shopping records**. It combines data cleaning and exploratory analysis in Python, business-focused SQL queries, and an interactive Power BI dashboard to answer practical retail questions.

The analysis focuses on:

- Customer demographics and age groups
- Revenue by gender and customer segment
- Product ratings and purchasing trends
- Subscription behavior and repeat purchases
- Discount usage and promotional activity
- Shipping preferences and purchase frequency

## Dashboard

The Power BI report is included in [`Customer_Shooping Analysis.pbix`](./Customer_Shooping%20Analysis.pbix).

> **Live dashboard:** Open the deployed report with the **View Live Dashboard** button above. Access may require permission in the Power BI workspace.

### Dashboard preview

![Power BI dashboard preview](https://placehold.co/1200x675/111827/F2C811?text=Add+Power+BI+Dashboard+Screenshot)

To add a real preview, export a dashboard page as an image and replace the image URL above with its repository path, for example `./assets/dashboard-preview.png`.

## Project workflow

```mermaid
flowchart LR
    A[(Customer shopping data)] --> B[Python cleaning]
    B --> C[Exploratory analysis]
    A --> D[SQL business questions]
    C --> E[Power BI model]
    D --> E
    E --> F[Interactive dashboard]
```

## Key business questions

The SQL analysis in [`project.sql`](./project.sql) investigates:

1. How does revenue compare between male and female customers?
2. Which discounted customers still spend above average?
3. Which products have the highest average review ratings?
4. How do standard and express shipping customers compare?
5. Do subscribers spend more than non-subscribers?
6. Which products have the highest discount-purchase rate?
7. How many customers are new, returning, or loyal?
8. What are the three most purchased products in each category?
9. Are repeat buyers more likely to subscribe?
10. Which age groups contribute the most revenue?

## Repository contents

| File | Description |
| --- | --- |
| [`customer_shopping_behavior.csv`](./customer_shopping_behavior.csv) | Source customer shopping dataset |
| [`shopping.ipynb`](./shopping.ipynb) | Python cleaning and exploratory analysis |
| [`project.sql`](./project.sql) | SQL business analysis queries |
| [`Customer_Shooping Analysis.pbix`](./Customer_Shooping%20Analysis.pbix) | Power BI report |
| [`Customer Shopping Behavior Analysis.pdf`](./Customer%20Shopping%20Behavior%20Analysis.pdf) | Exported analysis/report document |
| [`read.txt`](./read.txt) | Analysis notes and transformation explanations |

## Methods and tools

| Area | Tools |
| --- | --- |
| Data preparation | Python, pandas, missing-value imputation |
| Customer segmentation | Quantile-based age groups and purchase-history segments |
| Business analysis | SQL aggregations, CTEs, window functions |
| Reporting | Microsoft Power BI |

## Getting started

### Python notebook

1. Clone this repository.
2. Open [`shopping.ipynb`](./shopping.ipynb) in Jupyter Notebook or VS Code.
3. Update the dataset path in the notebook if your local folder differs.
4. Run the cells to reproduce the cleaning and exploratory analysis.

### Power BI report

Open [`Customer_Shooping Analysis.pbix`](./Customer_Shooping%20Analysis.pbix) in Power BI Desktop. If you publish an updated report, update the live URL in this README.

## Author

**Saikat Dash**

If this analysis is useful, consider leaving a ⭐ on the repository.
