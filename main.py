from menu import Menu
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine


coffee_maker=CoffeeMaker()
money_machine=MoneyMachine()
menu=Menu()

machine_on=True


while machine_on:
    order_options=menu.get_items() 
    user_choice=input(f"Enter what would you like to have☕?{order_options}")
    if user_choice =="off":
        machine_on=False
    elif user_choice =="report":
        coffee_maker.report()
        money_machine.report()
    else:
        drink_name=menu.find_drink(user_choice)
        if coffee_maker.is_resource_sufficient(drink_name) and money_machine.make_payment(drink_name.cost):
            coffee_maker.make_coffee(drink_name)
