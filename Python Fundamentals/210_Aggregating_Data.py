####################################################
# Pandas - Aggregating data using GROUPBY
####################################################

import pandas as pd

"""

select
    product_area_id,
    count(*) as row_count,
    sum(sales) as total_sales
    
from
    transactions
    
group by
    product_area_id

"""

transactions = pd.read_excel("grocery_database.xlsx", sheet_name = "transactions")
product_areas = pd.read_excel("grocery_database.xlsx", sheet_name = "product_areas")

transactions["sales_cost"].sum()

transactions = pd.merge(transactions, product_areas, how = "inner", on = "product_area_id")

transactions["product_area_name"].value_counts()

transactions.groupby("product_area_name")["sales_cost"].sum()
transactions.groupby("product_area_name")["sales_cost"].quantile([0.25,0.5,0.75])

sales_summary = transactions.groupby("product_area_name")["sales_cost"].sum().reset_index()

sales_summary = transactions.groupby(["product_area_name", "transaction_date"])["sales_cost"].sum().reset_index()

sales_summary = transactions.groupby(["product_area_name", "transaction_date"])[["sales_cost","num_items"]].sum().reset_index()

sales_summary = transactions.groupby("product_area_name")["sales_cost"].agg("sum").reset_index()
sales_summary = transactions.groupby("product_area_name")["sales_cost"].agg(["sum","mean"]).reset_index()

sales_summary = transactions.groupby(["product_area_name", "transaction_date"])[["sales_cost","num_items"]].agg(["sum","mean"]).reset_index()


sales_summary = transactions.groupby("product_area_name").agg({"sales_cost" : "sum", "num_items" : "mean"}).reset_index()






















































