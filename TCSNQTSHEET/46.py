#occurence of elements in the array
from collections import Counter

n=int(input("Entersize of the array "))
arr=[]
print("Enter the array elements")
for _ in range(n):
    arr.append(int(input()))
occurences=Counter(arr)
print("Occurences of each elements")
for key , count in occurences.items():
    print(f"{key} occurs {count} times")