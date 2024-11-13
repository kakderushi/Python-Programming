#Insertion sort

def insertion_sort(arr):
    for i in range(1,len(arr)):
        #Here we store the second element of the array
        temp=arr[i]
        #Here we store the first element index inside the j variable
        j=i-1
        '''
        1. Here we check j>=0 value until it beacme the zero 
        then also check the temp values with arr[j] values until it bacame the less than temp
        
        let's dry run:
        12 11 13 5 6
        temp=11
        j=0 => which is 12 values
        
        let's come up with while loop
        j value is equal to 0 => first condition is true
        temp=11 and j=12  here also our codnito is true beacuse the 11 < 12 11 is less than the 12
        then here we assign the values of arr[j] which is 12 to arr[j+1]with 11
        then decrease the j values by 1
        then also store the values of 
        arr[j+1]= temp
        
        
        '''
        while j>=0 and temp<arr[j]:
            arr[j+1]=arr[j]
            j-=1
        arr[j+1]=temp
            



arr=[12,11,13,5,6]

print("Original list", arr)
insertion_sort(arr)
print(arr)