#Binary search using recursion
def binarySearch(arr, low, high, key):
    # base case: if the range is invalid, key is not present
    if low > high:
        return False
    
    # find the middle index
    mid = (low + high) // 2
    
    # check if the middle element is the key
    if arr[mid] == key:
        return True
    # if key is smaller, search in the left half
    elif key < arr[mid]:
        return binarySearch(arr, low, mid - 1, key)
    # if key is larger, search in the right half
    else:
        return binarySearch(arr, mid + 1, high, key)

# Example usage
arr = [1, 3, 5, 7, 9, 11, 13]
key = 7
n = len(arr)
ans = binarySearch(arr, 0, n - 1, key)

print(ans)  # Output will be True if the key is found, otherwise False
