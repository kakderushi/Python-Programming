thislist={
    'brand':'ford',
    'model':'yyye',
    'year':1480
}

#using this loop we can only acces the values of the dict
for x in thislist:
    print(thislist[x])
    
# you can use the keys() method to return the keys of a dictionary

for x in thislist.keys():
    print(x)