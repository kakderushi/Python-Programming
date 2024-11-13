# Example 1
'''

class Parent:
    def __init__(self,num):
        self.__num=num
        
    def get_num(self):
        return self.__num
    
class Child(Parent):
    def show(self):
        print("this is the constructor")
        
        
son=Child(100)
print(son.get_num())
son.show()


output:
100
this is the constructor
Here we can acceses the parent class private values using get_num()(getter)
'''

#Example3
class Parent:
    def __init__(self,num):
        self.__num=num
        
    def get_num(self):
        return self.__num
    
class Child(Parent):
    def __init__(self,val,num):
        self.__val=val
        
    def get_val(self):
        return self.__val
    
son=Child(100,10)
print("Parent num ",son.get_num())
print("child val",son.get_val())


# Here we cannot accese son.get_num() beacuase child class have constructor


