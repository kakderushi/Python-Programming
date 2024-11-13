#Encapsulation 


'''
1. Class is blueprint
2.class consist of methods and attributes
3 self is 
'''

class Atm:
    def __init__(self):
        self.__pin = ''
        self.__balance = 0
        self.menu()
    def get_pin(self):
        return self.__pin
    
    def set_pin(self,new_pin):
        if type(new_pin)==str:
            
            self.__pin=new_pin
            print("Pin Changed")
        else:
            print("Not allowed")
    
    def menu(self):
        while True:
            user_input = input('''Hello, How would you like to use the machine?
1. Enter 1 to create PIN
2. Enter 2 to deposit money
3. Enter 3 to withdraw
4. Enter 4 to check the balance
5. Enter 5 to exit\n''')
            
            if user_input == '1':
                self.create_pin()
                
            elif user_input == '2':
                self.deposit()
        
            elif user_input == '3':
                self.withdraw()
                
            elif user_input == '4':
                self.check_balance()
                
            elif user_input == '5':
                print("Goodbye!")
                break
                
            else:
                print("Invalid option. Please try again.")
                
    def create_pin(self):
        self.pin = input('Enter your PIN: ')
        print("PIN set successfully")
        
    def deposit(self):
        temp = input("Enter your PIN: ")
        if temp == self.pin:
            try:
                amount = int(input("Enter the amount to deposit: "))
                if amount > 0:
                    self.balance += amount
                    print("Deposit successful")
                else:
                    print("Invalid amount")
            except ValueError:
                print("Invalid input. Please enter a number.")
        else:
            print('Invalid PIN')
        
    def withdraw(self):
        temp = input("Enter your PIN: ")
        if temp == self.pin:
            try:
                amount = int(input("Enter the amount to withdraw: "))
                if amount > 0:
                    if amount <= self.balance:
                        self.balance -= amount
                        print("Withdrawal successful")
                    else:
                        print("Insufficient funds")
                else:
                    print("Invalid amount")
            except ValueError:
                print("Invalid input. Please enter a number.")
        else:
            print("Invalid PIN")
            
    def check_balance(self):
        temp = input("Enter your PIN: ")
        if temp == self.pin:
            print(f"Your balance is: {self.balance}")
        else:
            print("Invalid PIN")
            
# Create an instance of the Atm class
sbi = Atm()
