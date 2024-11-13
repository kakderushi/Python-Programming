# Quick Sort function
def quick_sort(arr):
    # Base case: if the array has 1 or 0 elements, it's already sorted
    if len(arr) <= 1:
        return arr
    else:
        # Choosing the pivot (here, we are choosing the last element as pivot)
        pivot = arr[-1]

        # Partitioning the array
        left = [x for x in arr[:-1] if x <= pivot]  # Elements less than or equal to pivot
        right = [x for x in arr[:-1] if x > pivot]  # Elements greater than pivot

        # Recursively applying quick_sort to the left and right parts
        return quick_sort(left) + [pivot] + quick_sort(right)

# Example usage:
arr = [38, 27, 43, 3, 9, 82, 10]
print("Original array:", arr)
sorted_arr = quick_sort(arr)
print("Sorted array:", sorted_arr)
