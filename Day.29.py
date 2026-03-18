# Create  a class person and modify its attributes using objects . (update and delete ).
# Create class
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

# Create object
p1 = Person("Saksham", 20)

# Access original attributes
print("Original:")
print(p1.name, p1.age)

#  Update attributes
p1.name = "Rahul"
p1.age = 25

print("\nAfter Update:")
print(p1.name, p1.age)

#  Delete attribute
del p1.age

print("\nAfter Deleting age:")
print("Name:", p1.name)

# Trying to access deleted attribute will give error
# print(p1.age)  # This will cause AttributeError