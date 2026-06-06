import pandas as pd

df = pd.read_csv("data/processed/master_dataset.csv")

print(df.sort_values("GDP_Growth").head(5))

print("\nHighest Growth Years\n")

print(df.sort_values("GDP_Growth", ascending=False).head(5))