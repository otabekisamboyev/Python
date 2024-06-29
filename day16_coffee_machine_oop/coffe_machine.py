from coffee_maker import MakeCoffee
from menu import Menu
from money_machine import MoneyMachine


money_machine = MoneyMachine()
coffee_maker = MakeCoffee()
menu = Menu()

is_on = True

while is_on:
    options = menu.get_items()
    choice = input(f"What would you like? ({options}): ")
    if choice == "off":
        is_on = False
    elif choice == "report":
        money_machine.report()
        coffee_maker.report()
    else:
        drink = menu.find_drink(choice)
        if coffee_maker.is_resource_sufficient(drink):
            received_money = money_machine.proces_coin()
            if money_machine.is_transaction_successful(received_money, drink):
                print(coffee_maker.make_coffee(drink))
