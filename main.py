# my implementation of the coffee machine using oop
from factory import MENU, resources
from resource_control import ResourceBank

checker = ResourceBank(MENU, resources)
serve = True
while serve:
    user_request = input("What would you like? (espresso/latte/cappuccino): ")
    if user_request == "off":
        serve = False
    elif user_request == "report":
        checker.show_resource()
    elif user_request == "espresso" or user_request == "latte" or user_request == "cappuccino":
        verdict_on_resource = checker.check_resource(user_request)
        if verdict_on_resource == "get coins":
            total_amount = checker.coin_amount()
            money_returned = checker.coin_process(total_amount, user_request)
            if money_returned == 0:
                print(f"Sorry that's not enough money. Money refunded.")
            else:
                if total_amount > money_returned:
                    print(f"Here is ${money_returned} in change.")
                checker.adjust_resource(user_request)
        else:
            print(verdict_on_resource)
    else:
        print(f"enter either 'espresso' 'latte' 'cappuccino' 'report' or 'off'")
