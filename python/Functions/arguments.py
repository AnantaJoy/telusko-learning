# x is an arguments
def update(x):
    x = 8
    print(id(x))

a = 10
print(id(a))
update(a)
print(id(a))

def person(name,age):
# def person(name,age=21)
    print(name)
    print(age)

person(age=21,name='Joy')

# passing multiple arguments
def sum(x,*y):
    z = x
    for i in y:
        z += i  
    print(z)
    print(type(y))

sum(2,3,4,5,6)

# keyword variable length arguments
def person_info(name, **data):
    print(name)
    print(data)
    print(type(data))
    for i,j in data.items():
        print(i,j)

person_info('John',age=32,location="Dhaka",email="axxx@example.com")
    