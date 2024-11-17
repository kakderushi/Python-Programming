'''
input:  [5,3,1,4,3,7,6,9,2]
maximum product pair is: (7,9)


input: [0,-2,-1,-4,5,-8,7,-8,8]
output: Maximum product pair is (-8,8)


'''

def max_product(arr):
    a_len=len(arr)
    if a_len <2:
        print("No such pair exist")
        return
    
    a=arr[0]
    b=arr[1]
    
    for i in range(0,len(arr)):
        for j in range(i+1,len(arr)):
            if arr[i]*arr[j]>(a*b):
                a=arr[i]
                b=arr[j]
    return a,b


arr=eval(input("Enter array"))
print("Maximum Product pair is :",max_product(arr))
    