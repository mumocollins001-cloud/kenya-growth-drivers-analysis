import pandas as pd

file_path = r"data/raw/FP.CPI.TOTL.ZG_DS2.csv"

df = pd.read_csv(file_path, skiprows=4)

kenya = df[df["Country Code"] == "KEN"]

print(kenya)

years = [str(year) for year in range(1960, 2026)]

inflation = kenya[years].T

inflation.reset_index(inplace=True)

inflation.columns = ["Year", "Inflation"]

inflation["Year"] = inflation["Year"].astype(int)

print(inflation.head())

print(inflation.tail())

inflation.to_csv(
    "data/processed/inflation.csv",
    index=False
)

print("Inflation dataset saved successfully.")