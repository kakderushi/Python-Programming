'''
Exception :
An exception is an event which occurs during the
execution of program that disrupts normal flow of program


situation that python can't cope with it


Why it is dangerous:

1) Lead to sudden termination of program
2) can block the application
3) Data loss Problem can occur
4) corrupt data files
'''


'''

There are 4 block which python provide us inorder to handle exception
 try block
 except block
 else block
 finally block
'''

'''
num1=int(input("enter the num1"))
num2=int(input("enter the num2"))
try:
    div=num1/num2
    print(div)
except ZeroDivisionError:
    print("Divide by zero is not possible")
except NameError:
    print("variable name is wrong")
    
'''
# If we not aware about which type of exception are occured then use this code
'''
num1=int(input("enter the num1"))
num2=int(input("enter the num2"))
try:
    div=num1/num2
    print(div)
except Exception as var:
    print(var)
    print(var.__class__)

'''
# now third way
import sys
num1=int(input("enter the num1"))
num2=int(input("enter the num2"))
try:
    div=num1/num2
    print(div)
except:
    print(sys.exc_info()[0]) # exception name
    print(sys.exc_info()[1]) # exception information
    
