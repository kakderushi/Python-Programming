def BinarySearch(arr, n):
    left = 0
    right = len(arr) - 1
    
    while left <= right:
        mid = (left + right) // 2
        
        if arr[mid] == n:
            return mid
        elif arr[mid] < n:
            left = mid + 1  # Search in the right half
        else:
            right = mid - 1  # Search in the left half
            
    return -1  # If the element is not found

arr = [4, 7, 8, 12, 45, 99]
n = 45
res = BinarySearch(arr, n)
print(res)
