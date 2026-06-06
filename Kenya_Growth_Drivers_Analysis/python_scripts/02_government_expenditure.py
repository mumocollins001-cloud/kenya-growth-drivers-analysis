import pandas as pd

file_path = r"data/raw/NE.CON.GOVT.ZS_DS2.csv"

df = pd.read_csv(
    file_path,
    skiprows=4
)

kenya = df[df["Country Code"] == "KEN"]

years = [str(year) for year in range(1960, 2026)]

gov = kenya[years].T

gov.columns = ["Gov_Expenditure"]

gov.index.name = "Year"

gov.reset_index(inplace=True)

gov.to_csv(
    "data/processed/government_expenditure.csv",
    index=False
)

print(gov.head())

print("Government expenditure dataset saved.")