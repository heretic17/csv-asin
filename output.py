# import pandas as pd

# # Read the filtered CSV file
# filtered_df = pd.read_csv('filtered_file.csv')

# # Define the pattern to target certain regex texts
# pattern = r'VITA-\d+\b(?=\s*\([xX]?\d*\)|\s*[*]*)'

# # Specify the columns where you want to perform the replacement
# columns_to_replace = ['SKU']  # Add all columns you want to apply the replacement to

# # Perform the replacement
# for column in columns_to_replace:
#     filtered_df[column] = filtered_df[column].str.replace(pattern, '', regex=True)

# # Save the DataFrame with replacements to a new CSV file
# filtered_df.to_csv('filtered_file_with_replacements.csv', index=False)

import pandas as pd

# Read the input CSV file into a DataFrame
df = pd.read_csv('filtered_file.csv')

# Specify the column where you want to remove the pattern from the beginning of the string
column_to_modify = 'seller-sku'
# r'\b\d+\b'

df[column_to_modify] = df[column_to_modify].str.extract(r'(\b\d+\b)')

# Save the modified DataFrame to a new CSV file
df.to_csv('output_file.csv', index=False)


