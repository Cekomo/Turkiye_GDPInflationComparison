# Add 'Is Complete' field checking completion of inflation data through the years.
# True if all data is present and False if there is even single NULL data.

import pandas as pd

# Read the CSV file into a pandas DataFrame
data = pd.read_csv('Inflation_consumer_prices.csv')

# Select the year columns from '1960' to '2022'
year_columns = [str(year) for year in range(1960, 2023)]

# Check for each record if all year columns are not null
data['Is Complete'] = data[year_columns].notnull().all(axis=1)

# Reorder columns with 'Is Complete' after 'Indicator Code'
column_order = ['Country Name', 'Country Code', 'Indicator Name', 'Indicator Code', 'Is Complete'] + year_columns
data = data[column_order]

# Save the updated DataFrame back to a CSV file
data.to_csv('output_file.csv', index=False)

