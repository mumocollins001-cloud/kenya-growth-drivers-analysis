import pandas as pd

gdp = pd.read_csv(
    "data/processed/gdp_growth.csv"
)

gov = pd.read_csv(
    "data/processed/government_expenditure.csv"
)

master = pd.merge(
    gdp,
    gov,
    on="Year",
    how="inner"
)

print(master.head())

print(master.tail())

master.to_csv(
    "data/processed/master_dataset.csv",
    index=False
)

print("Master dataset created successfully.")