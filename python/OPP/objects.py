# create a class named Computer
class Computer():
    def config(self):
        print("i5, 8GB, 1TB")

com1 = Computer()
print(type(com1))

Computer.config(com1)
com1.config()