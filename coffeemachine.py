MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "coffee": 18,
        },
        "cost": 1.5,
    },
    "latte": {
        "ingredients": {
            "water": 200,
            "milk": 150,
            "coffee": 24,
        },
        "cost": 2.5,
    },
    "cappuccino": {
        "ingredients": {
            "water": 250,
            "milk": 100,
            "coffee": 24,
        },
        "cost": 3.0,
    }
}

resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
    "profit": 0,
}


def print_resource_report():
    print(f"Water: {resources['water']}ml")
    print(f"Milk: {resources['milk']}ml")
    print(f"Coffee: {resources['coffee']}g")
    print(f"Profit: ${resources['profit']}")


def process_coins(choice):
    print("Please insert coins")
    quarter = int(input("How many quarters?: "))
    dimes = int(input("How many dimes?: "))
    nickles = int(input("How many nickles?: "))
    pennies = int(input("How many pennies?: "))
    total_coins_value = (quarter * .25) + (dimes * .10) + (nickles * .05) + (pennies * .01)
    print(choice)
    if total_coins_value > MENU[choice]['cost']:
        money = total_coins_value - MENU[choice]['cost']
        change = [True, round(money, 2)]
        return change
    else:
        return False


def check_resources(choice):
    drink = MENU[choice]['ingredients']
    for key in drink:
        if drink[key] > resources[key]:
            check = [False, key]
            return check
    return [True, drink]


def update_resources(choice):
    drink = MENU[choice]['ingredients']
    for key in drink:
        resources[key] -= drink[key]


def process_transaction(choice):
    value = check_resources(choice)
    if value[0]:
        payment = process_coins(choice)
        if not payment:
            print("Sorry that's not enough money. Money refunded")
        else:
            print(f"Here is ${payment[1]} in change")
            print(f"Here is your {choice}, Enjoy!")
            update_resources(choice)
            resources['profit'] += MENU[choice]['cost']
    else:
        print(f"Sorry there is not enough {value[1]}")


is_on = True

while is_on:
    option = input("What would you like? (espresso/latte/cappuccino): ")
    if option == "off":
        is_on = False
    elif option == "report":
        print_resource_report()
    elif option == "espresso":
        process_transaction(option)
    elif option == "latte":
        process_transaction(option)
    elif option == "cappuccino":
        process_transaction(option)
    else:
        print("Please select a listed drink")
