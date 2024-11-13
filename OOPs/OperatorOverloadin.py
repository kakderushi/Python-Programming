'''
when same operator behaves differntly dependin on values
you can assign a new meaning to operators also and you can extend functionality of operators
it can change default behaviour of operator usin overriding

'''
'''
num1=10
num2=20
print(num1+num2)'''

# internally this step work in case of + 
'''
step1: check datatype of left operand 
step2: go in that class
step3:call __add__() function
'''
'''
class Book:
    def __init__(self,title,pages):
        self.title=title
        self.pages=pages
    def __add__(self,other):
        total=self.pages+other.pages
        return total
    
b1=Book('One indian Girl',300)
b2=Book("making awsome",300)
print('total number of pages',b1+b2)


'''
#overload operator comparision
class Hotel:
    def __init__(self,name,fare):
        self.name=name
        self.fare=fare
        
    def __gt__(self,other):
        return self.fare>other.fare

h1=Hotel('Taj hotel',20000)
h2=Hotel("pancharatna",1000)

        

