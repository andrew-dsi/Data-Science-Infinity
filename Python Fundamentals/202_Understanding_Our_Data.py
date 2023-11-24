####################################################
# Pandas - Exploring & Understanding our Data
####################################################

import pandas as pd

transactions = pd.read_excel("grocery_database.xlsx", sheet_name = "transactions")

transactions.shape
transactions.head(20)
transactions.tail(10)
transactions.sample(10)
sample = transactions.sample(frac = 0.1)

transactions.describe()

transactions.nlargest(25,"sales_cost")
transactions.nsmallest(25,"sales_cost")

transactions.nunique()

customer_details = pd.read_excel("grocery_database.xlsx", sheet_name = "customer_details")

customer_details.isna().sum()


