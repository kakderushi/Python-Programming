#Q1. Jack and Jill are playing a string game. 
# Jack has given Jill two strings A and B. Jill has to derive a string C from A, 
# by deleting elements from string A, such that string C does not contain any element of string B. Jill needs help to do this task.
# She wants a program to do this as she is lazy. Given strings A and B as input, give string C as Output.




# INPUT
# input A: tiger
# input B: ti 
#output ger


def deriveString(A, B):
    C=""
    #iterate through each character in string A
    for char in A:
        if char not in B:
            C+=char
    return C

A=input("Enter the input A")
B=input("Enter the input B")

result=deriveString(A,B)
print("the drived string will be",result)
