import pandas as pd

file_path = r"data/raw/NY.GDP.MKTP.KD.ZG.csv"

df = pd.read_csv(
    file_path,
    skiprows=4
)

kenya = df[df["Country Code"] == "KEN"]

print(kenya)

years = [str(year) for year in range(1960, 2026)]

gdp = kenya[years].T

gdp.columns = ["GDP_Growth"]

gdp.index.name = "Year"

gdp.reset_index(inplace=True)

print(gdp.head())

print(gdp.tail())
gdp.to_csv(
    "data/processed/gdp_growth.csv",
    index=False
)

print("GDP dataset saved successfully.")