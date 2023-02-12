from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine
coffee = CoffeeMaker()
money = MoneyMachine()
menu = Menu()
def coffeemaker():
    opitons = menu.get_items()
    prompt = input(f"What would you like {opitons}: ")
    if prompt == "off":
        return
    elif prompt=="report":
        coffee.report()
        money.report()
        coffeemaker()
    else:
        order_name = menu.find_drink(prompt)
        if coffee.is_resource_sufficient(order_name) and money.make_payment(order_name.cost):
            coffee.make_coffee(order_name)
            coffeemaker()
        else:
            coffeemaker()

        # if x == False:
        #     print("Sorry there is not enough resources")
        #     coffemaker()
        # else:
        #     y = money.make_payment(order_name.cost)
        #     if y == False:
        #         print("Sorry not enough money. Money refunded")
        #     else:


coffeemaker()