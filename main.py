from coffee_data import MENU, resources

# TODO: 1. Prompt user by asking what coffee they would like
# Check user's input to decide next action
# Prompt should show every time an action has completed (Show again to serve the next customer)
def machine_start():
    """Starts the coffee machine"""
    machine_end = False
    while not machine_end:
        choice = input("What would you like to have? (espresso/latte/cappuccino): ")
        coffee = choice.lower()
        if coffee == "espresso" or coffee == "latte" or coffee == "cappuccino":
            if check_resources(coffee):
                if validate_transaction(calculate_money(), coffee):
                    make_coffee(coffee)
        elif coffee == "report":
            machine_report()
        elif coffee == "off":
            machine_end = machine_off()
        else:
            print("Invalid Choice.")



# TODO: 2. Turn off the coffee machine by entering 'off' to the prompt
"""To switch off machine when not in use"""
def machine_off():
    print("Machine switching off.. Goodbye")
    return True

# TODO: 3. Print the report
"""Generate a report to show the current resources in the machine"""
def machine_report():
    for key, value in resources.items():
        print(key, ":", value)


# TODO: 4. Check if resources are sufficient
"""Check if resources are enough to make the choice of coffee"""
# Code can be made better by using a for loop (looping through order_ingredients)
def check_resources(coffee):
    if resources["water"] < MENU[coffee]["ingredients"]["water"]:
        print("Sorry there is not enough water.")
        return False
    elif resources["coffee"] < MENU[coffee]["ingredients"]["coffee"]:
        print("Sorry there is not enough coffee.")
        return False
    elif coffee != "espresso":
        if resources["milk"] < MENU[coffee]["ingredients"]["milk"]:
            print("Sorry there is not enough milk.")
            return False
        else:
            return True
    else:
        return True


# TODO: 5. Process coins
# Prompt the user for coins to make the coffee
# Quarters = 0.25, Dimes = 0.10, Nickles = 0.05, Pennies = 0.01
"""Calculate and return the value of money received"""
def calculate_money():
    money = False
    while not money:
        try:
            print("Please insert coins.")
            quarters = int(input("How many quarters?: "))
            dimes = int(input("How many dimes?: "))
            nickles = int(input("How many nickles?: "))
            pennies = int(input("How many pennies?: "))
            money = True

        except ValueError:
            print("Money entered must be an integer.")

    coins_received = {
                    "quarters": quarters,
                    "dimes": dimes,
                    "nickles": nickles,
                    "pennies": pennies
    }

    total_value = coins_received["quarters"] * 0.25 + coins_received["dimes"] * 0.1 + coins_received["nickles"] * 0.05 + coins_received["pennies"] * 0.01
    return total_value

# TODO: 6. Check if transaction is successful
# Check if money received is enough to buy the choice of coffee
"""If money is enough, add money received to the machine as profit and display in report"""
# Offer change if required
def validate_transaction(money_received, coffee):
    if money_received < MENU[coffee]["cost"]:
        print("Sorry that's not enough money. Your money has been refunded")
        return False
    elif money_received >= MENU[coffee]["cost"]:
        change = money_received - MENU[coffee]["cost"]
        print(f"Here is ${round(change,2)} in change")
        resources["money"] = resources["money"] + money_received - change
        return True

# TODO 7. Make the coffee
"""If transaction is valid and there are enough ingredients, deduct ingredients needed from resources"""
# Code can be better by using a for-loop
def make_coffee(coffee):
    resources["water"] = resources["water"] - MENU[coffee]["ingredients"]["water"]
    resources["coffee"] = resources["coffee"] - MENU[coffee]["ingredients"]["coffee"]
    if coffee.lower() != "espresso":
        resources["milk"] = resources["milk"] - MENU[coffee]["ingredients"]["milk"]

    print(f"Here is your {coffee}. Enjoy!")

# TODO 8: Main program
machine_start()