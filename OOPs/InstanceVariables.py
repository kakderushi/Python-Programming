'''
Instance Variables:

1) variables made for particular instance
2) sepatate copy is created for every object 
3) values of varibles differs from object to object
4) modification in one object won't effect ohter objects
'''



'''
Ways of creating Instance Varibles
1) using contructor
2) using instance method
3) outside class
'''


class Student:
    #instance constructor
    def __init__(self,name,marks):
        # these are instance varibles
        self.name=name
        self.marks=marks
    #instance method
    def display(self):
        print(self.name,self.marks)
        
std1=Student('Akshay',98)
std2=Student('raj',12)
std3=Student('jay',45)
std1.display()