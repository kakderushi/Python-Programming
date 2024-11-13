
def printArray(arr,n):
    print("The reversed array is")
    for i in range(n):
        print(arr[i],end="")
        
    print()

def reverse(arr,n):
    ans=[0]*n
    for i in range(n-1,-1,-1):
        ans[n-i-1]=arr[i]
    printArray(ans,n)

# Driver code
if __name__=="__main__":
    arr=[5,4,3,2,1]
    n=len(arr)
    reverse(arr,n)