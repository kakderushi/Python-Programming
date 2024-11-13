'''
static Method:
Methods which performs operations on external data
It can also perfom operations on class data
No need to pass object or class reference 
Creating using decorator @staticmethod
'''

class Bank:
    bankName='BOI'
    rateOfIntrest=12.65
    
    @staticmethod
    def simpleIntrest(prin,n):
        si=(prin*n*Bank.rateOfIntrest)/100
        print(si)
        
prin=float(input("Enter principle amount"))
n=int(input("Enter the number of years"))
Bank.simpleIntrest(prin,n)