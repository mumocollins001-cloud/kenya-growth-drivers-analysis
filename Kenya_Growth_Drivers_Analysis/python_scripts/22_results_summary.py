import pandas as pd

results = pd.DataFrame({
    "Variable": [
        "Investment",
        "Inflation",
        "Government Expenditure",
        "Unemployment"
    ],
    "Expected Effect": [
        "Positive",
        "Negative",
        "Positive",
        "Negative"
    ],
    "Observed Effect": [
        "Positive",
        "Negative",
        "Positive",
        "Positive"
    ],
    "Statistically Significant": [
        "Yes",
        "Yes",
        "No",
        "No"
    ]
})

results.to_csv(
    "data/processed/results_summary.csv",
    index=False
)

print(results)
print("\nResults summary saved.")