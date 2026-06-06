import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("data/processed/master_dataset.csv")

# Keep relevant variables
corr_data = df[
    [
        "GDP_Growth",
        "Investment",
        "Gov_Expenditure",
        "Inflation",
        "Unemployment"
    ]
]

corr_matrix = corr_data.corr()

print(corr_matrix)

plt.figure(figsize=(8,6))

plt.imshow(corr_matrix)

plt.colorbar()

plt.xticks(
    range(len(corr_matrix.columns)),
    corr_matrix.columns,
    rotation=45
)

plt.yticks(
    range(len(corr_matrix.columns)),
    corr_matrix.columns
)

plt.title("Correlation Heatmap")

plt.tight_layout()

plt.show()