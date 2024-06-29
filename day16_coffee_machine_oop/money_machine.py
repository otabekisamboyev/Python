class MoneyMachine:
    def __init__(self):
        self.profit = 0

    def proces_coin(self):
        """Returns the total calculated from coins inserted"""
        print("Please insert coins.")
        total = int(input("How many quarters?: ")) * 0.25
        total += int(input("How many dime?: ")) * 0.1
        total += int(input("How many nickel?: ")) * 0.05
        total += int(input("How many penny?: ")) * 0.01
        return total

    def is_transaction_successful(self, money_received, drink_cost):
        """Returns True when the payment is accepted,or False if money is insufficient """
        if money_received >= drink_cost.cost:
            change = round(money_received - drink_cost.cost, 2)
            print(f"Here is ${change} in change")
            self.profit += drink_cost.cost
            return True
        else:
            print("Sorry that's not enough money. Money refunded.")
            return False

    def report(self):
        """Prints a report of profit."""
        print(f"Money: {self.profit}$")
