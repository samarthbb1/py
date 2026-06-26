# 8a. Bank Balances and Transaction Updates
# Create a DataFrame for account balances

import pandas as pd
accounts = pd.DataFrame({'Balance': [5000, 3000, 1500]}, index=['Acc_1', 'Acc_2', 'Acc_3'])

# Create a Series for current transactions
transactions = pd.Series([-500, 2000, -200], index=['Acc_1', 'Acc_2', 'Acc_3'])

# Update balances using Series-DataFrame addition
accounts['Updated_Balance'] = accounts['Balance'] + transactions

print("--- Bank Account Updates ---")
print(accounts)




# 8b. Student Ranking System
import pandas as pd
data = {
    'Name': ['Alice', 'Bob', 'Charlie', 'David'],
    'Marks': [85, 92, 78, 92]
}

df = pd.DataFrame(data)

# Sort by Marks (Descending)
df = df.sort_values(by='Marks', ascending=False)

# Assign Ranks (method='min' handles ties)
df['Rank'] = df['Marks'].rank(ascending=False, method='min')

print("\n--- Student Rankings ---")
print(df)






























