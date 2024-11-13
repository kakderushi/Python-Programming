'''
# Here if child class has not constructor then it will call the parent class constructor
class Phone:
    def __init__(self,price,brand,camera):
        print("Inside phone constructor")
        self.price=price
        self.brand=brand
        self.camera=camera
        
    def buy(self):
        print("Buying a phone")
        
class SmartPhone(Phone):
    pass

s=SmartPhone(2000,'Apple',13)
s.buy()

'''

# If child class have the constuctor then it will not call the parent class constuctor
#So if If i try to acceses it's values of parent class then it will through error beacuse in parent class contructor is not initilized
class Phone:
    def __init__(self,price,brand,camera):
        print("Inside phone constructor")
        self.price=price
        self.brand=brand
        self.camera=camera
        
        
class SmartPhone(Phone):
    def __init__(self,os,ram):
        self.os=os
        self.ram=ram
        print("Inside SmartPhone constructor")
        
s=SmartPhone("Android ",12)

