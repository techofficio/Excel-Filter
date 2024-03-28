import pandas as pd
from rapidfuzz import process, fuzz
from concurrent.futures import ProcessPoolExecutor
from datetime import datetime
import numpy as np
import os

def load_data(site_list_path, data_path):
    # Load the site list
    site_list_df = pd.read_excel(site_list_path)
    # Combine site names into a list
    site_names = pd.concat([
        site_list_df['Site Name'].dropna(),
        site_list_df['Old Name'].dropna()
    ]).unique().tolist()

    # Separate list for Mnemonic with a higher matching requirement.
    mnemonic_names = site_list_df['Mnemonic'].dropna().unique().tolist()

    # Load the data file
    
    data_df = pd.read_excel(data_path)
    return site_names, mnemonic_names, data_df

def fuzzy_match(args):
    row, site_names, mnemonic_names, search_columns, mnemonic_threshold, general_threshold = args
    for column in search_columns:
        # Check if column exists in the row
        if column in row.index:
            cell_value = str(row[column])
            # Apply separate logic for 'Mnemonic'
            if column == 'Mnemonic':
                highest = process.extractOne(cell_value, mnemonic_names, scorer=fuzz.WRatio, score_cutoff=mnemonic_threshold)
            else:
                highest = process.extractOne(cell_value, site_names, scorer=fuzz.WRatio, score_cutoff=general_threshold)
            if highest:
                return True
        else:
            # Optionally, handle the case where the column is missing
            print(f"Column {column} not found in row.")
    return False

def process_chunk(chunk, site_names, mnemonic_names, search_columns, mnemonic_threshold, general_threshold):
    # Prepare args for each row in chunk
    args = [(chunk.iloc[i], site_names, mnemonic_names, search_columns, mnemonic_threshold, general_threshold) for i in range(len(chunk))]
    
    # Execute fuzzy matching in parallel
    with ProcessPoolExecutor() as executor:
        results = list(executor.map(fuzzy_match, args))
    
    # Use results to filter chunk directly
    return chunk[results]


def main():
    site_list_path = r"C:\Users\admin\Excel Filter\sites.xlsx"
    data_path = r"C:/Users/admin/Excel Filter/data.xlsx"
    site_names, mnemonic_names, data_df = load_data(site_list_path, data_path)
    
    search_columns = ['End User Customer', 'End User Parent Account', 'Job Description']
    mnemonic_threshold = 100  # Higher threshold for Mnemonic matches
    general_threshold = 85   # General threshold for other columns
    
    # Assuming data_df is split into manageable chunks for processing
    chunks = [data_df]  # Example: This should be your actual chunk splitting logic
    
    filtered_chunks = [process_chunk(chunk, site_names, mnemonic_names, search_columns, mnemonic_threshold, general_threshold) for chunk in chunks]
    
    filtered_df = pd.concat(filtered_chunks)
    
    base_file_name = 'filtered_data'
    output_file_name = base_file_name + '.xlsx'
    if os.path.exists(output_file_name):
        timestamp = datetime.now().strftime('%Y-%m-%d_%H-%M-%S')
        output_file_name = f'{base_file_name}_{timestamp}.xlsx'
    
    filtered_df.to_excel(output_file_name, index=False)

if __name__ == '__main__':
    main()