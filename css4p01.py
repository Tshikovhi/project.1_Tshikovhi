# -*- coding: utf-8 -*-
"""
Created on Mon Feb  5 10:07:13 2024

@author: lk
"""

import pandas as pd
data = pd.read_csv("movie_dataset.csv")
print(data.head())



import pandas as pd
data = pd.read_csv("movie_dataset.csv")
print("Missing Values:\n", data.isnull().sum())
data.fillna(data.mean(), inplace=True)
print(data.head())
correlation_matrix = data.corr()
print("\nData Types:\n", data.dtypes)
numeric_data = data.select_dtypes(include=['number'])
correlation_matrix = numeric_data.corr()
print("\nCorrelation Matrix:\n", correlation_matrix)
