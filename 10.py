# 1. Load student activity data from a CSV file
# Ensure 'activities.csv' exists with columns: Student, Study, Sports, Sleep

import pandas as pd

try:
    df = pd.read_csv('activities.csv')

    # 2. Perform Analysis: Calculate total daily hours
    df['Total_Hours'] = df['Study'] + df['Sports'] + df['Sleep']

    # 3. Perform Analysis: Statistical summary
    print("--- Student Activity Analysis ---")
    print(df)
    
    print("\n--- Summary Statistics ---")
    print(f"Average Study Hours: {df['Study'].mean():.2f}")
    print(f"Maximum Sports Hours: {df['Sports'].max()}")
    print(f"Minimum Sleep Hours: {df['Sleep'].min()}")

    # 4. Grouping: Find students with high study hours (> 6)
    high_study = df[df['Study'] > 6]
    print("\n--- High Study Students (>6 hrs) ---")
    print(high_study[['Student', 'Study']])

except FileNotFoundError:
    print("Error: 'activities.csv' not found. Please ensure the file exists.")
