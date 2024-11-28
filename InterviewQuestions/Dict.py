
# you can acesses the itmes of a dictionary by refering to it's key name inside the square brackets
this_dict={
    'brand':'ford',
    'model':'mustang',
    'year':1899
}
x=this_dict['model']
print(x)

# keys() method will return a list of all the keys in the dictionary
x1=this_dict.keys()
print(x1)

car = {
"brand": "Ford",
"model": "Mustang",
"year": 1964
}

x = car.keys()

print(x) #before the change

car["color"] = "white"

print(x) #after the change

car = {
"brand": "Ford",
"model": "Mustang",
"year": 1964
}

x = car.values()

print(x) #before the change

car["color"] = "red"

print(x) #after the change


# items() method will return each item in a dictinary as tuokes in list 

car={
    'brand':'ford',
    'model':'mustan',
    'year':1234
    }
x=car.items()
print(x)



thisdict={
    'brand':'ford',
    'model':'mustamg',
    'year':1890
}
thisdict['color']='red'
print(thisdict)



thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
thisdict.popitem()
print(thisdict)