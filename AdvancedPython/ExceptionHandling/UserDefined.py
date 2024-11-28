
# Write a python program for FiveDivisionError Exception

class FiveDivisionErro(Exception):
    def __init__(self):
        print("Cannot divide by 5")
    'this is happen when error happed'
     

try:
    n1=int(input("Enter the num1"))
    n2=int(input("Enter second num2"))
    if n2==5:
        raise FiveDivisionErro("Cannot divide by 5")
    div=n1/n2
    print("Division is :",div)
except(FiveDivisionErro,ZeroDivisionError) as var:
    print(var)