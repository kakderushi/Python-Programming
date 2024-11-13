'''
# Find the smallest element in an array
def find_smallest_element(arr):
    if not arr:
        return None # return None if the array is empty
    smallest=arr[0]
    for num in arr:
        if num<smallest:
            smallest=num
    return smallest



arr=[2,5,1,3,12]
smallest_element=find_smallest_element(arr)
print(smallest_element)
'''




def smallest_element(arr):
    arr.sort()
    return arr[0]
    
    

arr=[12,23,12,35]
small=smallest_element(arr)
print(small)