#Create a class car and instantiate its object s .
# also access the attributes of the class .
class car :
    def __init__(self, brand, model , price ) : 
          self.brand = brand 
          self.model = model
          self.price = price 
          
car1 = car("Toyota", "Fortuner", 5000000)
car2 = car("Honda", "City", 1500000)


print(car1.brand, car1.model, car1.price)
print(car2.brand, car2.model, car2.price)