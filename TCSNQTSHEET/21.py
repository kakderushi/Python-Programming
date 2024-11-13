class Solution:
    def nextGreastest(self,arr):
        
        n = len(arr)
    # Initialize the maximum element on the rightmost side
        max_from_right = -1
    
    # Traverse the array from right to left
        for i in range(n-1, -1, -1):
        # Store the current element
            current = arr[i]
        
        # Replace the current element with the max from right
            arr[i] = max_from_right
        
        # Update the max_from_right
            max_from_right = max(max_from_right, current)
    
        return arr
	    

if __name__=="__main__":
    
    t=int(input())
    while t>0:
        arr=list(map(int,input().split()))
        ob=Solution()
        ans=ob.nextGreastest(arr)
        print(*ans)
        t=t-1
        




