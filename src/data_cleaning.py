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
    """
    Load sales data from a CSV file.
    
    Parameters:
    file_path (str): Path to the raw CSV file
    
    Returns:
    pd.DataFrame: Raw sales data as a DataFrame
    """
    # Check if file exists
    if not os.path.exists(file_path):
        raise FileNotFoundError(f"File not found: {file_path}")
    
    # Load the CSV file
    df = pd.read_csv(file_path)
    return df

# ============================================================================
# Function: Clean Column Names
# Purpose: Standardize column names for consistency and ease of use
# ============================================================================
def clean_column_names(df: pd.DataFrame) -> pd.DataFrame:
    """
    Standardize column names to lowercase with underscores and remove whitespace.
    
    Parameters:
    df (pd.DataFrame): DataFrame with potentially messy column names
    
    Returns:
    pd.DataFrame: DataFrame with cleaned column names
    """
    # Create a copy to avoid modifying the original
    df_clean = df.copy()
    
    # Standardize column names: lowercase and replace spaces with underscores
    # Why: Consistent naming makes code easier to read and maintain
    df_clean.columns = (
        df_clean.columns
        .str.lower()  # Convert to lowercase
        .str.strip()  # Remove leading/trailing whitespace
        .str.replace(' ', '_', regex=False)  # Replace spaces with underscores
    )
    
    return df_clean

# ============================================================================
# Function: Handle Missing Values
# Purpose: Address missing data in price and quantity columns
# ============================================================================

def handle_missing_values(df_clean):
    # --- Step 1: Convert 'price' to numeric ---
    # Force conversion, invalid entries (like '') become NaN
    df_clean['price'] = pd.to_numeric(df_clean['price'], errors='coerce')

    # --- Step 2: Handle negative values ---
    # If negatives don't make sense, replace them with NaN
    df_clean.loc[df_clean['price'] < 0, 'price'] = None

    # --- Step 3: Compute median safely ---
    price_median = df_clean['price'].median()

    # --- Step 4: Fill missing values with median ---
    df_clean['price'] = df_clean['price'].fillna(price_median)

    # --- Step 5: Repeat for other columns if needed ---
    # Example: fill missing 'category' with mode
    if 'category' in df_clean.columns:
        category_mode = df_clean['category'].mode()[0]
        df_clean['category'] = df_clean['category'].fillna(category_mode)

    return df_clean

# ============================================================================
# Function: Remove Invalid Rows
# Purpose: Remove rows with invalid values (negative quantities/prices)
# ============================================================================
def remove_invalid_rows(df: pd.DataFrame) -> pd.DataFrame:
    """
    Remove rows with invalid values (negative quantities or negative prices).
    
    Parameters:
    df (pd.DataFrame): DataFrame that may contain invalid values
    
    Returns:
    pd.DataFrame: DataFrame with invalid rows removed
    """
    df_clean = df.copy()
    
    # Remove rows with negative quantities
    # Why: Negative quantities don't make sense for sales data (likely data entry errors)
    if 'quantity' in df_clean.columns:
        df_clean = df_clean[df_clean['quantity'] >= 0]
    
    # Remove rows with negative prices
    # Why: Negative prices are invalid for sales transactions
    if 'price' in df_clean.columns:
        df_clean = df_clean[df_clean['price'] >= 0]
    
    return df_clean

# ============================================================================
# Main Execution
# ============================================================================
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