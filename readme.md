# Advanced Fuzzy Matching Script for Excel Data Filtering

## Overview

In the realm of data analysis and management, the ability to accurately match and filter data based on similarity rather than exact matches can significantly enhance data quality and insights. This Python script leverages the power of the RapidFuzz library to perform advanced fuzzy string matching on Excel datasets, enabling users to efficiently filter rows that closely match specified criteria.

The script is designed to process large Excel files, comparing data across specified columns against a list of predefined names or terms. By employing fuzzy matching algorithms, it can identify and retain rows that approximate target values, even in the presence of minor discrepancies such as typos, variations in naming conventions, or incomplete data. This capability is particularly valuable in scenarios where data is derived from multiple sources, each with its own data entry standards.

## Why Use This Script?

- **Enhanced Data Cleaning**: Improve the quality of your datasets by filtering out irrelevant rows based on a sophisticated matching process that recognizes near-identical entries.
- **Increased Flexibility**: Traditional exact match filters often miss relevant data due to minor discrepancies. Fuzzy matching overcomes this limitation, ensuring valuable data is not inadvertently excluded from your analysis.
- **Time Efficiency**: Manually reviewing and filtering datasets for approximate matches can be prohibitively time-consuming, especially with large volumes of data. This script automates the process, saving significant time and effort.
- **Customizable Matching Threshold**: Users have the flexibility to set their own matching threshold, allowing for tighter or looser criteria depending on the specific requirements of the project.
- **Easy Integration**: Designed for straightforward implementation into existing data processing workflows, this script requires minimal setup and can be easily adapted to various projects and needs.

## Ideal Use Cases

- **Consolidating Customer Data**: Unify records from different databases where customer names might have been entered with slight variations.
- **Cleaning Survey Data**: Filter and categorize open-ended survey responses that contain similar phrases or keywords.
- **Product Catalog Management**: Identify and group similar product listings from multiple sources or vendors.
- **Research and Academic Projects**: For projects requiring the aggregation and analysis of data from diverse studies or sources.

Embrace the power of fuzzy string matching to refine your data processing tasks, ensuring your analyses are based on comprehensive and accurately filtered datasets.

## Getting Started

Follow the Installation and Usage sections above to integrate this script into your data analysis workflow and experience the benefits of advanced fuzzy matching in your projects.

## Requirements

- Python 3.6 or newer
- pandas
- RapidFuzz
- (optional FuzzyWuzzy) Requires more time/CPU

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
from rapidfuzz import process, fuzz #otionally use fuzzywuzzy for better logi but requires more resources)

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
