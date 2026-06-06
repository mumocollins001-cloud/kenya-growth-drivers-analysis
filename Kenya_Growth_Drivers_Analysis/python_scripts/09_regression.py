import pandas as pd
import statsmodels.api as sm

# Load master dataset
df = pd.read_csv("data/processed/master_dataset.csv")

# Keep only complete observations
df = df.dropna()

# Dependent variable
y = df["GDP_Growth"]

# Independent variables
X = df[
    [
        "Investment",
        "Gov_Expenditure",
        "Inflation"
    ]
]

# Add constant term
X = sm.add_constant(X)

# Run regression
model = sm.OLS(y, X).fit()

# Print results
print(model.summary())