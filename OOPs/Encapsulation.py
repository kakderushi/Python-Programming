'''
Encapsulation:
the term encapsulation is defined as wrapping up data into single unit is called encapsulation
'''

class Finace:
    def __init__(self):
        # we cannot acces the data of revenue in HR class 
        self.__revenue=10000 # private member 
        self.numberOfSales=113
    # using method we can acceses these attribute also modified
    def display(self):
        print(f"{self.__revenue} and {self.numberOfSales}")
        
f1=Finace()
print(f1.__dict__)

class HR:
    def __init__(self):
        self.numberOfemp=32
        f1.revenue=0
h1=HR()
print(h1.__dict__)

# In python there is no pure concept of encapsulation
# In python we can restrict only data but case if someone know name mandling concept they will acceses the data

