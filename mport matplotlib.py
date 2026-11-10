mport matplotlib.pyplot as plt
from sklearn.datasets import fetch_california_housing

# 1. Load Data
df = fetch_california_housing(as_frame=True).frame

# 2. Histograms (Pandas native)
df.hist(bins=30, figsize=(15, 10))
plt.show()

# 3. Box Plots (Pandas native with grid layout)
df.plot(kind='box', subplots=True, layout=(3, 3), figsize=(15, 10))
plt.show()

# 4. Identify outliers (Pandas vectorized math)
Q1 = df.quantile(0.25)
Q3 = df.quantile(0.75)
IQR = Q3 - Q1

# Calculate bounds and count outliers for all columns at once
outliers = ((df < (Q1 - 1.5 * IQR)) | (df > (Q3 + 1.5 * IQR))).sum()
print("Outliers Detection:\n", outliers)

# 5. Dataset Summary
print("\nDataset Summary:\n", df.describe())