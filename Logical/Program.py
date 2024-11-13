mylist=[1,2,2,3,3,4,5,5,5,6,6]
#  here i have to print those who have l count 
newList=[]
for num in mylist:
    if mylist.count(num)==1:
        newList.append(num)
print(newList)
        