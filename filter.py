import pandas as pd
from rapidfuzz import process, fuzz

# Load the site list
site_list_path = r"C:\Users\admin\Excel Filter\sites.xlsx"  # Update this path
site_list_df = pd.read_excel(site_list_path)

# Assuming site_list_df is your site list DataFrame
# Concatenate the values from 'Site Name' and 'Old Name', then drop duplicates and NaN values
site_names_combined = pd.concat([
    site_list_df['Site Name'].dropna(),
    site_list_df['Old Name'].dropna()
]).unique().tolist()

site_names = site_names_combined

# Load the data file
data_path = "C:/Users/admin/Excel Filter/data.xlsx"  # Update this path
data_df = pd.read_excel(data_path)

# Define the columns in data_df to search against
search_columns = ['End User Customer', 'End User Parent Account', 'Job Description'] # Adjust these to match the actual column names in your Excel file

# Define a threshold for fuzzy matching (0-100, where 100 is an exact match)
threshold = 95

# Function to apply fuzzy matching
def fuzzy_match(row):
    for column in search_columns:
        cell_value = str(row[column])  # Ensure the cell value is treated as a string
  # Use rapidfuzz to perform the fuzzy matching
        highest = process.extractOne(cell_value, site_names, scorer=fuzz.WRatio, score_cutoff=threshold)
# If a match with a score above the threshold is found, return True
        if highest is not None:
            return True
    return False

# Correctly applying fuzzy_match function to each row in the DataFrame
filtered_df = data_df[data_df.apply(fuzzy_match, axis=1)]

# Save the filtered dataframe to a new Excel file
filtered_df.to_excel('filtered_data.xlsx', index=False)
