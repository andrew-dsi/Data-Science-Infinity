

import pandas as pd
from sklearn.preprocessing import OneHotEncoder

X = pd.DataFrame({"input1" : [1,2,3,4,5],
                  "input2" : ["A","A","B","B","C"],
                  "input3" : ["X","X","X","Y","Y"]})

categorical_vars = ["input2", "input3"]

one_hot_encoder = OneHotEncoder(sparse=False, drop = "first")

encoder_vars_array = one_hot_encoder.fit_transform(X[categorical_vars])

encoder_feature_names = one_hot_encoder.get_feature_names(categorical_vars)

encoder_vars_df = pd.DataFrame(encoder_vars_array, columns = encoder_feature_names)

X_new = pd.concat([X.reset_index(drop=True), encoder_vars_df.reset_index(drop=True)], axis = 1)

X_new.drop(categorical_vars, axis = 1, inplace = True)


