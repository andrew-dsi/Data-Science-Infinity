
####################################################
# Pandas - Creating DataFrames
####################################################

import pandas as pd

my_df = pd.DataFrame()

my_df = pd.DataFrame({"Name" : ["Tom", "Dick", "Harry"]})

my_df = pd.DataFrame({"Name" : ["Tom", "Dick", "Harry"],
                      "ID" : [101,102,103]})

my_list = [["Tom", 101], ["Dick", 102], ["Harry", 103]]

my_df = pd.DataFrame(my_list, columns = ["Name", "ID"])

"""
Name,ID
Tom,101
Dick,102
Harry,103
"""

my_data = pd.read_csv("tester_csv.csv")

transactions = pd.read_excel("grocery_database.xlsx", sheet_name = "transactions")
