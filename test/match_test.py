import pandas as pd
import csv
from datetime import datetime
# Attempt to read the CSV file into a DataFrame
try:
    # Open the CSV file using Python's built-in CSV reader
    with open('test/output_file.csv', 'r', encoding='utf-8') as file:
        # Create a CSV reader object with a custom delimiter
        reader = csv.reader(file)

        # Read the CSV file line by line
        listing_lines = []
        for line in reader:
            listing_lines.append(line)

        # Convert the list of lines to DataFrame
        df = pd.DataFrame(listing_lines, columns=['seller-sku', 'asin1', 'status'])

    with open('test/Output_2024.4.12.csv', 'r', encoding='utf-8') as file:
        reader2 = csv.reader(file)

        output_lines = []
        for line2 in reader2:
            output_lines.append(line2)

        df2 = pd.DataFrame(output_lines, columns=['SKU', 'stat'])

    lvn_active_results = []
    vita_in_stock_results = []

    for listing_line in listing_lines:
        for output_line in output_lines:
            if listing_line[0] == output_line[0] and listing_line[2] == 'Active' and output_line[1] == 'Out of Stock':
                lvn_active_results.append(list(listing_line + [output_line[1]]))
            elif listing_line[0] == output_line[0] and listing_line[2] == 'Inactive' and output_line[1] == 'In Stock':
                vita_in_stock_results.append(list(listing_line + [output_line[1]]))

    current_date = datetime.now().strftime("%d.%m.%y")

    lvn_active_filename = f"Vita oos-Lvn In-Stock_{current_date}.csv"
    vita_in_stock_filename = f"Vita In-Stock-LVN Inactive_{current_date}.csv"

    # Write the data to the CSV file
    with open(lvn_active_filename, 'w', newline='', encoding='utf-8') as csvfile:
        writer = csv.writer(csvfile)

        # Write the header row
        writer.writerow(['seller-sku', 'asin1', 'LVN_status', 'Vita_status'])

        # Write each row of data
        for row in lvn_active_results:
            writer.writerow(row)

    print(f"CSV file '{lvn_active_filename}' has been created successfully.")

    with open(vita_in_stock_filename, 'w', newline='', encoding='utf-8') as csvfile:
        writer = csv.writer(csvfile)

        # Write the header row
        writer.writerow(['seller-sku', 'asin1', 'LVN_status', 'Vita_status'])

        # Write each row of data
        for row in vita_in_stock_results:
            writer.writerow(row)

    print(f"CSV file '{vita_in_stock_filename}' has been created successfully.")

except pd.errors.ParserError as e:
    print("Error parsing CSV:", e)
    # Handle the error as needed
