import os

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
}


# Main 
end_of_program = False
while(not end_of_program):
    print("Welcome to the Coffee House!")
    # TODO: 1. Prompt user by asking “What would you like? (espresso/latte/cappuccino):”
    custormer_choice = input("What would you like? (espresso/latte/cappuccino): ").lower()
    # TODO: 2. Turn off the Coffee Machine by entering “off” to the prompt.
    if custormer_choice == "off":
        print("Turning off the machine")
        end_of_program=True
    # TODO: 3. Print report.
    elif custormer_choice == "report":
        print(f"Water: {resources['water']}ml")
        print(f"Milk: {resources['milk']}ml")
        print(f"Coffee: {resources['coffee']}g")
    # TODO: 4. Check resources sufficient?
    elif custormer_choice in MENU.keys():
        drink = MENU[custormer_choice]
        if custormer_choice=="espresso":
            drink["ingredients"]["milk"]=0
        if resources["water"] < drink["ingredients"]["water"]:
            print("Sorry there is not enough water.")
        elif resources["coffee"] < drink["ingredients"]["coffee"]:
            print("Sorry there is not enough coffee.")
        elif resources["milk"] < drink["ingredients"]["milk"]:
            print("Sorry there is not enough milk.")
        else:
            print("Please insert coins.")
            quarters=input("How many quarters?: ")
            dimes=input("How many dimes?: ")
            nickles=input("How many nickles?: ")
            pennies=input("How many pennies?: ")
            total_money = float(quarters)*0.25 + float(dimes)*0.1 + float(nickles)*0.05 + float(pennies)*0.01
            if total_money < drink["cost"]:
                print("Sorry that's not enough money. Money refunded.")
            else:
                change = total_money - drink["cost"]
                print(f"Here is ${change} in change.")
                print(f"Here is your {custormer_choice} ☕. Enjoy!")
                resources["water"] -= drink["ingredients"]["water"]
                resources["milk"] -= drink["ingredients"]["milk"]
                resources["coffee"] -= drink["ingredients"]["coffee"]
    else:
        print("You've enter wrong selection, re-check it!")
