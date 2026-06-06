import pandas as pd
import statsmodels.api as sm
import matplotlib.pyplot as plt

# Load data
df = pd.read_csv("data/processed/master_dataset.csv")

# Keep only rows with complete data
df = df.dropna(subset=["GDP_Growth", "Investment", "Inflation"])

# Independent variables
X = df[["Investment", "Inflation"]]

# Add constant
X = sm.add_constant(X)

# Dependent variable
y = df["GDP_Growth"]

# Fit model
model = sm.OLS(y, X).fit()

# Generate predictions
df["Predicted_GDP_Growth"] = model.predict(X)

# Plot
plt.figure(figsize=(8,5))

plt.scatter(
    df["GDP_Growth"],
    df["Predicted_GDP_Growth"]
)

# Perfect prediction line
min_val = min(df["GDP_Growth"].min(),
              df["Predicted_GDP_Growth"].min())

max_val = max(df["GDP_Growth"].max(),
              df["Predicted_GDP_Growth"].max())

plt.plot(
    [min_val, max_val],
    [min_val, max_val]
)

plt.xlabel("Actual GDP Growth")
plt.ylabel("Predicted GDP Growth")
plt.title("Actual vs Predicted GDP Growth")

plt.show()