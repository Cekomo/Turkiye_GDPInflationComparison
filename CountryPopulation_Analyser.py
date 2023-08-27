import psycopg2
import matplotlib.pyplot as plt
import numpy as np

# Database connection details
db_params = {
    "dbname": "country_profile",
    "user": "postgres",
    "password": "3204965",
    "host": "localhost",
    "port": "5432"
}

# Connect to the database
conn = psycopg2.connect(**db_params)
cursor = conn.cursor()

# SQL query to retrieve data
query = """
    SELECT country_name, 
        region, 
        area_km2, 
        population, 
        ROUND(population / area_km2, 2) AS person_per_km2 
    FROM countries
    WHERE iso_code IS NOT NULL
    ORDER BY person_per_km2 DESC
    LIMIT 30;
"""

cursor.execute(query)
results = cursor.fetchall()

# Extract data for plotting
country_names = [row[0] for row in results]
person_per_km2 = [row[4] for row in results]

# Close the database connection
cursor.close()
conn.close()

# Create a logarithmic bar plot
plt.figure(figsize=(12, 8))
plt.barh(country_names, person_per_km2, color='skyblue')
plt.xscale('log')  # Use logarithmic scale on the x-axis
plt.xlabel('Population Density (people per km²) [log scale]')
plt.ylabel('Country')
plt.title('Top 50 Most Densely Populated Countries')
plt.gca().invert_yaxis()  # Invert y-axis to have the densest countries at the top
plt.tight_layout()

# Show the plot
plt.show()
