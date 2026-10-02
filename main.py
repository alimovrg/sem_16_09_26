import pandas as pd



"""transactions = pd.read_csv('transactions.csv')
print(transactions.shape)
print(transactions.head(3))
print(transactions.info())"""

df = pd.read_parquet('gibdd_2025.parquet')
print(df.shape)
print(df.head(5))
print(df.info)