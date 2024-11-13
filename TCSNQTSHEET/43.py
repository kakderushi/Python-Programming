class Solution:
    def minIncrements(self, arr, N):
        arr.sort()
        
        operation = 0
        
        for i in range(1,N):
            if arr[i]<=arr[i-1]:
                operation = operation+arr[i-1]-arr[i]+1
                arr[i] = arr[i-1]+1
        return operation 
        
        
if __name__ == "__main__":
    t=int(input())
    while t>0:
        n=int(input())
        arr=[int (i) for i in input().split()]
        ob=Solution()
        print(ob.minIncrements(arr,n))
        t-=1