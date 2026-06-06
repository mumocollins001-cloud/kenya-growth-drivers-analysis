import pandas as pd

master = pd.read_csv("data/processed/master_dataset.csv")

unemployment = pd.read_csv(
    "data/processed/unemployment.csv"
)

master = master.merge(
    unemployment,
    on="Year",
    how="left"
)

print(master.head())

print(master.tail())

master.to_csv(
    "data/processed/master_dataset.csv",
    index=False
)

print("Unemployment merged successfully.")