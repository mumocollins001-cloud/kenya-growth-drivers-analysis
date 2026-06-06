import pandas as pd
import statsmodels.api as sm

df = pd.read_csv("data/processed/master_dataset.csv")

df = df.dropna()

X = df[
    [
        "Investment",
        "Gov_Expenditure",
        "Inflation",
        "Unemployment"
    ]
]

X = sm.add_constant(X)

y = df["GDP_Growth"]

model = sm.OLS(y, X).fit()

print(model.summary())