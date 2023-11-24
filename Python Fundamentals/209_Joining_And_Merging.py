####################################################
# Pandas - Joining & Merging DataFrames
####################################################

import pandas as pd

# JOINING

df_a = pd.DataFrame({"A" : [1,2,3], "B" : [4,5,6]})
df_b = pd.DataFrame({"C" : [1,2,3], "D" : [4,5,6]})

df_c = pd.concat([df_a,df_b], axis = 1)

df_c = pd.concat([df_a,df_b], axis = 0)

df_a = pd.DataFrame({"A" : [1,2,3], "B" : [4,5,6]})
df_b = pd.DataFrame({"A" : [1,2,3], "B" : [4,5,6]})
df_c = pd.concat([df_a,df_b], axis = 0)

df_a.append(df_b)

# MERGING

df_a = pd.DataFrame({"user_id" : [1,2,3,5,7], "age" : [41,15,60,18,29]})
df_b = pd.DataFrame({"user_id" : [1,2,3,4,5], "gender" : ["m","f","f","f","m"]})

# INNER JOIN

pd.merge(df_a,df_b, how = "inner", on = "user_id")

# LEFT JOIN

pd.merge(df_a,df_b, how = "left", on = "user_id")

# OUTER JOIN

pd.merge(df_a,df_b, how = "outer", on = "user_id")

# JOIN ON MULTIPLE COLUMNS
pd.merge(df_a,df_b, how = "outer", on = ["user_id","column2"])

df_b.rename(columns = {"user_id" : "customer_id"}, inplace = True)
pd.merge(df_a,df_b, how = "inner", left_on = "user_id", right_on = "customer_id")

















