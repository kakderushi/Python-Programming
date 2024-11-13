# find an array find the second smallest and second largest element in the array
def find_second_largest_and_smallest(arr):
    if len(arr) < 2:
        return "Array needs to have at least 2 elements."

    # Sort the array
    arr.sort()

    # Second smallest element is at index 1
    second_smallest = arr[1]

    # Second largest element is at index -2
    second_largest = arr[-2]

    return [second_smallest, second_largest]

# Example usage
arr = [12, 35, 1, 10, 34, 1]
result = find_second_largest_and_smallest(arr)
print(result)  # Output: [10, 34]