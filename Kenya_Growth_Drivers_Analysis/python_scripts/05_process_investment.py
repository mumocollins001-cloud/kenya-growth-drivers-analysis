import pandas as pd

file_path = r"data/raw/NE.GDI.TOTL.ZS_DS2.csv"

df = pd.read_csv(file_path, skiprows=4)

kenya = df[df["Country Code"] == "KEN"]

years = [str(year) for year in range(1960, 2026)]

investment = kenya[years].T

investment.columns = ["Investment"]

investment.index.name = "Year"

investment.reset_index(inplace=True)

investment["Year"] = investment["Year"].astype(int)

print(investment.head())

print(investment.tail())

investment.to_csv(
    "data/processed/investment.csv",
    index=False
)

print("Investment dataset saved successfully.")