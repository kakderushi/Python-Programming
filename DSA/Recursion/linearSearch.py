def linearSearch(arr, n, k):
    # base case: if the array is empty, return False
    if n == 0:
        return False
    # if the current element matches k, return True
    if arr[0] == k:
        return True
    # otherwise, check the remaining part of the array
    return linearSearch(arr[1:], n - 1, k)

arr = [3, 5, 1, 2, 6]
n = 5
k = 6
ans = linearSearch(arr, n, k)
print(ans)