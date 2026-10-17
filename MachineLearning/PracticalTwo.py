# Practical 2: Data Visualization
# Aim: Load a dataset, calculate descriptive summary statistics,
# create visualizations, and identify potential features and target variables.

# Setup commands (run these in Terminal, not inside this file):
# python -m pip install numpy pandas matplotlib seaborn scikit-learn

import numpy as np
import pandas as pd
import seaborn as sns
from matplotlib import pyplot as plt

# Create dataset
data = {
    "Gender": ["Male", "Female", "Male", "Female", "Female", "male", "FEMALE", "Male"],
    "City": ["Mumbai", "Pune", "Mumbai", "Delhi", "Pune", "Mumbai", "Delhi", "Mumbai"],
    "Age": [20, 21, 19, 22, 20, np.nan, 21, 23],
    "Study_Hours": [3, 5, 2, 6, 4, 5, 3, 7],
    "Marks": [75, 88, 65, 92, 55, np.nan, 78, 150]
}

df = pd.DataFrame(data)

# Display original data
print("Original Data:")
print(df)

# Descriptive Statistics
print("\nDescriptive Statistics:")
print(df.describe())

# Box Plot
sns.boxplot(x=df["Marks"])
plt.title("Box Plot of Marks")
plt.show()

# Scatter Plot
sns.scatterplot(
    data=df,
    x="Study_Hours",
    y="Marks",
    hue="Gender"
)
plt.title("Study Hours vs Marks")
plt.show()

# Correlation Matrix
correlation = df.select_dtypes(include="number").corr()

print("\nCorrelation Matrix:")
print(correlation)

sns.heatmap(correlation, annot=True)
plt.title("Correlation Matrix")
plt.show()

# Identify Features and Target
X = df[["Gender", "City", "Age", "Study_Hours"]]
y = df["Marks"]

print("\nFeatures:")
print(X)

print("\nTarget Variable:")
print(y)
