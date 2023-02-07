class ResourceBank:

    def __init__(self, drink_collection, available_resource):
        self.drink_collection = drink_collection
        self.available_resource = available_resource
        self.original_balance = 0

    def show_resource(self):
        """Checks the amount of resources left"""
        water_left = self.available_resource["water"]
        milk_left = self.available_resource["milk"]
        coffee_left = self.available_resource["coffee"]
        money_left = self.original_balance

        print(f"Water: {water_left}ml\nMilk: {milk_left}ml\nCoffee: {coffee_left}g\nMoney: ${money_left}")

    def check_resource(self, drink_selected):
        """Checks if resources available can make drink requested"""
        current_selection = self.drink_collection[drink_selected]
        for item in current_selection["ingredients"]:
            if self.available_resource[item] < current_selection["ingredients"][item]:
                return f"Sorry there is not enough {item}."

        return f"get coins"

    def coin_amount(self):
        """Returns total amount from coins inputted"""
        print("Please insert coins")
        quarters = int(input("How many quarters?: "))
        dimes = int(input("How many dimes?: "))
        nickels = int(input("How many nickels?: "))
        pennies = int(input("How many pennies?: "))

        total = float(((0.25 * quarters) + (0.10 * dimes) + (0.05 * nickels) + (0.01 * pennies)))

        return total

    def coin_process(self, total_money, drink_chosen):
        """Checks total amount inputted for refund or change"""
        working_selection = self.drink_collection[drink_chosen]
        if total_money < working_selection["cost"]:
            return 0
        elif total_money == working_selection["cost"]:
            return total_money
        elif total_money > working_selection["cost"]:
            change = total_money - working_selection["cost"]
            change_rounded = round(change, 2)
            return change_rounded

    def adjust_resource(self, drink_preferred):
        """Deducts resources for drinks made and tops up original balance"""
        print(f"Here is your {drink_preferred}. Enjoy!!!")
        present_selection = self.drink_collection[drink_preferred]
        for item in present_selection["ingredients"]:
            self.available_resource[item] -= present_selection["ingredients"][item]

        top_up = present_selection["cost"]
        self.original_balance += top_up

