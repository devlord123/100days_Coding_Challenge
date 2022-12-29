import pprint

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
report = {
    "water": "100ml",
    "milk": "50ml",
    "coffee": "76g",
    "money": 0
}


def resourse(item):
    if item == "espresso":
        men_water = MENU["espresso"]["ingredients"]["water"]
        res_water = resources["water"]
        men_cofee = MENU["espresso"]["ingredients"]["coffee"]
        res_cofee = resources["coffee"]
        if res_water > men_water:
            if res_cofee > men_cofee:
                print("Kindly insert your coin ")
            else:
                print("Sorry there is not enough coffee.")
        else:
            print("Sorry there is not enough water.")


    elif item == "latte":
        men_water = MENU["latte"]["ingredients"]["water"]
        res_water = resources["water"]
        men_cofee = MENU["latte"]["ingredients"]["coffee"]
        res_cofee = resources["coffee"]
        men_milk = MENU["latte"]["ingredients"]["milk"]
        res_milk = resources["milk"]
        if res_water > men_water:
            if res_cofee > men_cofee:
               if res_milk > men_milk:
                   print("Kindly insert your coin ")

               else:
                   print("Sorry there is not enough Milk.")
            else:
                print("Sorry there is not enough coffee.")
        else:
            print("Sorry there is not enough water.")

    elif item == "cappuccino":
        men_water = MENU["cappuccino"]["ingredients"]["water"]
        res_water = resources["water"]
        men_cofee = MENU["cappuccino"]["ingredients"]["coffee"]
        res_cofee = resources["coffee"]
        men_milk = MENU["cappuccino"]["ingredients"]["milk"]
        res_milk = resources["milk"]
        if res_water > men_water:
            if res_cofee > men_cofee:
               if res_milk > men_milk:
                   print("Kindly insert your coin ")
               else:
                   print("Sorry there is not enough Milk.")
            else:
                print("Sorry there is not enough coffee.")
        else:
            print("Sorry there is not enough water.")


def payment():
    quarters = int(input("How many quarters? "))
    dimes = int(input("How many dimes? "))
    nickles = int(input("How many nickles? "))
    penny = int(input("How many penny? "))
    q = quarters * 0.25
    d = dimes * 0.1
    n = nickles * 0.05
    p = penny * 0.01
    add = q + d + n + p
    return add

def transaction(item):
    if item == "espresso":
        cost = MENU["espresso"]["cost"]
        balance = payment()
        if cost > balance:
            print("Sorry that's not enough money. Money refunded.")
        else:
            report["money"] = balance
            #pprint.pprint(report)
            if balance > cost:
                new = balance - cost
                print(f"Your change is ${new:2}")
    elif item == "latte":
        cost = MENU["latte"]["cost"]
        balance = payment()
        if cost > balance:
            print("Sorry that's not enough money. Money refunded.")
        else:
            report["money"] = balance
            #pprint.pprint(report)
            if balance > cost:
                new = balance - cost
                print(f"Your change is ${new:2}")
    elif item == "cappuccino":
        cost = MENU["espresso"]["cost"]
        balance = payment()
        if cost > balance:
            print("Sorry that's not enough money. Money refunded.")
        else:
            report["money"] = balance
            #pprint.pprint(report)
            if balance > cost:
                new = balance - cost
                print(f"Your change is ${new:2}")

def make_coffee(item):
    if item == "espresso":
        men_water = MENU["espresso"]["ingredients"]["water"]
        res_water = resources["water"]
        men_cofee = MENU["espresso"]["ingredients"]["coffee"]
        res_cofee = resources["coffee"]
        water = res_water - men_water
        coffee = res_cofee - men_cofee
        resources["water"] = water
        resources["coffee"] = coffee
        resources["money"] = report["money"]
        #pprint.pprint(resources)
        print(f"Here is your {item}. Enjoy!")

    elif item == "latte":
        men_water = MENU["latte"]["ingredients"]["water"]
        res_water = resources["water"]
        men_cofee = MENU["latte"]["ingredients"]["coffee"]
        res_cofee = resources["coffee"]
        men_milk = MENU["latte"]["ingredients"]["milk"]
        res_milk = resources["milk"]
        water = res_water - men_water
        coffee = res_cofee - men_cofee
        milk = res_milk - men_milk
        resources["water"] = water
        resources["coffee"] = coffee
        resources["milk"] = milk
        resources["money"] = report["money"]
        #pprint.pprint(resources)
        print(f"Here is your {item}. Enjoy!")
    elif item == "cappuccino":
        men_water = MENU["cappuccino"]["ingredients"]["water"]
        res_water = resources["water"]
        men_cofee = MENU["cappuccino"]["ingredients"]["coffee"]
        res_cofee = resources["coffee"]
        men_milk = MENU["cappuccino"]["ingredients"]["milk"]
        res_milk = resources["milk"]
        water = res_water - men_water
        coffee = res_cofee - men_cofee
        milk = res_milk - men_milk
        resources["water"] = water
        resources["coffee"] = coffee
        resources["milk"] = milk
        resources["money"] = report["money"]
        #pprint.pprint(resources)
        print(f"Here is your {item}. Enjoy!")








machine = True

while machine:
    order = input("What would you like? (espresso/latte/cappuccino): ")
    if order == "report":
        for i, j in report.items():
            print(f"{i}: {j}")
    elif order == "off":
        machine = False
        print("Shutting Down.")
    if order == "espresso":
        resourse("espresso")
        transaction("espresso")
        make_coffee("espresso")
    elif order == "latte":
        resourse("latte")
        transaction("latte")
        make_coffee("latte")
    elif order == "cappuccino":
        resourse("cappuccino")
        transaction("cappuccino")
        make_coffee("cappuccino")


