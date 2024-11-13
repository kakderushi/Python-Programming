'''Optimized approach: Following a bottom-up approach to reach the desired index. This approach of converting recursion into iteration is known as Dynamic programming(DP).

Observations:

Finally, what we do is recursively call each response index field and calculate its value using previously saved outputs. 
Recursive calls terminate via the base case, which means we are already aware of the answers which should be stored in the base case indexes. 
In the case of Fibonacci numbers, these indices are 0 and 1 as f(ib0) = 0 and f(ib1) = 1. So we can directly assign these two values ​​into our answer array and then use them to calculate f(ib2), which is f(ib1) + f(ib0), and so on for each subsequent index. 
This can easily be done iteratively by running a loop from i = (2 to n). Finally, we get our answer at the 5th index of the array because we already know that the ith index contains the answer to the ith value.
Simply, we first try to find out the dependence of the current value on previous values ​​and then use them to calculate our new value. Now, we are looking for those values which do not depend on other values, which means they are independent(base case values, since these, are the smallest problems
which we are already aware of).'''

def fibo(n):
    ans=[None]*(n+1)
    #storing the independent values in the answer array
    ans[0]=0
    ans[1]=1
    #using the bottom up approach
    for i in range(2,n+1):
        ans[i]=ans[i-1]+ans[i-2]
    return ans[n]

n=5
print(fibo(n))    