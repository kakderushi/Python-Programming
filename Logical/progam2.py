mystr='a,a,a,b,b,c,c,c'

mylist=mystr.split(',')

visited=[]

for ch in mylist:
    if ch not in visited:
        print(f"{ch}:{mylist.count} ",end=",")
        visited.append(ch)
        