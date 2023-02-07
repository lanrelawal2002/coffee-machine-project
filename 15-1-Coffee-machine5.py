# my fifth version of the coffee machine project
# I incorporated Angela's dictionary key looping method.
# topped up money by using a function with a return value.
# and I simplified the section of code for printing change.


def show_resources():
    """Checks the amount of resources left"""
    water_left = resources["water"]
    milk_left = resources["milk"]
    coffee_left = resources["coffee"]
    money_left = original_balance

    print(f"Water: {water_left}ml\nMilk: {milk_left}ml\nCoffee: {coffee_left}g\nMoney: ${money_left}")


def check_resources(current_dict, resources_dict):
    """Checks if resources available can make drink requested"""
    for item in current_dict["ingredients"]:
        if resources_dict[item] < current_dict["ingredients"][item]:
            return f"Sorry there is not enough {item}"

    return f"get coins"


def coin_amount():
    """Returns total amount from coins inputted"""
    print("Please insert coins")
    quarters = int(input("How many quarters?: "))
    dimes = int(input("How many dimes?: "))
    nickels = int(input("How many nickels?: "))
    pennies = int(input("How many pennies?: "))

    total = float(((0.25 * quarters) + (0.10 * dimes) + (0.05 * nickels) + (0.01 * pennies)))

    return total


def coin_process(total_money, working_dict):
    """Checks total amount inputted for refund or change"""
    if total_money < working_dict["cost"]:
        return 0
    elif total_money == working_dict["cost"]:
        return total_money
    elif total_money > working_dict["cost"]:
        change = total_money - working_dict["cost"]
        change_rounded = round(change, 2)
        return change_rounded


def adjust_resources(resources_dict, working_dict, original_amount):
    """Deducts resources for drink made and tops up money for drink"""
    for item in working_dict["ingredients"]:
        resources_dict[item] -= working_dict["ingredients"][item]

    additional_money = working_dict["cost"]
    original_amount += additional_money

    return original_amount


MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "coffee": 18
        },
        "cost": 1.5
    },
    "latte": {
        "ingredients": {
            "water": 200,
            "milk": 150,
            "coffee": 24
        },
        "cost": 2.5
    },
    "cappuccino": {
        "ingredients": {
            "water": 250,
            "milk": 100,
            "coffee": 24
        },
        "cost": 3.0
    }
}

resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100
}

original_balance = 0
game_run_outer = True

while game_run_outer:
    user_request = input("What would you like? (espresso/latte/cappuccino): ")
    if user_request == "off":
        game_run_outer = False
    elif user_request == "report":
        show_resources()
    elif user_request == "espresso" or user_request == "latte" or user_request == "cappuccino":
        drink_dict = MENU[user_request]
        resource_verdict = check_resources(drink_dict, resources)
        if resource_verdict == "get coins":
            total_amount = coin_amount()
            money_returned = coin_process(total_amount, drink_dict)
            if money_returned == 0:
                print(f"Sorry that's not enough money. Money refunded.")
            # elif total_amount == money_returned:
            #     print(f"Here is your {user_request}. Enjoy!!!")
            #     top_up = adjust_resources(resources, drink_dict, original_balance)
            #     original_balance = top_up
            # elif total_amount > money_returned:
            #     print(f"Here is ${money_returned} in change.")
            #     print(f"Here is your {user_request}. Enjoy!!!")
            else:
                if total_amount > money_returned:
                    print(f"Here is ${money_returned} in change.")
                print(f"Here is your {user_request}. Enjoy!!!")
                top_up = adjust_resources(resources, drink_dict, original_balance)
                original_balance = top_up
        else:
            print(resource_verdict)
    else:
        print(f"enter either 'espresso' 'latte' 'cappuccino' 'report' or 'off'")
