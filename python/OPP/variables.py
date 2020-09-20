# instance variable and class variable
class Car:
    # class namespace
    wheels = 4
    # __init__ method
    def __init__(self):
        self.brand = 'Audi'
        self.model = 'A8'

# instance variable
car1 = Car()
print(car1.brand, car1.model, car1.wheels)

# class variable
Car.wheels = 5
print(car1.brand, car1.model, car1.wheels)