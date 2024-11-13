# Super used in method
'''
class Phone:
    def __init__(self,price,brand,camera):
        print("Inside phone constructor")
        self.__price=price
        self.brand=brand
        self.camera=camera
    def buy(self):
        print("Buying a phone")
        
class SmartPhone(Phone):
    def buy(self):
        print("Buying a smartphone")
        # Here we use parent class buy() using super() keyword
        super().buy()
        
s=SmartPhone(1000,"rose",12)

'''
# Super is used in constructor
class Phone:
    def __init__(self,price,brand,camera):
        print("Inside phone constructor")
        self.__price=price
        self.brand=brand
        self.camera=camera
        
class SmartPhone(Phone):
    
    def __init__(self,price,brand,camera,os,ram):
        super().__init__(price,brand,camera)
        self.os=os
        self.ram=ram
        print("Inside smartphone constructor")
        
s=SmartPhone(2000,"samsung",12,"andorid",2)
print(s.os)
print(s.brand)

'''
Summary:

1) Super cannot aceses variable
2)super cannot used outside the class
3)super is used inside the class
4)Super is used for methods and contructor
'''