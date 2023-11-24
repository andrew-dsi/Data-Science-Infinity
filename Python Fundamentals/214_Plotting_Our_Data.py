####################################################
# Pandas - Plotting our Data using Pandas
####################################################

import pandas as pd
transactions = pd.read_excel("grocery_database.xlsx", sheet_name = "transactions")
customer_details = pd.read_excel("grocery_database.xlsx", sheet_name = "customer_details")
product_areas = pd.read_excel("grocery_database.xlsx", sheet_name = "product_areas")

customer_details.plot()

daily_sales_summary = transactions.groupby("transaction_date")[["sales_cost","num_items"]].sum().reset_index()

daily_sales_summary["sales_cost"].plot()
daily_sales_summary.plot(x = "transaction_date", y = "sales_cost")
daily_sales_summary.plot(x = "transaction_date", y = "sales_cost", kind = "line")

daily_sales_summary.plot(x = "num_items", y = "sales_cost", kind = "scatter")

daily_sales_summary.plot(y = "sales_cost", kind = "box")
daily_sales_summary.plot(y = "sales_cost", kind = "hist", bins = 25)

product_areas.plot(kind = "bar", y = "profit_margin", x = "product_area_name")
























