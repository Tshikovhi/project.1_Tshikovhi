# -*- coding: utf-8 -*-
"""
Created on Fri Aug  2 06:27:21 2024

@author: lk
"""

# Naval hill 08/05/2024 till 30/05/2024 anomalies 
import pandas as pd
import matplotlib.pyplot as plt

# Loading temperature

data = pd.read_csv('temperature_data.csv')  # Replace with your data file
print(data.columns)
# Rename columns for easier access (optional)
data = data.rename(columns={'Date Time, GMT+02:00': 'Date', 'Temp, °C': 'Temperature'})

# Convert 'Date' column to datetime format
data['Date'] = pd.to_datetime(data['Date'])

 # Calculate baseline average temperature
baseline_period = data[(data['Date'] >= '2024-05-08') & (data['Date'] <= '2024-05-30')]
baseline_avg = baseline_period.groupby(baseline_period['Date'].dt.dayofyear)['Temperature'].mean()

# Filter data for the specific period: May 8, 2024, to May 30, 2024
analysis_period = data[(data['Date'] >= '2024-05-08') & (data['Date'] <= '2024-05-30')]

# Calculate baseline average temperature for each hour of the day over the period
baseline_avg = analysis_period.groupby(analysis_period['Date'].dt.hour)['Temperature'].mean()
# Calculate anomalies
analysis_period['Hour'] = analysis_period['Date'].dt.hour
analysis_period = analysis_period.set_index('Date')
analysis_period['Anomaly'] = analysis_period['Temperature'] - analysis_period['Hour'].map(baseline_avg)
