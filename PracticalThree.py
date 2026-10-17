# Practical 3: Data Preprocessing
# Aim: Perform Label Encoding, Feature Scaling, and Binarization.

import numpy as np
import pandas as pd
from sklearn.preprocessing import LabelEncoder
from sklearn.preprocessing import MinMaxScaler
from sklearn.preprocessing import StandardScaler
from sklearn.preprocessing import Binarizer

# Create dataset
data = {
    "Gender": ["Male", "Female", "Male", "Female", "Female"],
    "Age": [20, 21, 19, 22, 20],
    "Marks": [75, 88, 65, 92, 55],
    "Study_Hours": [3, 5, 2, 6, 4]
}

df = pd.DataFrame(data)

print("Original Data:")
print(df)

# 1. Label Encoding
le = LabelEncoder()
df["Gender_Encoded"] = le.fit_transform(df["Gender"])

print("\nAfter Label Encoding:")
print(df[["Gender", "Gender_Encoded"]])

# 2. Min-Max Scaling
minmax = MinMaxScaler()
df["Marks_MinMax"] = minmax.fit_transform(df[["Marks"]])

print("\nAfter Min-Max Scaling:")
print(df[["Marks", "Marks_MinMax"]])

# 3. Standard Scaling
standard = StandardScaler()
df["Marks_Standard"] = standard.fit_transform(df[["Marks"]])

print("\nAfter Standard Scaling:")
print(df[["Marks", "Marks_Standard"]])

# 4. Binarization
binarizer = Binarizer(threshold=75)
df["Marks_Binary"] = binarizer.fit_transform(df[["Marks"]])

print("\nAfter Binarization:")
print(df[["Marks", "Marks_Binary"]])