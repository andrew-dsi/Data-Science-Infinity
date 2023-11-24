####################################################
# Pandas - Pivoting our Data
####################################################

import pandas as pd

transactions = pd.read_excel("grocery_database.xlsx", sheet_name = "transactions")
product_areas = pd.read_excel("grocery_database.xlsx", sheet_name = "product_areas")
transactions = pd.merge(transactions, product_areas, how = "inner", on = "product_area_id")

transactions.head()

sales_summary = transactions.groupby(["transaction_date", "product_area_name"])["sales_cost"].sum().reset_index()

sales_summary_pivot = transactions.pivot_table(index = "transaction_date",
                                               columns = "product_area_name",
                                               values = "sales_cost",
                                               aggfunc = "sum")


sales_summary_pivot.plot()

sales_summary_pivot = transactions.pivot_table(index = ["transaction_date", "profit_margin"],
                                               columns = "product_area_name",
                                               values = "sales_cost",
                                               aggfunc = "sum",
                                               fill_value = 0,
                                               margins = True,
                                               margins_name = "Total") 















