class Solution: 
    def firstAndLast(self, x, arr):
        def binary_search_left(arr, x):
            left, right = 0, len(arr) - 1
            first_occurrence = -1
            while left <= right:
                mid = (left + right) // 2
                if arr[mid] == x:
                    first_occurrence = mid
                    right = mid - 1  # Continue to search in the left half
                elif arr[mid] < x:
                    left = mid + 1
                else:
                    right = mid - 1
            return first_occurrence

    
            
        def BinarySearchRight(arr,x):
            left, right = 0, len(arr) - 1
            last_occurrence = -1
            while left <= right:
                mid = (left + right) // 2
                if arr[mid] == x:
                    last_occurrence = mid
                    left = mid + 1  # Continue to search in the right half
                elif arr[mid] < x:
                    left = mid + 1
                else:
                    right = mid - 1
            return last_occurrence
            
            
            
        first=binary_search_left(arr,x)
        if first==-1:
            return [-1]
            
        last=BinarySearchRight(arr,x)
        return [first, last]


if  __name__  =="__main__":
    t=int(input())
    for _ in range(t):
        x =int(input())
        arr=[int (i) for i in  input().split()]
        ob=Solution()
        ans=ob.firstAndLast(x, arr)
        print(ans)
        
        