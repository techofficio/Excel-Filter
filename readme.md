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
Output
The script will create an Excel file named filtered_data.xlsx containing the filtered dataset based on the fuzzy matching criteria.

