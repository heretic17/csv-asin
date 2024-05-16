import pandas as pd
import csv

# Attempt to read the CSV file into a DataFrame
try:
    # Open the CSV file using Python's built-in CSV reader
    with open('All+Listings+Report+04-23-2024.csv', 'r', encoding='utf-8') as file:
        # Create a CSV reader object with a custom delimiter
        reader = csv.reader(file, delimiter=';')

        # Read the CSV file line by line
        lines = []
        for line in reader:
            lines.append(line)

        # Convert the list of lines to DataFrame
        df = pd.DataFrame(lines, columns=['seller-sku', 'asin1', 'status'])

    # Define the pattern
    pattern = r'VITA-\d+\b(?=\s*\([xX]?\d*\)|\s*[*]*)'

    # Filter rows based on the pattern
    filtered_df = df[df['seller-sku'].str.contains(pattern, regex=True, na=False)]

    # Save the filtered DataFrame to a new CSV file
    filtered_df.to_csv('filtered_file.csv', index=False)

except pd.errors.ParserError as e:
    print("Error parsing CSV:", e)
    # Handle the error as needed
