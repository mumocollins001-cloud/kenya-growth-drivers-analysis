import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

df = pd.read_csv("data/processed/master_dataset.csv")

df = df.dropna(subset=["GDP_Growth", "Investment"])

x = df["Investment"]
y = df["GDP_Growth"]

plt.figure(figsize=(8,5))

plt.scatter(x, y)

m, b = np.polyfit(x, y, 1)

plt.plot(
    x,
    m*x + b
)

plt.xlabel("Investment (% of GDP)")
plt.ylabel("GDP Growth (%)")
plt.title("Investment and Economic Growth in Kenya")

plt.show()