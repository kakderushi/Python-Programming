'''

A company has decided to give some gifts to all its employee
for that , the comapny has given rank to each employee based ont that,
the company has made certain rules to distribute the gifts

the rules for distributing the giffs 
1) each emp must receive at least one gift
2) emp having higher ranking get a greater number of gifts than their neigbours
3) what is the minimum number of gifts required by the company

input format:
first line contains intger T denoting the number of test cases
for each test case:
first line contains integer N, denoting the number of emp
second line contains N space separated intergers denoting the rank of each emp


output format:
for each test case  print the number of minimum gifts required on a new line

EXample:
input: 
 1# test case
 5 #no of emp
 1 2 1 5 2 # rank of emp
 
 
output:
7 

'''
# test case
t=int(input())

while t>0:
    # number of emp
    n=int(input())
    # rank of emp
    emp=list(map(int, input().split()))
    gift=[1]
    
    for i in range(1,n):
        if emp[i] > emp[i-1]:
            gift.append(gift[i-1]+1)
        else:
            gift.append(1)
    for i in range(n-2,-1,-1):
        if emp[i]>emp[i+1]:
            gift[i]=max(1+gift[i+1],gift[i])
    print(sum(gift)) 
    
