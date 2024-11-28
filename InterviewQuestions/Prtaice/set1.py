myset={
    'apple','banna','cherry'
}

#A set is collectionn which is unordered unchangeble, and unindexed and do not allow duplicates
for x in myset:
    print(x)

# in set once set is created you cannot change its items, but you can add new items
#using add fucntion we can add() new element 
myset.add('orange')
myset.remove('apple')
print(myset)