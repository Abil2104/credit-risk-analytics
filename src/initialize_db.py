import pandas as pd
import sqlite3
import os

print("Loading raw LendingClub data (sampling for performance)...")
csv_path = os.path.join('data', 'loan.csv')

# Step 1: Read essential columns to prevent memory crashes
keep_cols = [
    'member_id', 'loan_amnt', 'term', 'int_rate', 'installment', 
    'grade', 'sub_grade', 'annual_inc', 'loan_status'
]

# Using chunks or low_memory to handle the large file safely
df = pd.read_csv(csv_path, usecols=keep_cols, low_memory=False)

# Step 2: Handle basic data anomalies (Data Engineering/Auditing prep)
df['member_id'] = df['member_id'].fillna(df.index.to_series()) 
df['annual_inc'] = df['annual_inc'].fillna(df['annual_inc'].median())

print("Connecting to local SQLite database...")
db_dir = 'database'
conn = sqlite3.connect(os.path.join(db_dir, 'credit_risk.db'))

print("Writing data to database table 'loans'...")
df.to_sql('loans', conn, if_exists='replace', index=False)

conn.close()
print("🎉 Database initialized successfully at database/credit_risk.db!")
