class Coffee:
    
    def __init__(self,name,water,milk,coffee_beans,cost):
        self.name=name
        self.water=water
        self.milk=milk
        self.coffee_beans=coffee_beans
        self.cost=cost
        
        
class CoffeeMachine:
    def __init__(self,water,milk,coffee_beans,money=0):
        self.water=water
        self.milk=milk
        self.coffee_beans=coffee_beans
        self.money=money
            
        self.menu=[
                Coffee("Espresso", 50, 0, 18, 1.5),
            Coffee("Latte", 200, 150, 24, 2.5),
            Coffee("Cappuccino", 250, 100, 24, 3.0)
            ]
    def report(self):
        print(f"Water: {self.water}ml")
        print(f"Milk: {self.milk}ml")
        print(f"Coffee Beans: {self.coffee_beans}g")
        print(f"Money: ${self.money}")

    def check_res(self,coffee):
        if self.water < coffee.water:
            print("sorry, not enough water")
            return False
        if self.milk < coffee.milk:
            print("Sorry, not enough milk!")
            return False
        if self.coffee_beans < coffee.coffee_beans:
            print("Sorry, not enough coffee beans!")
            return False
        return True
    
    def process_payment(self, cost):
        print(f"Please insert ${cost}")
        total_inserted = float(input("Enter amount inserted: "))
        if total_inserted < cost:
            print("Sorry, not enough money. Money refunded.")
            return False
        elif total_inserted > cost:
            change = round(total_inserted - cost, 2)
            print(f"Here is your change: ${change}")
        self.money += cost
        return True
    
    def make_coffee(self, coffee):
        if self.check_resources(coffee):
            if self.process_payment(coffee.cost):
                self.water -= coffee.water
                self.milk -= coffee.milk
                self.coffee_beans -= coffee.coffee_beans
                print(f"Here is your {coffee.name}. Enjoy!")
           
    def start(self):
        while True:
            choice = input("What would you like? (Espresso/Latte/Cappuccino): ").lower()
            if choice == "off":
                print("Turning off the machine. Goodbye!")
                break
            elif choice == "report":
                self.report()
            else:
                for coffee in self.menu:
                    if coffee.name.lower() == choice:
                        self.make_coffee(coffee)
                        break
                else:
                    print("Invalid choice. Please select a valid coffee.")

# Initialize the coffee machine with some resources
coffee_machine = CoffeeMachine(water=500, milk=500, coffee_beans=100)

# Start the coffee machine
coffee_machine.start()