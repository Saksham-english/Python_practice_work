fruits = ("apple","mango","plum")
print(fruits)
list_fruits = list(fruits)
print(type(list_fruits))
y = list_fruits[1]
# print(y)
x = list_fruits[-3]
# print(x)
list_fruits[1] = "Kiwi"
print(list_fruits)
list_fruits[-3] = "Pomegrenate"
print(list_fruits)
z = tuple(list_fruits)
print(x,y)