from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

menu = Menu()
coffee = CoffeeMaker()
money = MoneyMachine()


machine = True
while machine:
    order = input(f"The items available are {menu.get_items()}, make your order: ")

    if order == "report":
        coffee.report()
        money.report()
    elif order == "off":
        machine = False
        print("Power Off")
    else:
        drink = menu.find_drink(order)
        if coffee.is_resource_sufficient(drink) and money.make_payment(drink.cost):
            coffee.make_coffee(drink)