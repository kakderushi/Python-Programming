#callable*()
'''
syntax:

callable(python_object)
True: if passed object is callable
False: if passed object not callable


what is callable objects:
Objects which can be called whenever required
objects having __call__() method in their class
'''

'''
x=100
# it is callable object beacause it's class is function so inside this class there is callable function
def add(a,b): #add.__call__(10,20)
    return a+b

print(type(add))

#let's check callable or not
print(callable(x))
print(callable(add))

'''

# python classes  callble 
class Add(object):
    def __init__(self,a,b):
        self.a=a
        self.b=b
    # make object callable 
    def __call__(self,a,b):
        res=a+b 
        
a1=Add(10,20)
print(a1(10,20) ) # a1__call__()
#but class object are not callable
print(callable(a1)) #False
print(callable(Add)) #True
    





