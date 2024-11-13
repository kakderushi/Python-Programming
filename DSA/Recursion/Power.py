def power(a,b):
    #base case
    if b==0:
        return 1
    if b==1:
        return a
    
    #Recursive call
    ans=power(a, b//2)
    
    if b%2==0:
        return ans*ans
    else:
        return a*ans*ans
    
    
a=12
b=10
ans=power(a,b)
print(ans)