class Student():
    
    def __init__(self,name,rollno):
        self.name = name
        self.rollno = rollno
        self.lap = self.Laptop()

    def show(self):
        print(self.name, self.rollno)

    class Laptop:
        
        def __init__(self):
            self.brand = 'HP'
            self.cpu = 'i5'
            self.ram = '8GB'

        def show(self):
            print(self.brand,self.cpu,self.ram)

std1 = Student('Jenny',23)
std2 = Student('John',25)

std1.show()
std2.show()

# call a class inside a class
lap1 = Student.Laptop()
print(lap1.brand)
laptop_config = lap1.show()
laptop_config()