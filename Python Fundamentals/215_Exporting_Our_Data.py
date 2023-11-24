####################################################
# Pandas - Exporting our Data
####################################################

import pandas as pd
import numpy as np

my_df = pd.DataFrame({"A" : [1,2,3],
                      "B" : ["one", np.nan, "three"]})

my_df.to_csv("tester_export.csv", index = False)

my_df.to_csv("tester_export.csv", index = False, columns = ["B"])

my_df.to_csv("tester_export.csv", index = False, header = False)

my_df.to_csv("tester_export.csv", index = False, na_rep = "MISSING")

my_df.to_csv("tester_export.txt", index = False, na_rep = "MISSING")

my_df.to_csv("tester_export.txt", index = False, sep = "\t")

my_df.to_excel("tester_export.xlsx", sheet_name = "Sheet_12345")

my_other_df = my_df * 3

with pd.ExcelWriter("tester_export.xlsx") as excel_writer:
    my_df.to_excel(excel_writer, sheet_name = "Sheet_12345")
    my_other_df.to_excel(excel_writer, sheet_name = "Sheet_6789")
    
    
my_df.to_csv("C:\Users\andre\OneDrive\Desktop\tester_export.csv", index = False)
my_df.to_csv("C:\\Users\\andre\\OneDrive\\Desktop\\tester_export.csv", index = False)
my_df.to_csv(r"C:\Users\andre\OneDrive\Desktop\tester_export.csv", index = False)