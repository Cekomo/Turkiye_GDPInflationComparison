import pandas as pd

# Load the CSV file into a pandas DataFrame
input_file = 'Countries_area.csv'
output_file = 'output_file.csv'

data = pd.read_csv(input_file)

# Find the most recent population for each country
data[' Area (km2)'] = data.apply(lambda row: row.dropna().iloc[-1], axis=1)

# Create a new DataFrame with "Country Name" and the most recent population
output_data = data[['Country Name', ' Area (km2)']]

# Format values based on whether they are integers or floats
def format_value(value):
    if pd.notnull(value):
        if isinstance(value, float) and value.is_integer():
            return int(value)
        return value
    return None

output_data.loc[:, ' Area (km2)'] = output_data[' Area (km2)'].apply(format_value)

# Write the new DataFrame to a new CSV file
output_data.to_csv(output_file, index=False)

print("CSV file with formatted values created successfully.")
