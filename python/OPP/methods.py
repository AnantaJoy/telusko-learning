# Instance, Class, Static Methods

class Student():
    school = 'Pathshala'
    def __init__(self, m1,m2,m3):
        self.m1 = m1
        self.m2 = m2
        self.m3 = m3
    def avg(self):
        return (self.m1+self.m2+self.m3)/3
    # class variable
    @classmethod
    def get_school(cls):
        return cls.school
    
    # static class
    @staticmethod
    def info():
        print("This is student class")

s1 = Student(75,65,68)
s2 = Student(78,67,78)
s3 = Student(78,75,79)

print(s2.avg())

print(Student.get_school())
Student.info()