'''
Enumeration: keeps a counter to iterable and returns it.
syntax:
enumerate(iterable,[start=0])
iterable: any object that supports iteration ex: list, tuple
'''
import json
sports=['circket','kabbdi','kho-kho']

data=dict(list(enumerate(sports,1)))
f=open("data.json",'w')
json.dump(data,f)

enum_obj=enumerate(sports)
print(type(enum_obj))
# print the enumerate values
print(list(enum_obj)) #[(0, 'circket'), (1, 'kabbdi'), (2, 'kho-kho')] 

# use in looping
for pos ,ele in enumerate(sports):
    print(f"{pos}:{ele}")
    