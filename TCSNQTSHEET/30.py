#Check wheather a number is perfect number or not

# Perfect number is : if all divisor of this number sum is equal to itself but excludig itself

def checkPerfectNumber(num):
    if num<=1:
        return False
    
    sum=0
    for i in range(1,num):
        if num%i==0:
            sum=sum+i
            
    if sum==num:
        return True
    else:
        return False
        

num=int(input()) # (6 )==1+2+3=6 
res=checkPerfectNumber(num)
print(res)



