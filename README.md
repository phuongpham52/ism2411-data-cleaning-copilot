# Sales Data Cleaning Project

## Overview
This project demonstrates data cleaning techniques on a messy sales dataset using Python. The script cleans inconsistencies, handles missing values, and removes invalid data entries.

## Project Structure
ism2411-data-cleaning-copilot/
├── data/
│   ├── raw/
│   │   └── sales_data_raw.csv
│   └── processed/
│       └── sales_data_clean.csv        # created by your script
├── src/
│   └── data_cleaning.py                # your main script
├── README.md                           # short project description
└── reflection.md                       # your written explanation
text

## Requirements
- Python 3.7+
- pandas library

## Installation
```bash
pip install pandas
Usage
Clone the repository

bash
git clone https://github.com/yourusername/ism2411-data-cleaning-copilot.git
cd ism2411-data-cleaning-copilot
Place your raw data (optional - sample data included)
Ensure your CSV file is at data/raw/sales_data_raw.csv

Run the cleaning script

bash
python src/data_cleaning.py
Check the output

Cleaned data: data/processed/sales_data_clean.csv

Console output shows cleaning statistics

Sample Output
text
Loaded data with 10 rows and 7 columns
Column names standardized:
  'Order ID' -> 'order_id'
  'Product Name' -> 'product_name'
  'Category' -> 'category'
  'Quantity' -> 'quantity'
  'Price' -> 'price'
  'Order Date' -> 'order_date'
  'Customer' -> 'customer'
Stripped whitespace from 4 string columns
Filled 1 missing prices with median: $29.99
Filled 0 missing quantities with 0
Dropped 1 rows with missing product names
Found 1 rows with negative quantities
Found 1 rows with negative prices
Found 1 rows with zero transactions
Removed 3 invalid rows. 7 valid rows remaining.
Data cleaning pipeline completed!
Cleaning Logic
Column Names: Standardized to lowercase with underscores

Whitespace: Removed from all string columns

Missing Values:

Prices: Filled with column median

Quantities: Filled with 0

Product Names: Rows dropped (essential field)

Invalid Data:

Negative quantities removed

Negative prices removed

Zero transactions (quantity=0 & price=0) removed

AI Tool Usage
This project incorporates GitHub Copilot for code generation, demonstrating:

Responsible AI-assisted development

Critical review and modification of AI suggestions

Enhancement of AI-generated code with human expertise

Detailed reflection on the collaboration process

Learning Outcomes
Professional data cleaning workflows in Python

Production-ready error handling

AI pair programming best practices

Git version control with meaningful commits

Project documentation standards