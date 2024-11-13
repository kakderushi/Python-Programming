
#Rearrange array in increasing-decreasing order
# sort the whole array 
# then print the first half of the array in the ascending order
# then the reverse the array 


def RearrangeArray(arr,n):
    # sort the entire array in ascending order
    arr.sort()
    #find the midpoint
    n=len(arr)
    mid=n//2
    # first half of the array
    first_half=arr[:mid]
    
    #second half of the array
    second_half=arr[mid:][::-1]
    
    # combine the first and second half of the array
    rearranged_array=first_half+second_half
    
    return rearranged_array
    
    


if __name__ =="__main__":
    arr=[8,7,1,6,5,9]
    n=len(arr)
    output=RearrangeArray(arr,n)
    print(output)
    
