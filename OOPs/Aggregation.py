# Aggregation (Has-A-Relationship)
class Customer:
    def __init__(self,name,gender,address):
        self.name=name
        self.gender=gender
        self.address=address
        
    def print_address(self):
        print(self.address.get_city(),self.address.pin,self.address.state)
    
    def edit_addreses(self,new_name,new_city,new_state,new_pin):
        self.name=new_name
        self.address.edit_address(new_city,new_pin,new_city)
        
        
class Address:
    def __init__(self,city,pin,state):
        self.__city=city
        self.pin=pin
        self.state=state
        
    def get_city(self):
        return self.__city # Here we make city attribute as private 
        
    def edit_address(self,new_city,new_pin,new_state):
         self.__city=new_city
         self.pin=new_pin
         self.state=new_state

# Object
add1=Address("Ghargon",4123,"maharashtra")
cust=Customer("Rushikesh",'male',add1)
cust.print_address()
cust.edit_addreses('kdfdk',"mumbai",123,"maha")
cust.print_address()
  