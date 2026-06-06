# Kenya Growth Drivers Analysis

## Project Overview

This project investigates the key macroeconomic factors associated with economic growth in Kenya using World Bank data.

The objective is to identify which variables have the strongest relationship with GDP growth and evaluate their statistical significance using econometric techniques.

---

## Data Source

World Bank World Development Indicators (WDI)

Variables used:

* GDP Growth (%)
* Investment (% of GDP)
* Inflation (%)
* Government Expenditure (% of GDP)
* Unemployment (%)

Period Covered:

1960–2024

---

## Methodology

1. Data Collection
2. Data Cleaning
3. Data Transformation
4. Dataset Merging
5. Correlation Analysis
6. OLS Regression
7. Model Diagnostics
8. Visualization

---

## Key Findings

### Investment

Positive and statistically significant.

A 1 percentage-point increase in investment is associated with approximately a 0.31 percentage-point increase in GDP growth.

### Inflation

Negative and statistically significant.

A 1 percentage-point increase in inflation is associated with approximately a 0.11 percentage-point decrease in GDP growth.

### Government Expenditure

Not statistically significant.

### Unemployment

Not statistically significant.

---

## Final Regression Model

GDP Growth = -0.973 + 0.310(Investment) - 0.109(Inflation)

---

## Technologies Used

* Python
* Pandas
* NumPy
* Matplotlib
* Statsmodels

---

## Author

Joseph Mumo
Aspiring Data Analyst | Statistics Graduate
