import pandas as pd
import matplotlib.pyplot as plt

# Define file paths for each station
file_paths = {
    'CBC': r'C:\Users\lk\OneDrive\Desktop\NQF 9\DATA ANALYSIS\DATA ANALYSIS\CBC.csv',
    'Naval_Hill': r'C:\Users\lk\OneDrive\Desktop\NQF 9\DATA ANALYSIS\DATA ANALYSIS\Naval_Hill.csv',
    'St_Micheals': r'C:\Users\lk\OneDrive\Desktop\NQF 9\DATA ANALYSIS\DATA ANALYSIS\St_Micheals.csv'
}

# Initialize an empty list to hold DataFrames
dataframes = []

# Read each CSV file and append DataFrames to the list
for station, file_path in file_paths.items():
    df = pd.read_csv(file_path)
    df = df.rename(columns={'Date Time, GMT+02:00': 'Date', 'Temp, °C': 'Temperature'})
    df['Station'] = station  # Add station identifier
    dataframes.append(df)

# Concatenate all DataFrames into a single DataFrame
combined_data = pd.concat(dataframes, ignore_index=True)

# Convert 'Date' column to datetime format
combined_data['Date'] = pd.to_datetime(combined_data['Date'])

# Filter data for the specific period: May 8, 2024, to May 30, 2024
analysis_period = combined_data[(combined_data['Date'] >= '2024-05-08') & (combined_data['Date'] <= '2024-05-30')].copy()

# Extract hour from the Date column
analysis_period['Hour'] = analysis_period['Date'].dt.hour

# Calculate baseline average temperature for each hour of the day across all stations
baseline_avg = analysis_period.groupby(['Station', 'Hour'])['Temperature'].mean().reset_index()
baseline_avg = baseline_avg.rename(columns={'Temperature': 'BaselineTemperature'})

# Merge baseline average back with the original data
analysis_period = pd.merge(analysis_period, baseline_avg, on=['Station', 'Hour'])

# Calculate hourly anomalies
analysis_period['Anomaly'] = analysis_period['Temperature'] - analysis_period['BaselineTemperature']

# Calculate hourly spatial mean anomalies
hourly_spatial_mean_anomalies = analysis_period.groupby('Hour')['Anomaly'].mean().reset_index()

# Plot hourly spatial mean anomalies
plt.figure(figsize=(12, 6))
plt.plot(hourly_spatial_mean_anomalies['Hour'], hourly_spatial_mean_anomalies['Anomaly'], marker='o', linestyle='-', label='Hourly Spatial Mean Temperature Anomaly')
plt.axhline(0, color='red', linestyle='--', label='Baseline')
plt.xlabel('Hour of the Day')
plt.ylabel('Temperature Anomaly (°C)')
plt.title('Hourly Spatial Mean Temperature Anomalies from May 8 to May 30, 2024')
plt.legend()
plt.xticks(range(24))  # Show all hours
plt.tight_layout()
plt.show()

