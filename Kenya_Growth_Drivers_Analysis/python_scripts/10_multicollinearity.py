import pandas as pd
from statsmodels.stats.outliers_influence import variance_inflation_factor

df = pd.read_csv("data/processed/master_dataset.csv")

df = df[[
    "Investment",
    "Gov_Expenditure",
    "Inflation"
]].dropna()

vif_data = pd.DataFrame()

vif_data["Variable"] = df.columns

vif_data["VIF"] = [
    variance_inflation_factor(df.values, i)
    for i in range(df.shape[1])
]

print(vif_data)