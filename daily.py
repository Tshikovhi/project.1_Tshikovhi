# -*- coding: utf-8 -*-
"""
Created on Fri Aug  2 06:54:44 2024

@author: lk
"""

import pandas as pd
import matplotlib.pyplot as plt

# Load temperature data
data = pd.read_csv('C:/Users/lk/OneDrive/Desktop/NQF 9/DATA ANALYSIS/DATA ANALYSIS/temperature_data.csv')

# Rename columns for easier access (optional)
data = data.rename(columns={'Date Time, GMT+02:00': 'Date', 'Temp, °C': 'Temperature'})

# Convert 'Date' column to datetime format
data['Date'] = pd.to_datetime(data['Date'])

# Filter data for the specific period: May 8, 2024, to May 30, 2024
analysis_period = data[(data['Date'] >= '2024-05-08') & (data['Date'] <= '2024-05-30')].copy()

# Extract day of the year for each date
analysis_period['DayOfYear'] = analysis_period['Date'].dt.dayofyear

# Calculate baseline average temperature for each day of the year over the period
baseline_avg = analysis_period.groupby('DayOfYear')['Temperature'].mean()

# Calculate daily average temperatures
daily_avg = analysis_period.groupby(analysis_period['Date'].dt.date)['Temperature'].mean()

# Map baseline averages to the daily data
daily_avg_df = pd.DataFrame(daily_avg).reset_index()
daily_avg_df['DayOfYear'] = pd.to_datetime(daily_avg_df['Date']).dt.dayofyear
daily_avg_df['Baseline'] = daily_avg_df['DayOfYear'].map(baseline_avg)

# Calculate anomalies
daily_avg_df['Anomaly'] = daily_avg_df['Temperature'] - daily_avg_df['Baseline']

# Plot daily anomalies
plt.figure(figsize=(12, 6))
plt.plot(daily_avg_df['Date'], daily_avg_df['Anomaly'], marker='o', linestyle='-', label='Daily Temperature Anomaly')
plt.axhline(0, color='red', linestyle='--', label='Baseline')
plt.xlabel('Date')
plt.ylabel('Temperature Anomaly (°C)')
plt.title('Daily Temperature Anomalies from May 8 to May 30, 2024')
plt.legend()
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()
import pandas as pd
import matplotlib.pyplot as plt

# Load temperature data
data = pd.read_csv('C:/Users/lk/OneDrive/Desktop/NQF 9/DATA ANALYSIS/DATA ANALYSIS/temperature_data.csv')

# Rename columns for easier access (optional)
data = data.rename(columns={'Date Time, GMT+02:00': 'Date', 'Temp, °C': 'Temperature', 'RH, %': 'RelativeHumidity', 'Location': 'Location'})

# Convert 'Date' column to datetime format
data['Date'] = pd.to_datetime(data['Date'])

# Filter data for the specific period: May 8, 2024, to May 30, 2024
analysis_period = data[(data['Date'] >= '2024-05-08') & (data['Date'] <= '2024-05-30')].copy()

# Extract day of the year for each date
analysis_period['DayOfYear'] = analysis_period['Date'].dt.dayofyear

# Calculate baseline average temperature for each day of the year over the period
baseline_avg = analysis_period.groupby('DayOfYear')['Temperature'].mean()

# Calculate daily average temperatures and RH
daily_avg = analysis_period.groupby(['Date', 'Location'])[['Temperature', 'RelativeHumidity']].mean().reset_index()

# Calculate daily anomalies for temperature
daily_avg['DayOfYear'] = pd.to_datetime(daily_avg['Date']).dt.dayofyear
daily_avg['Baseline'] = daily_avg['DayOfYear'].map(baseline_avg)
daily_avg['TemperatureAnomaly'] = daily_avg['Temperature'] - daily_avg['Baseline']

# Calculate spatial mean anomalies
spatial_mean_anomalies = daily_avg.groupby('Date')['TemperatureAnomaly'].mean().reset_index()

# Plot daily spatial mean anomalies
plt.figure(figsize=(12, 6))
plt.plot(spatial_mean_anomalies['Date'], spatial_mean_anomalies['TemperatureAnomaly'], marker='o', linestyle='-', label='Daily Spatial Mean Temperature Anomaly')
plt.axhline(0, color='red', linestyle='--', label='Baseline')
plt.xlabel('Date')
plt.ylabel('Temperature Anomaly (°C)')
plt.title('Daily Spatial Mean Temperature Anomalies from May 8 to May 30, 2024')
plt.legend()
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()




import pandas as pd
import matplotlib.pyplot as plt

# Load temperature data
data = pd.read_csv('C:/Users/lk/OneDrive/Desktop/NQF 9/DATA ANALYSIS/DATA ANALYSIS/temperature_data.csv')

# Rename columns for easier access
data = data.rename(columns={'Date Time, GMT+02:00': 'Date', 'Temp, °C': 'Temperature', 'RH, % ': 'RelativeHumidity'})

# Convert 'Date' column to datetime format
data['Date'] = pd.to_datetime(data['Date'])

# Filter data for the specific period: May 8, 2024, to May 30, 2024
analysis_period = data[(data['Date'] >= '2024-05-08') & (data['Date'] <= '2024-05-30')].copy()

# Extract day of the year for each date
analysis_period['DayOfYear'] = analysis_period['Date'].dt.dayofyear

# Calculate baseline average temperature for each day of the year over the period
baseline_temp_avg = analysis_period.groupby('DayOfYear')['Temperature'].mean()

# Calculate daily average temperatures and RH
daily_avg = analysis_period.groupby('Date')[['Temperature', 'RelativeHumidity']].mean().reset_index()

# Calculate daily anomalies for temperature
daily_avg['DayOfYear'] = pd.to_datetime(daily_avg['Date']).dt.dayofyear
daily_avg['TempBaseline'] = daily_avg['DayOfYear'].map(baseline_temp_avg)
daily_avg['TemperatureAnomaly'] = daily_avg['Temperature'] - daily_avg['TempBaseline']

# Plot daily temperature anomalies
plt.figure(figsize=(12, 6))
plt.plot(daily_avg['Date'], daily_avg['TemperatureAnomaly'], marker='o', linestyle='-', label='Daily Temperature Anomaly')
plt.axhline(0, color='red', linestyle='--', label='Baseline')
plt.xlabel('Date')
plt.ylabel('Temperature Anomaly (°C)')
plt.title('Daily Temperature Anomalies from May 8 to May 30, 2024')
plt.legend()
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()

# Calculate baseline average RH for each day of the year over the period
baseline_rh_avg = analysis_period.groupby('DayOfYear')['RelativeHumidity'].mean()

# Calculate daily anomalies for RH
daily_avg['RHBaseline'] = daily_avg['DayOfYear'].map(baseline_rh_avg)
daily_avg['RHAnomaly'] = daily_avg['RelativeHumidity'] - daily_avg['RHBaseline']

