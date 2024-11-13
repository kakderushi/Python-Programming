class Demo:
    pass
d1=Demo()
class Empoyee:
    def __init__(self,nm,age):
        self.name=nm
        self.age=age
        

e1=Empoyee('raj',21)
e2=Empoyee('jay',23)

# IsInstance function checks any object is a class object or not if yes then it is true or false
print(isinstance(d1,Empoyee))