"""
Sales Data Cleaning Script
=========================
This script cleans a messy sales dataset by:
1. Standardizing column names for consistency
2. Removing whitespace from text columns
3. Handling missing values appropriately
4. Removing invalid data entries
5. Outputting a clean, analysis-ready dataset

Author: [Your Name]
Date: [Current Date]
"""

import pandas as pd
import os

# ============================================================================
# Function: Load Data
# Purpose: Load the raw CSV file into a pandas DataFrame
# ============================================================================
def load_data(file_path: str) -> pd.DataFrame:
    pass
# ============================================================================
# Function: Clean Column Names
# Purpose: Standardize column names for consistency and ease of use
# ============================================================================
def clean_column_names(df: pd.DataFrame) -> pd.DataFrame:
    pass
# ============================================================================
# Function: Handle Missing Values
# Purpose: Address missing data in price and quantity columns
# ============================================================================

def handle_missing_values(df_clean):
    pass

# ============================================================================
# Function: Remove Invalid Rows
# Purpose: Remove rows with invalid values (negative quantities/prices)
# ============================================================================
def remove_invalid_rows(df: pd.DataFrame) -> pd.DataFrame:
    pass

if __name__ == "__main__":
    raw_path = "data/raw/sales_data_raw.csv"
    cleaned_path = "data/processed/sales_data_clean.csv"

    df_raw = load_data(raw_path)
    df_clean = clean_column_names(df_raw)
    df_clean = handle_missing_values(df_clean)
    df_clean = remove_invalid_rows(df_clean)
    df_clean.to_csv(cleaned_path, index=False)
    print("Cleaning complete. First few rows:")
    print(df_clean.head())