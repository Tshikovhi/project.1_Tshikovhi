import pandas as pd

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
    df = df.rename(columns={'Date Time, GMT+02:00': 'Date', 'Temp, °C': 'Temperature', 'RH, % ': 'RelativeHumidity'})
    df['Station'] = station  # Add station identifier
    dataframes.append(df)

# Concatenate all DataFrames into a single DataFrame
combined_data = pd.concat(dataframes, ignore_index=True)

# Convert 'Date' column to datetime format
combined_data['Date'] = pd.to_datetime(combined_data['Date'])

# Filter data for the specific period: May 8, 2024, to May 30, 2024
analysis_period = combined_data[(combined_data['Date'] >= '2024-05-08') & (combined_data['Date'] <= '2024-05-30')].copy()

# Extract date without time
analysis_period['DateOnly'] = analysis_period['Date'].dt.date

# Calculate baseline average temperature and RH for each day across all stations
baseline_avg_daily = analysis_period.groupby(['Station', 'DateOnly'])[['Temperature', 'RelativeHumidity']].mean().reset_index()
baseline_avg_daily = baseline_avg_daily.rename(columns={'Temperature': 'BaselineTemperature', 'RelativeHumidity': 'BaselineRH'})

# Merge baseline average back with the original data
analysis_period = pd.merge(analysis_period, baseline_avg_daily, on=['Station', 'DateOnly'])

# Calculate daily anomalies
analysis_period['TemperatureAnomaly'] = analysis_period['Temperature'] - analysis_period['BaselineTemperature']
analysis_period['RHAnomaly'] = analysis_period['RelativeHumidity'] - analysis_period['BaselineRH']

# Calculate daily spatial mean anomalies
daily_spatial_mean_anomalies = analysis_period.groupby('DateOnly')[['TemperatureAnomaly', 'RHAnomaly']].mean().reset_index()

