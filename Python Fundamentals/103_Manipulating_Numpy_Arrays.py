

import numpy as np

my_1d_array = np.zeros(10)
print(my_1d_array)

my_1d_array[0] = 50
print(my_1d_array)

my_1d_array[3:6] = 50
print(my_1d_array)

np.where(my_1d_array == 50)

my_2d_array = np.array([[1,5,9],[8,5,5]])
print(my_2d_array)

np.where(my_2d_array == 5)
np.where(my_2d_array < 5)
np.where(my_2d_array >= 5)
np.where(my_2d_array != 5)

np.argwhere(my_2d_array == 5)

index = np.where(my_2d_array > 5)
print(index)

my_2d_array[index]
my_2d_array[index] = 100
print(my_2d_array)

np.all(my_1d_array)
np.all(my_1d_array >= 0)
np.all(my_1d_array > 5)

np.any(my_1d_array)



a = np.array([[1,2],[3,4]])
b = np.array([[5,6],[7,8]])
print(a)
print(b)

v = np.vstack((a,b))
print(v)

np.vstack((a,b,a,b))

h = np.hstack((a,b))
print(h)

np.hstack((a,b,a,b))



print(my_2d_array)
my_2d_array.flatten()


































































