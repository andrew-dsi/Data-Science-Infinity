


"""
for each element in a collection:
    do stuff
"""

my_string = "Cup of Coffee"

for i in my_string:
    print(i)
    
for i in my_string:
    print(i.upper())
    
my_list = ["Cup", "of", "Coffee"]

for i in my_list:
    print(i)
    
my_list = [1,2,3,4,5,6,7,8,9]

for i in my_list:
    i_squared = i ** 2
    print(i,i_squared)
    
for i in my_list:
    print(i,i ** 2)
    
for i in my_list:
    print(i, "Loop Finished", type(i))
    
    
    
my_list = ["a", "b", "c"]

for idx, i in enumerate(my_list):
    print(idx,i)
    
    
for i in my_list:
    for j in my_list:
        print(i,j)
    
# range(start, stop, step)

for i in range(10, 100, 5):
    print(i)
    
    
i = 4

if i % 2 == 0:
    print(f"{i} is an even number")
else:
    print(f"{i} is an odd number")
    

my_nums = list(range(0,20))
print(my_nums)

for i in my_nums:
    
    if i % 2 == 0:
        print(f"{i} is an even number")
    else:
        print(f"{i} is an odd number")
        
        
for i in range(0,21):
    print(i)
    
for i in range(0,21):
    if i % 3 == 0:
        continue
    print(i)
    
for i in range(0,21):
    if i > 10:
        break
    print(i)
    

    

    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    