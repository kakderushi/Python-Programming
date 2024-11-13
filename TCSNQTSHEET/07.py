# Calcualte sum of the elements of the array
def sum_of_the_array(array):
    return sum(array)


# input number of test cases
T=int(input("Enter the Number of test cases"))

# loop through each test case
for _ in range(T):
    #input size of the array
    N=int(input("Enter the size of the array"))
    # input for the array elements
    
    array=list(map(int,input("Enter the element  in the array").split()))
    
    #calculate the sum of the array
    print(sum_of_the_array(array))
