from sys import *
from collections import *
from math import *
# largeset element inside the array
def largestElement(arr: [], n: int) -> int:
    arr.sort()
    return arr[n-1]


arr=[12,23,446,12]
value=largestElement(arr,4)
print(value)