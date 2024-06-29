class MakeCoffee:
    def __init__(self):
        """Models the machine that makes the coffee"""
        self.water = 300
        self.milk = 200
        self.coffee = 100
        self.resources = {
            "water": self.water,
            "milk": self.milk,
            "coffee": self.coffee
        }

    def is_resource_sufficient(self, drink):
        """Returns True when order can be made, False if ingredients are insufficient"""
        for item in drink.ingredients:
            if drink.ingredients[item] > self.resources[item]:
                print(f"Sorry there is not enough {item}.")
                return False
        return True

    def make_coffee(self, order):
        """Deducts the required ingredients from the resources and make the coffee"""
        for item in order.ingredients:
            self.resources[item] -= order.ingredients[item]
        return f"Here is your {order.name} 🍵. Enjoy 😊"

    def report(self):
        """Prints a report of all resources."""
        for item in self.resources:
            if item == "coffee":
                print(f"{item.title()}: {self.resources[item]}gr")
            else:
                print(f"{item.title()}: {self.resources[item]}ml")
