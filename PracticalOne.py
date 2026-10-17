#  Data Pre-processing and Exploration a. Load a CSV dataset. Handle missing values, inconsistent formatting, and outliers

# python3 -m venv venv
# source venv/bin/activate
# python -m pip install numpy pandas matplotlib seaborn scikit-learn
# python -c "import numpy, pandas, matplotlib, seaborn, sklearn; print('All libraries installed successfully!')"


import numpy as np
import pandas as pd
import seaborn as sns
from matplotlib import pyplot as plt
from sklearn.preprocessing import Binarizer
from sklearn.preprocessing import LabelEncoder
from sklearn.preprocessing import MinMaxScaler
from sklearn.preprocessing import StandardScaler
# Create dataset
data = {
 "Gender": ["Male", "Female", "Male", "Female", "Female", "male", "FEMALE", "Male"],
 "City": ["Mumbai", "Pune", "Mumbai", "Delhi", "Pune", "Mumbai", "Delhi", "Mumbai"],
 "Age": [20, 21, 19, 22, 20, np.nan, 21, 23],
 "Study_Hours": [3, 5, 2, 6, 4, 5, 3, 7],
 "Marks": [75, 88, 65, 92, 55, np.nan, 78, 150]
}
df = pd.DataFrame(data)
# Original Data
print("Original Data")
print(df)

# Missing Values
print("\nMissing Values")
print(df.isnull().sum())
# Fill missing values with median
df["Age"] = df["Age"].fillna(df["Age"].median())
df["Marks"] = df["Marks"].fillna(df["Marks"].median())
# Standardize Gender values
df["Gender"] = df["Gender"].str.strip().str.lower()
print("\nUnique Values")
print(df["Gender"].unique())
# Detect Outliers using IQR
Q1 = df["Marks"].quantile(0.25)
Q3 = df["Marks"].quantile(0.75)
IQR = Q3 - Q1
lower = Q1 - 1.5 * IQR
upper = Q3 + 1.5 * IQR
print("\nLower Limit:", lower)
print("Upper Limit:", upper)
outliers = df[
 (df["Marks"] < lower) |
  (df["Marks"] > upper)
]
print("\nOutliers:")
print(outliers)
# Handle outliers using clipping
df["Marks"] = df["Marks"].clip(lower, upper)