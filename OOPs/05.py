# Collection of the object

class Customer:
    def __init__(self,name,age):
        self.name=name
        self.age=age
        
    def intro(self):
        print("i am ",self.name,"and i am ",self.age)
        
c1=Customer("Rohit",12)
c2=Customer("omkar",34)
c3=Customer('Rushikesh',21)

l=[c1,c2,c3]

for i in l:
    #print(i.name)
    i.intro()
    
    
    
'''
WE can pass the object in list 
and we can also acceses it using loop

'''