import pandas as pd

df = pd.read_csv(
    "data/processed/master_dataset.csv"
)

df = df.dropna()

correlation = df["GDP_Growth"].corr(
    df["Gov_Expenditure"]
)

print("Correlation =", correlation)