'''
what is Function:
function is an organized block of reusable code
functions can be called any number of times
functions contains a set of instructions which perform specific tasks 
'''
'''
def functionName([parameters]):

parameters : 

it also called formal arugments 
it is varibale which will pass to the functions

arguments: 

arguments are actual values which will provide to the functions 
it is also called actual arguments


'''

def simple_intrest(p,n,r):
    print("Principle amount is :",p)
    print("Number of years: ",n)
    print("Rate of intrest :",r)
    si=(p*r*n)/100
    print("simple interes :",si)
    
#function call
si=simple_intrest(1000,2.23,4)
si=simple_intrest(100,2.23,4)
si=simple_intrest(100,2.23,4)


    