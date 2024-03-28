README for Site List Filtering Script
This Python script (filter.py) is designed to filter a dataset based on fuzzy string matching. It uses pandas for data manipulation, rapidfuzz for efficient fuzzy string matching, and requires Excel files as inputs and outputs.

Prerequisites
Python 3.6 or newer
pip (Python package installer)
Optionally, Anaconda for creating isolated Python environments
Installation Instructions
Installing Python
If you do not have Python installed, download and install it from the official Python website (https://www.python.org/downloads/). Ensure that Python and pip are added to your system's PATH.

Setting up a Python Environment
Using native Python:
Install Required Packages: Open a terminal or command prompt and navigate to the directory containing filter.py. Install the required Python packages by running:

Copy code
pip install -r requirements.txt
requirements.txt should contain:

shell
Copy code
pandas>=1.2.0
rapidfuzz>=1.4.1
openpyxl>=3.0.0
Using Anaconda:
Install Anaconda: Download and install Anaconda from (https://www.anaconda.com/products/individual). Follow the installation instructions for your operating system.

Create a Conda Environment: Open Anaconda Prompt and create a new environment:

lua
Copy code
conda create --name filter_env python=3.8
Activate the Environment:

Copy code
conda activate filter_env
Install Required Packages:

r
Copy code
conda install pandas
conda install -c conda-forge rapidfuzz
conda install openpyxl
Alternatively, if you prefer using pip in a Conda environment:

Copy code
pip install pandas rapidfuzz openpyxl
Running in a Jupyter Notebook (Optional)
To run the script in a Jupyter Notebook, ensure you have installed Jupyter in your environment:

r
Copy code
conda install -c conda-forge notebook
or using pip:

Copy code
pip install notebook
Start Jupyter Notebook:

Copy code
jupyter notebook
Navigate to the script's directory and open a new notebook in the browser.

Running the Script
Before running the script, ensure you have updated the paths to the Excel files within the script according to your local file structure.

Native Python Execution
Run the script using the following command in the terminal or command prompt:

css
Copy code
python filter.py
Running in Jupyter Notebook
Copy the code from filter.py into a new cell in your notebook.
Update the Excel file paths directly in the code to match your environment.
Execute the cell to run the script.

Usage
Prepare Your Data: Ensure your dataset and list of site names are in Excel format. The script expects two Excel files:

A dataset file with the data to be filtered.
A site list file containing site names to match against.
Configure the Script: Open filter.py in your favorite text editor and adjust the following variables to match your setup:

site_list_path: Path to your site list Excel file.
data_path: Path to your dataset Excel file.
search_columns: Columns in your dataset to apply fuzzy matching on.
threshold: The fuzzy matching score threshold (0-100) to consider a match.
Run the Script: Navigate to the directory containing filter.py in your terminal or command prompt, and execute the script with Python:

bash
Copy code
python filter.py
Check Results: If the script runs successfully, it will generate a new Excel file (filtered_data.xlsx) in the same directory, containing only the rows from your dataset that matched the site names based on the specified threshold.

Example filter.py
Below is an example snippet from filter.py. Adjust the file paths and column names as needed:

python
Copy code
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
License
This project is licensed under the MIT License - see the LICENSE file for details.

go
Copy code

Feel free to copy and paste this Markdown directly into your GitHub `README.md`. Adjust the `site_list_path`, `data_path`, and `search_columns` variables in the example code block to match your actual file paths and column names.




