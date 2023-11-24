
import pandas as pd
import numpy as np
from sklearn.impute import SimpleImputer

my_df = pd.DataFrame({"A" : [1,4,7,10,13],
                      "B" : [3,6,9,np.nan,15],
                      "C" : [2,5,np.nan,11,np.nan]})

imputer = SimpleImputer()

imputer.fit(my_df)
imputer.transform(my_df)

my_df1 = imputer.transform(my_df)

imputer.fit_transform(my_df)

my_df2 = pd.DataFrame(imputer.fit_transform(my_df), columns = my_df.columns)

imputer.fit_transform(my_df[["B"]])
my_df["B"]= imputer.fit_transform(my_df[["B"]])






