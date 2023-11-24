


my_list = [1,2,3,4,5]
my_new_list = []

for i in my_list:
    my_new_list.append(i)
    
my_new_list = [i for i in my_list]



my_list = [1,2,3,4,5]
my_new_list = []

for i in my_list:
    my_new_list.append(i*i)
    
my_new_list = [i*i for i in my_list]


my_list = [1,2,3,4,5]
my_new_list = []

for i in my_list:
    if i % 2 == 0:
        my_new_list.append(i)
    
my_new_list = [i for i in my_list if i % 2 == 0]



def square_root(number):
    return number ** 0.5

my_list = [1,4,9,16,25]

my_new_list = [square_root(i) for i in my_list]


my_list = [[1,8],[2,3],[3,17]]

my_new_list = [i[0] for i in my_list]

my_new_list = [i[0] for i in my_list if i[1] == max(i[1] for i in my_list)]






























