import pandas as pd

master = pd.read_csv("data/processed/master_dataset.csv")

inflation = pd.read_csv("data/processed/inflation.csv")

master = pd.merge(
    master,
    inflation,
    on="Year",
    how="left"
)

print(master.head())

print(master.tail())

master.to_csv(
    "data/processed/master_dataset.csv",
    index=False
)

print("Inflation merged successfully.")