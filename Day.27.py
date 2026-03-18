#Create a class person and instantiate its objects . 
# also access the attributes of the class .  
class person :
    def __init__(self, name , age ):
        self.name = name 
        self.age = age 
        
    
    def display(self) :
        print("Name:", self.name)
        print("Age:", self.age)


# instantiating  objects . 
p1 = person("Saksham", 20)
p2 = person("Rahul", 22)

print("Person 1 Name:", p1.name)
print("Person 1 Age:", p1.age)

print("\nPerson 2 Name:", p2.name)
print("Person 2 Age:", p2.age)

# Using method
print("\nUsing display method:")
p1.display()
print()
p2.display()
  