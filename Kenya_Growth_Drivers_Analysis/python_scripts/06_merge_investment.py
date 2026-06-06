import pandas as pd

master = pd.read_csv(
    "data/processed/master_dataset.csv"
)

investment = pd.read_csv(
    "data/processed/investment.csv"
)

master = master.merge(
    investment,
    on="Year",
    how="left"
)

print(master.head())

print(master.tail())

master.to_csv(
    "data/processed/master_dataset.csv",
    index=False
)

print("Investment merged successfully.")