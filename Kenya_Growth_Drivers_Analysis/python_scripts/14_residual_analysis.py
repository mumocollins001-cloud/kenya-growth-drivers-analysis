import pandas as pd
import statsmodels.api as sm
import matplotlib.pyplot as plt

df = pd.read_csv("data/processed/master_dataset.csv")

df = df.dropna()

X = df[["Investment", "Gov_Expenditure", "Inflation"]]
y = df["GDP_Growth"]

X = sm.add_constant(X)

model = sm.OLS(y, X).fit()

df["Predicted"] = model.predict(X)

df["Residuals"] = y - df["Predicted"]

print(df[["Year", "GDP_Growth", "Predicted", "Residuals"]].head())

plt.scatter(df["Predicted"], df["Residuals"])

plt.axhline(y=0)

plt.xlabel("Predicted GDP Growth")
plt.ylabel("Residuals")
plt.title("Residual Plot")

plt.show()