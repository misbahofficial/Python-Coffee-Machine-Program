# This is a Coffee Machine Program with OOP approach

class Coffee:
    def __init__(self):
        self.espresso = {
            "water": 30,
            "milk": 35,
            "coffee": 20,
            "unit_price": 1.25,
        }
        self.latte = {
            "water": 35,
            "milk": 35,
            "coffee": 25,
            "unit_price": 1.45,
        }
        self.cappuccino = {
            "water": 40,
            "milk": 35,
            "coffee": 35,
            "unit_price": 1.75,
        }

        self.water = 100
        self.milk = 400
        self.coffee = 350
        self.revenue = 0.00

    def display_report(self):
        print(f"""
    ------ Report ------
    
    Water   :   {self.water} ml
    Milk    :   {self.milk} ml
    Coffee  :   {self.coffee} ml
    Revenue :   ${self.revenue}
""")

    def check_resources(self, coffee_type):
        if coffee_type == 'espresso':
            if self.water >= self.espresso['water'] and self.milk >= self.espresso['milk'] and self.coffee >= self.espresso['coffee']:
                self.water -= self.espresso['water']
                self.milk -= self.espresso['milk']
                self.coffee -= self.espresso['coffee']
                return True
            else:
                return False
        elif coffee_type == 'latte':
            if self.water >= self.latte['water'] and self.milk >= self.latte['milk'] and self.coffee >= self.latte['coffee']:
                self.water -= self.latte['water']
                self.milk -= self.latte['milk']
                self.coffee -= self.latte['coffee']
                return True
            else:
                return False
        elif coffee_type == 'cappuccino':
            if self.water >= self.cappuccino['water'] and self.milk >= self.cappuccino['milk'] and self.coffee >= self.cappuccino['coffee']:
                self.water -= self.cappuccino['water']
                self.milk -= self.cappuccino['milk']
                self.coffee -= self.cappuccino['coffee']
                return True
            else:
                return False
        else:
            return False

    def get_change(self, coffee_type, cash):
        if coffee_type == 'espresso':
            return cash - self.espresso['unit_price']
        elif coffee_type == 'latte':
            return cash - self.latte['unit_price']
        elif coffee_type == 'cappuccino':
            return cash - self.cappuccino['unit_price']

    def make_transaction(self, coffee_type, cash):
        if coffee_type == 'espresso':
            if cash >= self.espresso['unit_price']:
                self.revenue += self.espresso['unit_price']
                return True
            else:
                return False
        elif coffee_type == 'latte':
            if cash >= self.latte['unit_price']:
                self.revenue += self.latte['unit_price']
                return True
            else:
                return False
        elif coffee_type == 'cappuccino':
            if cash >= self.cappuccino['unit_price']:
                return True
            else:
                return False

    def make_coffee(self, coffee_type, cash):
        print(f"""Making your {coffee_type} coffee.....""")
        print("Here you go. Enjoy the coffee.")
        change = self.get_change(coffee_type, cash)
        print(f"Your change amount is ${change}")


coffee = Coffee()

while True:
    print("""
    ----- Welcome to CoffeeX -----

    1. Espresso
    2. Latte
    3. Cappuccino
    4. Report
    5. Exit
""")
    user_choice = int(input("Enter your choice: "))

    if user_choice == 1:
        amount = float(input("Enter the cash amount: "))
        if coffee.make_transaction("espresso", amount):
            if coffee.check_resources("espresso"):
                coffee.make_coffee("espresso", amount)
            else:
                print("Sorry, there are not enough resources to make the coffee!")
        else:
            print("Sorry, you entered short amount.")
    elif user_choice == 2:
        amount = float(input("Enter the cash amount: "))
        if coffee.make_transaction("latte", amount):
            if coffee.check_resources("latte"):
                coffee.make_coffee("latte", amount)
            else:
                print("Sorry, there are not enough resources to make the coffee!")
        else:
            print("Sorry, you entered short amount.")
    elif user_choice == 3:
        amount = float(input("Enter the cash amount: "))
        if coffee.make_transaction("cappuccino", amount):
            if coffee.check_resources("cappuccino"):
                coffee.make_coffee("cappuccino", amount)
            else:
                print("Sorry, there are not enough resources to make the coffee!")
        else:
            print("Sorry, you entered short amount.")
    elif user_choice == 4:
        coffee.display_report()
    elif user_choice == 5:
        break
    else:
        print("Invalid command!")
