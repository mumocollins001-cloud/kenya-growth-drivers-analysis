import pandas as pd
import matplotlib.pyplot as plt

# Load data

df = pd.read_csv(
    "data/processed/master_dataset.csv"
)

# -------------------------
# GDP Growth Trend
# -------------------------

plt.figure(figsize=(10,5))

plt.plot(
    df["Year"],
    df["GDP_Growth"]
)

plt.title("Kenya GDP Growth Over Time")
plt.xlabel("Year")
plt.ylabel("GDP Growth (%)")

plt.savefig(
    "visuals/time_series/gdp_growth_trend.png"
)

plt.close()

# -------------------------
# Investment Trend
# -------------------------

plt.figure(figsize=(10,5))

plt.plot(
    df["Year"],
    df["Investment"]
)

plt.title("Kenya Investment Over Time")
plt.xlabel("Year")
plt.ylabel("Investment (% of GDP)")

plt.savefig(
    "visuals/time_series/investment_trend.png"
)

plt.close()

# -------------------------
# Inflation Trend
# -------------------------

plt.figure(figsize=(10,5))

plt.plot(
    df["Year"],
    df["Inflation"]
)

plt.title("Kenya Inflation Over Time")
plt.xlabel("Year")
plt.ylabel("Inflation (%)")

plt.savefig(
    "visuals/time_series/inflation_trend.png"
)

plt.close()

# -------------------------
# Government Expenditure Trend
# -------------------------

plt.figure(figsize=(10,5))

plt.plot(
    df["Year"],
    df["Gov_Expenditure"]
)

plt.title("Kenya Government Expenditure Over Time")
plt.xlabel("Year")
plt.ylabel("Government Expenditure (% of GDP)")

plt.savefig(
    "visuals/time_series/gov_expenditure_trend.png"
)

plt.close()

# -------------------------
# Unemployment Trend
# -------------------------

plt.figure(figsize=(10,5))

plt.plot(
    df["Year"],
    df["Unemployment"]
)

plt.title("Kenya Unemployment Over Time")
plt.xlabel("Year")
plt.ylabel("Unemployment (%)")

plt.savefig(
    "visuals/time_series/unemployment_trend.png"
)

plt.close()

print("Time series charts created successfully.")