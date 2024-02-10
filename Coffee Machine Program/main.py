# Declaring global variables
espresso = {
    "water": 30,
    "milk": 35,
    "coffee": 20,
    "unit_price": 1.25,
}
latte = {
    "water": 35,
    "milk": 35,
    "coffee": 25,
    "unit_price": 1.45,
}
cappuccino = {
    "water": 40,
    "milk": 35,
    "coffee": 35,
    "unit_price": 1.75,
}
water = 100
milk = 400
coffee = 350
revenue = 0.00


# Global Variables: espresso, latte, cappuccino, water, milk, coffee, revenue


# function for checking if there are sufficient resources available for making the coffee
def check_resources(coffee_type):
    global espresso, latte, cappuccino, water, milk, coffee, revenue
    if coffee_type == 'espresso':
        if water >= espresso["water"] and milk >= espresso["milk"] and coffee >= espresso["coffee"]:
            water -= espresso["water"]
            milk -= espresso["milk"]
            coffee -= espresso["coffee"]
            return True
        else:
            return False
    elif coffee_type == 'latte':
        if water >= latte["water"] and milk >= latte["milk"] and coffee >= latte["coffee"]:
            water -= latte["water"]
            milk -= latte["milk"]
            coffee -= latte["coffee"]
            return True
        else:
            return False
    elif coffee_type == 'cappuccino':
        if water >= cappuccino["water"] and milk >= cappuccino["milk"] and coffee >= cappuccino["coffee"]:
            water -= cappuccino["water"]
            milk -= cappuccino["milk"]
            coffee -= cappuccino["coffee"]
            return True
        else:
            return False
    else:
        return False


# function for displaying the resources report with revenue
def display_report():
    print(f"""
    ------ Report of CoffeeManiac ------
    
    Water   :   {water} ml
    Milk    :   {milk} ml
    Coffee  :   {coffee} ml
    Revenue :   ${revenue}
""")


def get_change(coffee_type, cash):
    global espresso, latte, cappuccino

    if coffee_type == 'espresso':
        return cash - espresso["unit_price"]
    elif coffee_type == 'latte':
        return cash - latte["unit_price"]
    elif coffee_type == 'cappuccino':
        return cash - cappuccino["unit_price"]


# function for monitoring the successful transaction
def make_transaction(coffee_type, cash):
    global espresso, latte, cappuccino, revenue

    if coffee_type == 'espresso':
        if cash >= espresso["unit_price"]:
            revenue += espresso["unit_price"]
            return True
        else:
            return False
    elif coffee_type == 'latte':
        if cash >= latte["unit_price"]:
            revenue += latte["unit_price"]
            return True
        else:
            return False
    elif coffee_type == 'cappuccino':
        if cash >= cappuccino["unit_price"]:
            revenue += cappuccino["unit_price"]
            return True
        else:
            return False


def make_coffee(coffee_type, cash):
    print(f"""Making your {coffee_type} coffee.....""")
    print("Here you go. Enjoy the coffee.")
    change = get_change(coffee_type, cash)
    print(f"Your change amount is ${change}")


while True:
    print("""
    ----- Welcome to CoffeeManiac -----
    
    1. Espresso
    2. Latte
    3. Cappuccino
    4. Report
    5. Exit
""")
    user_choice = int(input("Enter your choice: "))

    if user_choice == 1:
        amount = float(input("Enter the cash amount: "))
        if make_transaction("espresso", amount):
            if check_resources("espresso"):
                make_coffee("espresso", amount)
            else:
                print("Sorry, there are not enough resources to make the coffee!")
        else:
            print("Sorry, you entered short amount.")
    elif user_choice == 2:
        amount = float(input("Enter the cash amount: "))
        if make_transaction("latte", amount):
            if check_resources("latte"):
                make_coffee("latte", amount)
            else:
                print("Sorry, there are not enough resources to make the coffee!")
        else:
            print("Sorry, you entered short amount.")
    elif user_choice == 3:
        amount = float(input("Enter the cash amount: "))
        if make_transaction("cappuccino", amount):
            if check_resources("cappuccino"):
                make_coffee("cappuccino", amount)
            else:
                print("Sorry, there are not enough resources to make the coffee!")
        else:
            print("Sorry, you entered short amount.")
    elif user_choice == 4:
        display_report()
    elif user_choice == 5:
        break
    else:
        print("Invalid command!")
