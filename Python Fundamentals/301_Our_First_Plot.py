####################################################
# Matplotlib - Our First Plot
####################################################

import matplotlib.pyplot as plt

x_values = [0,1,2,3,4,5,6,7,8,9,10]
x_squared = [x ** 2 for x in x_values]

plt.plot(x_values,x_squared)
plt.title("Exponential Growth")
plt.xlabel("The values of x")
plt.ylabel("The values of y")
plt.show()

import pandas as pd

my_df = pd.DataFrame({"X" : x_values,
                      "Y" : x_squared})


plt.plot(my_df["X"],my_df["Y"])
plt.title("Exponential Growth")
plt.xlabel("The values of x")
plt.ylabel("The values of y")
plt.show()



