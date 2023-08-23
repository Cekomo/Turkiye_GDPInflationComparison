import psycopg2

# Connect to the PostgreSQL database
conn = psycopg2.connect(
    dbname="country_economics",
    user="postgres",
    password="3204965",
    host="localhost",
    port="5432"
)

# Create a cursor
cur = conn.cursor()

# Construct the list of year columns dynamically
year_columns = ",\n".join([f"year_{year}" for year in range(1960, 2023)])

# List of countries in your desired order
countries = ['Turkiye', 'Germany', 'Greece']

# Create a dictionary to store country data
country_data = {}

# SQL queries for the selected countries
for country in countries:
    sql_query = f"""
        SELECT
            gdp.country_name,
            {year_columns}
        FROM inflation_consumer AS gdp
        WHERE country_name = '{country}';
    """
    cur.execute(sql_query)
    inf_row = cur.fetchone()

    inf_query = f"""
        SELECT
            inf.country_name,
            {year_columns}
        FROM gdp_per_capita_growth AS inf
        WHERE country_name = '{country}';
    """
    cur.execute(inf_query)
    gdp_row = cur.fetchone()

    # Store data in the dictionary
    country_data[country] = {'gdp': gdp_row[1:], 'inf': inf_row[1:]}

# Close the cursor and connection
cur.close()
conn.close()

# Calculate and print the average scores for each country
for country in countries:
    gdp_values = country_data[country]['gdp']
    inf_values = country_data[country]['inf']

    # Calculate the differences between GDP growth and inflation for each year
    diff_values = [gdp - inf if gdp is not None and inf is not None else None for gdp, inf in zip(gdp_values, inf_values)]

    # Calculate the average difference for the country
    filtered_diff = list(filter(None, diff_values))
    avg_score = sum(filtered_diff) / len(filtered_diff) if filtered_diff else None

    print(f"Average GDP - Inflation Score for {country}: {avg_score}")

