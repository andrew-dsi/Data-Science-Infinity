

list1 = []
type(list1)

list1 = list()

list1 = [1, 2.55, "Three", 400000, True]
print(list1)

len(list1)


# Accessing Elements & Slicing

list1[0]
list1[3]
list1[5]

list1[-1]
list1[-2]

list2 = [0,1,2,3,4,5,6,7,8,9]
len(list2)

list2[start:end]
list2[start:]
list2[:end]

list2[4:7]

list2[4:]
list2[:4]

list2[-4:-1]


# Adding Elements

planets = ["Mercury", "Venus", "Earth"]
print(planets)

planets.append("Jupiter")
print(planets)

planets.insert(3,"Mars")
print(planets)

outer_planets = ["Saturn", "Uranus", "Neptune", "Pluto"]

planets.extend(outer_planets)
print(planets)

[1,2,3] + [4,5,6]


# Removing Elements

print(planets)

planets.remove("Pluto")
print(planets)

del planets[2]
print(planets)

planets.pop(2)


# Finding the index of an element

planets.index("Mercury")
planets.index("Earth")
planets.index("Tatooine")

"Earth" in planets
"Tatooine" in planets


# Sorting Lists

planets.sort()
print(planets)

planets.sort(reverse = True)
print(planets)


# Copying Lists

list1 = [1,2,3]
list2 = list1

print(list1)
print(list2)

list2.append(4)

print(list1)
print(list2)


list1 = [1,2,3]
list2 = list1.copy()

list2.append(4)

print(list1)
print(list2)
























































































































































