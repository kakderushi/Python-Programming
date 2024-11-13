def swap(arr, start1, start2, d):
    for i in range(d):
        arr[start1 + i], arr[start2 + i] = arr[start2 + i], arr[start1 + i]

def rotateArray(arr, n, k):
    if k == 0 or k == n:
        return
    
    # If k > n, reduce it to within the array's bounds
    if k > n:
        k = k % n
    
    A_start = 0
    B_start = k
    while k != 0 and k != n:
        if k < n - k:
            swap(arr, A_start, n - k, k)
            n = n - k
        else:
            swap(arr, A_start, B_start, n - k)
            k = 2 * k - n
            A_start = n - k

def main():
    T = int(input("Enter number of test cases: "))
    
    while T > 0:
        # Read N and K
        nd = [int(x) for x in input("Enter N and K: ").strip().split()]
        N = nd[0]
        K = nd[1]
        
        # Read array elements
        array = [int(x) for x in input("Enter array elements: ").strip().split()]
        
        # Rotate array using Block Swap Algorithm
        rotateArray(array, N, K)
        
        # Print the rotated array
        for i in array:
            print(i, end=" ")
        print()
        
        T -= 1

if __name__ == "__main__":
    main()
