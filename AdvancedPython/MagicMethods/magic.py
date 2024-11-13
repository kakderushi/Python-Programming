'''
what are magic methods

magic methods  are special methods in python that have double
underscore(dunder) on both sides of the method name


Naming convention:  __methodName__

we don't need to call magic methods explicitely python automatically calls magic methods 
as a response to certain operations such as instantiation
'''

print(10 + 20 )
# __add__() this magic methods happend
print((10).__add__(20))