####################################################
# Matplotlib - Plot Colours & Styles
####################################################

import matplotlib.pyplot as plt

x_values = [0,1,2,3,4,5,6,7,8,9,10]
x_squared = [x ** 2 for x in x_values]
x_cubed = [x ** 3 for x in x_values]

plt.style.available
plt.style.use('seaborn-poster')

plt.plot(x_values,x_squared, label = "X Squared")
plt.plot(x_values,x_cubed, label = "X Cubed")
plt.title("Exponential Growth")
plt.xlabel("The values of x")
plt.ylabel("The values of y")
plt.legend()
plt.show()