
import numpy as np

my_1d_array = np.random.randint(2,8,16)

np.max(my_1d_array)
my_1d_array.max()

my_1d_array.min()
my_1d_array.mean()
my_1d_array.sum()
my_1d_array.std()

my_2d_array = my_1d_array.reshape(4,4)
print(my_2d_array)

my_2d_array.max()
my_2d_array.max(axis = 0)
my_2d_array.max(axis = 1)

my_2d_array.argmax(axis = 0)
my_2d_array.argmax(axis = 1)

np.sort(my_1d_array)

a = np.array([1,2,3,4,5])

a + 10
a - 10
a * 10
a / 10

b = np.array([3,7,1,2,6])

a + b

a = np.array([-2,-1,0,1,2])

np.square(a)
np.sqrt(a)
np.sign(a)

np.sin(a)
np.cos(a)
np.tan(a)

a = np.array([1,2,3])
b = np.array([4,5,6])

np.dot(a,b)




































