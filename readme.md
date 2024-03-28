```
# Fuzzy Matching Script

This Python script performs fuzzy string matching on Excel files using the `RapidFuzz` library. It's designed to filter rows from a dataset where specified columns match any name from a provided list of site names, based on a set fuzzy matching threshold.

## Requirements

- Python 3.6 or newer
- pandas
- RapidFuzz

## Installation

1. **Install Python 3.6 or newer**: Download from [python.org](https://www.python.org/downloads/) and install Python if you haven't already.

2. **Install Required Python Libraries**: Open your terminal or command prompt and run the following command:

   ```bash
   pip install pandas rapidfuzz
   ```

## Usage

1. **Prepare Your Data**: Ensure your dataset and list of site names are in Excel format. The script expects two Excel files:
    - A dataset file with the data to be filtered.
    - A site list file containing site names to match against.

2. **Configure the Script**: Open `filter.py` in your favorite text editor and adjust the following variables to match your setup:
    - `site_list_path`: Path to your site list Excel file.
    - `data_path`: Path to your dataset Excel file.
    - `search_columns`: Columns in your dataset to apply fuzzy matching on.
    - `threshold`: The fuzzy matching score threshold (0-100) to consider a match.

3. **Run the Script**: Navigate to the directory containing `filter.py` in your terminal or command prompt, and execute the script with Python:

   ```bash
   python filter.py
   ```

4. **Check Results**: If the script runs successfully, it will generate a new Excel file (`filtered_data.xlsx`) in the same directory, containing only the rows from your dataset that matched the site names based on the specified threshold.

## Example `filter.py`

Below is an example snippet from `filter.py`. Adjust the file paths and column names as needed:

```python
import pandas as pd
from rapidfuzz import process, fuzz

# Load the site list
site_list_path = r"path_to_your_site_list.xlsx"
site_list_df = pd.read_excel(site_list_path)
site_names = pd.concat([
    site_list_df['Site Name'].dropna(),
    site_list_df['Old Name'].dropna()
]).unique().tolist()

# Load the data file
data_path = r"path_to_your_data_file.xlsx"
data_df = pd.read_excel(data_path)

# Define the columns in data_df to search against
search_columns = ['End User Customer', 'End User Parent Account', 'Job Description']

# Define a threshold for fuzzy matching
threshold = 85

# Function to apply fuzzy matching
def fuzzy_match(row):
    for column in search_columns:
        cell_value = str(row[column])
        highest = process.extractOne(cell_value, site_names, scorer=fuzz.WRatio, score_cutoff=threshold)
        if highest is not None:
            return True
    return False

# Apply the fuzzy_match function and save filtered dataframe
filtered_df = data_df[data_df.apply(fuzzy_match, axis=1)]
filtered_df.to_excel('filtered_data.xlsx', index=False)
```

## License

This project is licensed under the MIT License - see the LICENSE file for details.
```
