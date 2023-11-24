

string1 = "data"
string2 = "science"
string3 = "infinity"

len(string1)

string1.index("d")

string3[0]
string3[3:6]

string1.replace("a","o")

print(string1)
string1a = string1.replace("a","o")
print(string1a)

string4 = string1 + "-" + string2 + "-" + string3
print(string4)

string4.upper()
string4.lower()

string4.title()

string4.split("-")

string4.count("-")

print('Don't Know')
print("Don't Know")

print("He said "One Small Step for Man"")
print('He said "One Small Step for Man"')

print('Don\'t Know')
print("He said \"One Small Step for Man\"")

a = 123
type(a)
b = str(a)
type(b)

my_string = "RED ALERT - Meltdown in sector 7G. Please contact: Homer"

alert_level = "RED"
error_type = "Meltdown"
sector = "7G"
contact_name = "Homer"

my_string = f"{alert_level} ALERT - {error_type} in sector {sector}. Please contact: {contact_name}"
print(my_string)

alert_level = "AMBER"
error_type = "Overheating"
sector = "7H"
contact_name = "Lenny"

my_string = f"{alert_level} ALERT - {error_type} in sector {sector}. Please contact: {contact_name}"
print(my_string)

my_string = "{} ALERT - {} in sector {}. Please contact: {}".format(alert_level,error_type,sector,contact_name)
print(my_string)

my_string = "%s ALERT - %s in sector %s. Please contact: %s" % (alert_level,error_type,sector,contact_name)
print(my_string)


























































