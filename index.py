python
import requests
import pandas as pd
import json

# Define API endpoint and parameters
api_url = "https://publictransport.abudhabi/api/v1/data"
params = {
    "dataset": "public_transport",
    "format": "json",
    "language": "en"
}

# Fetch data from the API
response = requests.get(api_url, params=params)
data = response.json()

# Process data into a DataFrame
df = pd.DataFrame(data['results'])

# Example: Filter data for buses operating in a specific area
area_of_interest = 'Al Khalidiya'
buses_in_area = df[df['route'].str.contains(area_of_interest, case=False)]

# Save filtered data to CSV
buses_in_area.to_csv('filtered_buses_in_area.csv', index=False)

print(f"Filtered data saved to 'filtered_buses_in_area.csv'")
