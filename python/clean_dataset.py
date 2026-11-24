# STUDENT CAREER PREFERENCE ANALYSIS
# Phase 2: Data Cleaning

import pandas as pd
from pathlib import Path

# Project folder
project_folder = Path(__file__).resolve().parent.parent

# Load dataset
input_file = project_folder / "data" / "raw" / "student_career_data.csv"

df = pd.read_csv(input_file)

print("DATA CLEANING STARTED")
print("=" * 40)

# 1. Original dataset information
print("\nOriginal Dataset Shape:")
print(df.shape)

# 2. Check missing values
print("\nMissing Values:")
print(df.isnull().sum())

# 3. Check duplicate records
print("\nDuplicate Records:")
print(df.duplicated().sum())

# 4. Remove duplicates
df = df.drop_duplicates()

# 5. Clean column names
df.columns = df.columns.str.strip()

# 6. Clean text values
for column in df.select_dtypes(include="object").columns:
    df[column] = df[column].str.strip()

# 7. Handle missing values safely

for column in df.columns:

    missing_count = df[column].isnull().sum()

    if missing_count > 0:

        # Numerical columns
        if pd.api.types.is_numeric_dtype(df[column]):
            df[column] = df[column].fillna(df[column].median())

        # Government exam field
        elif column == "Government_Exam":
            df[column] = df[column].fillna("None")

        # Private career field
        elif column == "Private_Career":
            df[column] = df[column].fillna("None")

        # Other text columns
        else:
            df[column] = df[column].fillna("Unknown")
# 8. Check final dataset
print("\nFinal Dataset Shape:")
print(df.shape)

print("\nRemaining Missing Values:")
print(df.isnull().sum().sum())

print("\nRemaining Duplicates:")
print(df.duplicated().sum())

# 9. Save cleaned dataset
output_file = project_folder / "data" / "processed" / "student_career_cleaned.csv"

output_file.parent.mkdir(parents=True, exist_ok=True)

df.to_csv(output_file, index=False)

print("\n" + "=" * 40)
print("DATA CLEANING COMPLETED!")
print("Cleaned file saved at:")
print(output_file)

print("\nFirst 5 Cleaned Records:")
print(df.head())