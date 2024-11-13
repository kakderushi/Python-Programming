import math
#bubble sort 
# Here we compare elements and place the maximum value at the end of the array
def sort(nums):
    for i in range(0,len(nums)-1):
        for j in range(len(nums)-1):
            if nums[j] >nums[j+1]:
                nums[j],nums[j+1]=nums[j+1], nums[j]
    return nums
                
nums=[5,3,8,6,7,2]
sort(nums)
print(nums)