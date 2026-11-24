import pandas as pd
import sqlite3
import os

# Load cleaned dataset
csv_path = "data/processed/student_career_cleaned.csv"

df = pd.read_csv(csv_path)

# Create database folder if it does not exist
os.makedirs("data/database", exist_ok=True)

# Connect to SQLite database
db_path = "data/database/student_career.db"

connection = sqlite3.connect(db_path)

# Transfer CSV data into SQL table
df.to_sql(
    "students",
    connection,
    if_exists="replace",
    index=False
)

# Verify database
cursor = connection.cursor()

cursor.execute("SELECT COUNT(*) FROM students")

total_records = cursor.fetchone()[0]

print("SQL Database Created Successfully!")
print("Total records:", total_records)
print("Database location:", db_path)

connection.close()