'''
getattr(object_name, attribute_name)
setattr(object_name,attribute_name,new_value)
delattr(object_name,attribute_name)
hasattr(object_name,attribute_name)
'''

class Empoyee:
    def __init__(self,nm,age):
        self.name=nm
        self.age=age
        

e1=Empoyee('raj',21)
e2=Empoyee('jay',23)
#get attribute value
print(getattr(e1,'age')) #21

#set attribute  value
setattr(e2,'name','jayraj')
print(e2.__dict__)
#delete the attribute of class
delattr(e2,'age')

#hasattr it is check whather any object is present or not
hasattr(e1,'nam')
