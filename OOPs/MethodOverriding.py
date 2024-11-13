# Method overriding
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
        print("Buying a smartPhone")
        
        
s=SmartPhone(20000,"Apple",19)


# IN Method overriding if parent class and child class have same method or constructor then   always child class method and child class constuctor excecuted this concept is known as method overriding