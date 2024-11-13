'''class calci:
    def add(self,num1,num2):
        print('addition',num1+num2)
        
    def add(self,num1,num2,num3):
        print('addition',num1+num2+num3)
        
c1=calci()
c1.add(10,20)
c1.add(12,3,45)'''

# In python there is no concept of method overloading so this code gives type error

#but using below logic we can acheive method overloading in python
class Calci:
    def add(self,num1=None,num2=None,num3=None):
        if num1!=None and num2!=None and num3!=None:
            print(num1+num2+num3)
        elif num1!=None and num2!=None:
            print(num1+num2)
        else:
            print("Incorrect parameter is provide")
        
c1=Calci()
c1.add(10,20)
c1.add(12,3,45)