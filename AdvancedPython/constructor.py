class Employee:
    #non parametized 
    def __init__(self):
        self.salary=2000
        self.age=21
        # parametrized contructor
    def __init__(self,sal,age):
        self.salary=sal
        self.age=age
        
        
e1=Employee()
e2=Employee()
e3=Employee(23,12)
# __dict__ is notation it is useful for to see the object content or information
print(e1.__dict__)

#constructor is special method for intializing objects with attributes 
#it is __init__() method and it's first arguments is 'self'


#without constructor we cannot create object of the class