
# pass by reference
'''

class Customer:
    
    def __init__(self,name,gender):
        self.name=name
        self.gender=gender
        
def greet(customer):
    if customer.gender =='male':
        print("hello",customer.name,"sir")
    else:
        print("hello",customer.name,"mam")
    print('hello',customer.name)
    
    cust2=Customer("Gayu",'female')
    return cust2
        

cust=Customer("Rushikesh",'male')
print(cust.name)
greet(cust)
new_cust=greet(cust)
print(new_cust.name)

'''

'''
Here i pass the cust(which is object of the customer class) 
to greet function as reference so far that it will acceses all the values inside this greet() function.
'''


# Let's understand in better way

class Customer:
    def __init__(self,name):
        self.name=name
    
def greet(customer):
   print(id(customer))
   customer.name="Rohan"
   print(customer.name)
   # what happened
   print(id(customer))
    
    
cust=Customer('Rushikesh')
print(id(cust))
greet(cust)
print(cust.name)
'''
1 st output
1638337002176
1638337002176 there memeory addrese here same

2. output
1700424285536
1700424285536
Rohan
1700424285536
Rohan

# learning is in python objects are mutable like lists, dict, sets

'''

    