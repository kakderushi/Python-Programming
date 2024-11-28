'''
Requirments:
Balance in bank should not be less than 1000

user account will be blocked for an hour if user put 3 times wrong pin
'''
import time 
class BalanceExceptionError(Exception):
    pass

class AttemptExcetion(Exception):
    pass
attempt=1
def withdraw():
    global attempts
    saved_pin=1234
    balance=10000
    pin=input("Enter the PIN")
    if pin==saved_pin:
        try:
            amt=float(input("Enter amount to be withdeaw"))
            temp_balance=balance-amt
            if temp_balance<1000:
                raise BalanceExceptionError('insufficent Balance')
            balance=balance-amt
            print("Remained balance is :",balance)
            
        except Exception as var:
            print(var)
        else:
            ans=input("Do you want to continye again:(y/n):")
            if ans.lower()=='y':
                attempt+=1
                try:
                    if attempt==4:
                       raise AttemptExcetion("Two many attempt your accout for an hour")
                except Exception as var:
                    time.sleep(3600)
                    print(var) 
                else:
                    withdraw()
            else:
                print("Thank you")
                return 
            
            
withdraw()