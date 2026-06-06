# Kenya Growth Drivers Analysis

## Executive Summary

This study investigates the factors associated with economic growth in Kenya using World Bank macroeconomic data. The analysis focuses on GDP growth, investment, inflation, government expenditure, and unemployment.

Using correlation analysis, regression modeling, and hypothesis testing, the study finds that investment has a positive and statistically significant relationship with GDP growth, while inflation has a negative and statistically significant relationship with GDP growth.

The final regression model explains approximately 32% of the variation in Kenya's GDP growth and suggests that increasing investment while maintaining inflation stability may contribute to stronger economic performance.

## 1. Introduction

Economic growth is one of the most important indicators of a country's development. Policymakers continually seek to identify the factors that promote sustainable growth and improve living standards.

This study examines the relationship between GDP growth and selected macroeconomic variables in Kenya. Specifically, the analysis investigates whether investment, inflation, government expenditure, and unemployment are associated with changes in economic growth.

The objective is to identify which variables have the strongest statistical relationship with GDP growth and provide evidence-based insights for economic decision-making.

## 2. Research Questions

This study seeks to answer the following questions:

1. Does investment significantly affect GDP growth in Kenya?

2. Does inflation significantly affect GDP growth in Kenya?

3. Does government expenditure significantly affect GDP growth in Kenya?

4. Does unemployment significantly affect GDP growth in Kenya?

5. Which variables provide the strongest explanation for variations in Kenya's economic growth?

## 3. Data Sources

The data used in this analysis was obtained from the World Bank World Development Indicators database.

Variables included:

* GDP Growth (annual %)
* Gross Capital Formation / Investment (% of GDP)
* Government Final Consumption Expenditure (% of GDP)
* Inflation, Consumer Prices (annual %)
* Unemployment Rate (% of labor force)

The study focuses exclusively on Kenya and covers the years for which data was available across the selected indicators.

## 4. Methodology

The analysis was conducted using Python and several statistical techniques.

The process involved:

1. Downloading macroeconomic indicators from the World Bank.
2. Extracting Kenya-specific observations.
3. Cleaning and transforming the datasets.
4. Merging the variables into a single master dataset.
5. Performing correlation analysis.
6. Building multiple linear regression models using Ordinary Least Squares (OLS).
7. Testing statistical significance using p-values and hypothesis testing.
8. Evaluating multicollinearity using Variance Inflation Factors (VIF).
9. Producing visualizations to explore relationships among variables.

The primary dependent variable was GDP Growth (annual %).

## 5. Exploratory Data Analysis

Correlation analysis revealed the following relationships with GDP Growth:

| Variable               | Correlation with GDP Growth |
| ---------------------- | --------------------------- |
| Investment             | 0.250                       |
| Government Expenditure | 0.061                       |
| Inflation              | -0.264                      |
| Unemployment           | 0.172                       |

Investment displayed a positive relationship with GDP growth, while inflation displayed a negative relationship.

Government expenditure and unemployment showed relatively weak correlations with GDP growth.

Scatterplots and trend visualizations supported these findings by illustrating a mild positive association between investment and growth and a negative association between inflation and growth.

## 6. Regression Analysis

An Ordinary Least Squares (OLS) regression model was estimated to examine the relationship between GDP growth and the explanatory variables.

The final reduced model was:

GDP Growth = -0.973 + 0.310(Investment) - 0.109(Inflation)

Model Statistics:

* R-squared = 0.319
* Adjusted R-squared = 0.276
* F-statistic p-value = 0.00257

The model explains approximately 31.9% of the variation in Kenya's GDP growth.

Investment was found to have a positive coefficient, while inflation had a negative coefficient.

## 7. Hypothesis Testing

### Investment

Null Hypothesis (H₀):
Investment has no significant relationship with GDP growth.

Alternative Hypothesis (H₁):
Investment has a significant relationship with GDP growth.

Result:

* Coefficient = 0.310
* P-value = 0.036

Decision:

Reject H₀.

Conclusion:

Investment is statistically significant at the 5% significance level.

### Inflation

Null Hypothesis (H₀):
Inflation has no significant relationship with GDP growth.

Alternative Hypothesis (H₁):
Inflation has a significant relationship with GDP growth.

Result:

* Coefficient = -0.109
* P-value = 0.007

Decision:

Reject H₀.

Conclusion:

Inflation is statistically significant at the 5% significance level.

## 8. Key Findings

The analysis produced four major findings:

1. Investment has a positive and statistically significant relationship with GDP growth.

2. Inflation has a negative and statistically significant relationship with GDP growth.

3. Government expenditure was not statistically significant in the regression model.

4. Unemployment was not statistically significant in the regression model.

Overall, investment and inflation emerged as the most important variables explaining economic growth within the scope of this study.

## 9. Policy Recommendations

Based on the findings:

1. Policies that encourage investment should be prioritized, as investment is positively associated with economic growth.

2. Inflation should be maintained at stable and manageable levels to support economic expansion.

3. Further research should investigate sector-specific investments to identify the areas that contribute most to growth.

4. Additional macroeconomic variables may be incorporated in future studies to improve explanatory power.

## 10. Limitations

This study has several limitations:

1. Only a small number of macroeconomic variables were included.

2. The analysis focuses exclusively on Kenya.

3. Regression analysis identifies statistical associations and does not prove causation.

4. Data availability limited the number of observations for some variables.

Future studies may incorporate additional economic, demographic, and institutional variables.

## 11. Conclusion

This study examined the drivers of economic growth in Kenya using World Bank data and econometric techniques.

The results indicate that investment is positively associated with GDP growth, while inflation is negatively associated with GDP growth.

The final regression model suggests that policies aimed at increasing productive investment and maintaining price stability may contribute to stronger economic performance.

The project demonstrates the application of data cleaning, exploratory data analysis, econometric modeling, hypothesis testing, and visualization techniques using Python.

