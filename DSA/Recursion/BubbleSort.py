def BubbleSort(arr,n):
    #base case
    if n==0 or n==1:
        return 
    
    #here solve one case
    for i in range(0,len(arr)-1):
        if arr[i]>arr[i+1]:
            arr[i],arr[i+1]=arr[i+1], arr[i]
    #This is the Recursive call for this function 
    BubbleSort(arr,n-1)
        
         
arr=[1,5,7,2,3]
n=len(arr)
BubbleSort(arr,n)
print(arr)