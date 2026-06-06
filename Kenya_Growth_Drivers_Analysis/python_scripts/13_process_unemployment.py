import pandas as pd

df = pd.read_csv(
    "data/raw/SL.UEM.TOTL.ZS_DS2.csv",
    skiprows=4
)

kenya = df[df["Country Code"] == "KEN"]

years = [str(year) for year in range(1960, 2026)]

unemployment = kenya[years].T

unemployment.columns = ["Unemployment"]

unemployment = unemployment.reset_index()

unemployment.columns = ["Year", "Unemployment"]

unemployment["Year"] = unemployment["Year"].astype(int)

print(unemployment.head())
print(unemployment.tail())

unemployment.to_csv(
    "data/processed/unemployment.csv",
    index=False
)

print("Unemployment dataset saved successfully.")