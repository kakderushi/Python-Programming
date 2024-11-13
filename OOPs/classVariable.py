'''class Variables :
1)variables made for entire class(All objects)
2)only one copy is created and distributed to all objects
3)Modification in class varible impact on all objects
'''

'''
Class Method:
Method which works on class varible
first argument is class reference
made using decorator @classmethod
'''

class Employee:
    companyName='infoysis'
    def __init__(self,nm,sal):
        self.name=nm
        self.salary=sal
        
    @classmethod
    def getCompanyName(cls):
        #cls.companyName="TCS"
        #print(cls.companyName)
        print(cls.companyName)
        
          
        
e1=Employee('jay',2000)
e2=Employee('vijay',12334)

Employee.getCompanyName()

# In order to acceses the class varible we have to use class  or object reference
print(e1.companyName)
# In order to modification we only use class reference
#Here we change the compay name 
Employee.companyName='TCS'
print(Employee.companyName)