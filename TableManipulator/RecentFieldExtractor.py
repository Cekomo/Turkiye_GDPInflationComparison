# ------- Is for field extractor
# import pandas as pd

# # Load the CSV file into a pandas DataFrame
# input_file = 'Literacy_rate_countries.csv'
# output_file = 'output.csv'

# data = pd.read_csv(input_file)

# # Find the most recent literacy rate for each country
# data['Most_Recent_Literacy'] = data.apply(lambda row: row.dropna().iloc[-1], axis=1)

# # Create a new DataFrame with "Country Name" and the most recent literacy rate
# output_data = data[['Country Name', 'Most_Recent_Literacy']]

# # Rename the columns for clarity
# output_data.columns = ['Country Name', 'Recent Literacy Rate']

# # Write the new DataFrame to a new CSV file
# output_data.to_csv(output_file, index=False)

# ------- Is for record extractor
import csv

latest_years = {}

with open('DP_LIVE_26082023223458852.csv', newline='') as csvfile:
    reader = csv.DictReader(csvfile)
    for row in reader:
        if row['MEASURE'] == 'RT' and row['SUBJECT'] == 'TOT':
            year = int(row['TIME'])
            location = row['LOCATION']
            if location not in latest_years or year > latest_years[location]:
                latest_years[location] = year

with open('output.csv', 'w', newline='') as outputfile:
    writer = csv.writer(outputfile)
    writer.writerow(['LOCATION', 'Value'])
    
    with open('DP_LIVE_26082023223458852.csv', newline='') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            location = row['LOCATION']
            value = row['Value'] if row['MEASURE'] == 'RT' and row['SUBJECT'] == 'TOT' and int(row['TIME']) == latest_years[location] else ""
            writer.writerow([location, value])
