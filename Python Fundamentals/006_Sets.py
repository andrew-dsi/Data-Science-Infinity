

my_set = {1,2,3}

my_set = set([1,2,3])

my_set = {1,1,2,3}
print(my_set)

my_set[0]

my_list = [1,2,1,3,1,4,5,6,1]
unique_values = set(my_list)
print(unique_values)

len(my_set)

my_set.add(4)
print(my_set)

my_set.update({5,6,7})
print(my_set)

my_set.discard(7)
print(my_set)

my_set.discard(9)
my_set.remove(9)


set1 = {1,2,3,4,5}
set2 = {3,4,5,6,7}

set1.difference(set2)

set2.difference(set1)

set1.difference_update(set2)
print(set1)

set1 = {1,2,3,4,5}
set2 = {3,4,5,6,7}

set1.intersection(set2)

set1.intersection_update(set2)







































