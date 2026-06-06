import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import statsmodels.api as sm

# Load data
df = pd.read_csv("data/processed/master_dataset.csv")

# Remove missing values
df = df.dropna()

# -----------------------------
# 1. Investment vs GDP Growth
# -----------------------------

plt.figure(figsize=(8,5))
plt.scatter(df["Investment"], df["GDP_Growth"])

plt.xlabel("Investment (% of GDP)")
plt.ylabel("GDP Growth (%)")
plt.title("Investment vs GDP Growth")

plt.savefig(
    "visuals/scatterplots/investment_vs_growth.png"
)

plt.close()

# -----------------------------
# 2. Inflation vs GDP Growth
# -----------------------------

plt.figure(figsize=(8,5))
plt.scatter(df["Inflation"], df["GDP_Growth"])

plt.xlabel("Inflation (%)")
plt.ylabel("GDP Growth (%)")
plt.title("Inflation vs GDP Growth")

plt.savefig(
    "visuals/scatterplots/inflation_vs_growth.png"
)

plt.close()

# -----------------------------
# 3. Correlation Heatmap
# -----------------------------

corr = df[
    [
        "GDP_Growth",
        "Investment",
        "Gov_Expenditure",
        "Inflation",
        "Unemployment"
    ]
].corr()

plt.figure(figsize=(8,6))

sns.heatmap(
    corr,
    annot=True,
    cmap="coolwarm"
)

plt.title("Correlation Matrix")

plt.savefig(
    "visuals/heatmaps/correlation_heatmap.png"
)

plt.close()
print("All visualizations generated successfully.")