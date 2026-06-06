import pandas as pd
import statsmodels.api as sm

# Load data

df = pd.read_csv(
    "data/processed/master_dataset.csv"
)

# Keep required variables

df = df[
    [
        "GDP_Growth",
        "Investment",
        "Inflation"
    ]
].dropna()

# Define variables

X = df[
    [
        "Investment",
        "Inflation"
    ]
]

X = sm.add_constant(X)

y = df["GDP_Growth"]

# Fit model

model = sm.OLS(y, X).fit()

print(model.summary())

print("\n")
print("HYPOTHESIS TEST RESULTS")
print("-" * 40)

investment_p = model.pvalues["Investment"]
inflation_p = model.pvalues["Inflation"]

# Investment

print("\nInvestment")

if investment_p < 0.05:
    print("Reject H0")
    print("Investment significantly affects GDP Growth")
else:
    print("Fail to Reject H0")
    print("Investment does not significantly affect GDP Growth")

# Inflation

print("\nInflation")

if inflation_p < 0.05:
    print("Reject H0")
    print("Inflation significantly affects GDP Growth")
else:
    print("Fail to Reject H0")
    print("Inflation does not significantly affect GDP Growth")