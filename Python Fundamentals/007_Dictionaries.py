

my_dict = {}

a = {1,2,3}

planet_dict = {
    "Mercury" : 8,
    "Venus" : 6,
    "Earth" : 5,
    "Mars" : 7,
    "Jupiter" : 1,
    "Saturn" : 2,
    "Uranus" : 3,
    "Neptune" : 4
    }

len(planet_dict)

planet_dict["Mars"]
planet_dict["Jupiter"]

planet_dict.get("Mars")

planet_dict.get("Pluto")

planet_dict.get("Pluto", 0)

planet_dict["Pluto"]

"Saturn" in planet_dict
"Pluto" in planet_dict

planet_dict.keys()
planet_dict.values()

planet_dict["Pluto"] = 9
print(planet_dict)

planet_dict["Uranus"] = 4
planet_dict["Neptune"] = 3
print(planet_dict)

planet_dict.pop("Earth")
print(planet_dict)






























