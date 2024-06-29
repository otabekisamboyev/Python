class MenuItem:
    def __init__(self, name, water, milk, coffee, cost):
        self.name = name
        self.cost = cost
        self.ingredients = {
            "water": water,
            "milk": milk,
            "coffee": coffee
        }


class Menu:
    def __init__(self):
        """Creating objects"""
        self.menu = {
            MenuItem(name="espresso", water=50, milk=0, coffee=18, cost=1.5),
            MenuItem(name="latte", water=200, milk=150, coffee=24, cost=2.5),
            MenuItem(name="cappuccino", water=250, milk=100, coffee=24, cost=3.0)
        }

    def get_items(self):
        """Returns all the name of the available menu items ad a concatenated string"""
        option = ''
        stop = 0
        for item in self.menu:
            if stop >= 2:
                option += f"{item.name}"
            else:
                option += f"{item.name}/"
            stop += 1
        return option

    def find_drink(self, order_name):
        """Searches the menu for a particular drink by name. Returns that item if it exists, otherwise returns None"""
        for item in self.menu:
            if item.name == order_name:
                return item
        print("Sorry that item is not available.")
