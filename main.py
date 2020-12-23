from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine


machine_stop = False
menu = Menu()
espresso = MenuItem("espresso", 50,  0,  18, 1.5)
latte = MenuItem("latte",  200, 150,  24, 2.5)
cappuccino = MenuItem("cappuccino", 250, 100, 24, 3.0)
coffeemachine = CoffeeMaker()
moneymachine= MoneyMachine()

menu_list = []
menu_list.append(espresso)
menu_list.append(latte)
menu_list.append(cappuccino)

while not machine_stop:
    user_coffee_choice = input(f"What would you like? {menu.get_items()}: ")
    if user_coffee_choice == "off":
        machine_stop = True
    elif user_coffee_choice == "report":
        print(coffeemachine.report(), moneymachine.report())
    elif menu.find_drink(user_coffee_choice):
        for i in menu_list:
            if i.name == user_coffee_choice and coffeemachine.is_resource_sufficient(i) and moneymachine.make_payment(i.cost):
                coffeemachine.make_coffee(i)