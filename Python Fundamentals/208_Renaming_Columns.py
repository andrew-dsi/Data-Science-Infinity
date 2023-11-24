####################################################
# Pandas - Renaming Columns
####################################################

import pandas as pd
transactions = pd.read_excel("grocery_database.xlsx", sheet_name = "transactions")

list(transactions)

transactions.rename(columns = {"customer_id" : "friend_id"}, inplace = True)
list(transactions)

column_names = ['friend_id',
 'transaction_date',
 'basket_id',
 'product_group_id',
 'num_items',
 'sales_cost']

transactions.columns = column_names
list(transactions)

column_names = ['friend id',
 'transaction date',
 'basket id',
 'product group id',
 'num items',
 'sales cost']

transactions.columns = column_names
list(transactions)
transactions.columns

transactions.columns = transactions.columns.str.replace(" ","_")
list(transactions)
























