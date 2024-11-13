# Child can't access private members of the  parent class
class Phone:
    def __init__(self,price,brand,camera):
        print("Inside phone constructor")
        self.__price=price
        self.brand=brand
        self.camera=camera
        
    def show(self):
        print(self.__price)
        
class SmartPhone(Phone):
    def check(self):
        print(self.__price)
        
        
s=SmartPhone(2000,'apple',13)
s.check() # this error gives error beacause in python we cannot private members of the class

    