class User:
    
    
    def __init__(self):
        pass
    
    def login(self):
        print("login")
        
        
class Student(User):
        
    def enroll(self):
        print("enroll into the course")
        
        
u=User()
s=Student()
# Here we acceses parent class object
s.login()


# what we inherited from parent class
# 1)constructor
# 2)Non Private attributes
# 3)Non private methods 


'''
# Inheritance Summary
1)A class inherit form another class
2)Inheritance improves code reuse
3)constructor attributes, methods get inherited to the child class
4)The parent has no access to the child class
5)Private properties of parent are not accessible directly in child class
6)child class can overrid the attributes or methods this is called method overriding
7)super() is an inherit function which is used to invovke the parent class methods and contructor
'''
