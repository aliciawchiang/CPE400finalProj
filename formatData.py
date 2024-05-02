import pandas as pd
from datetime import datetime

# Load CSV data into a pandas DataFrame
data = pd.read_csv('heart_rate_data.csv')

# Define a function to categorize activity level
def categorize_activity_level(heart_rate):
    # Modify this function based on your criteria to categorize activity level
    if heart_rate < 72:
        return 'resting'
    else:
        return 'active'

# Convert 'Date Time' column to datetime
data['Date Time'] = pd.to_datetime(data['Date Time'])

# Extract time of day
data['time_of_day'] = data['Date Time'].dt.hour.apply(lambda x: 'morning' if 5 <= x < 12 else ('afternoon' if 12 <= x < 18 else 'evening'))

# Calculate activity level based on heart rate values
data['activity_level'] = data['Heart Rate'].apply(categorize_activity_level)

# Create binary label for resting or active
data['label'] = (data['activity_level'] == 'resting').astype(int)

# Select features and label
features = data[['Heart Rate', 'time_of_day', 'activity_level']]
labels = data['label']

# Export processed data to a new CSV file
data.to_csv('processed_heart_rate_data.csv', index=False)
