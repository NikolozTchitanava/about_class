MENU = {
    'espresso': {
        'ingredients': {
            'coffee': 19,
            'water': 35,
        },
        'price': 1.99,
    },
    'latte': {
        'ingredients': {
            'coffee': 24,
            'water': 50,
            'milk': 150,
        },
        'price': 2.39,
    },
    'flat white': {
        'ingredients': {
            'coffee': 24,
            'water': 60,
            'milk': 50,
        },
        'price': 3.19,
    }
}

INVENTORY = {
    'coffee': 100,
    'water': 300,
    'milk': 300,
    'money': 0,
}

def check_resources(drink):
    for ingredient, amount_required in MENU[drink]['ingredients'].items():
        if INVENTORY[ingredient] < amount_required:
            print(f"Sorry, there is not enough {ingredient}.")
            return False
    return True

def process_coins():
    print("Please insert coins.")
    total_money_inserted = 0
    total_money_inserted += int(input("How many quarters? ")) * 0.25
    total_money_inserted += int(input("How many dimes? ")) * 0.10
    total_money_inserted += int(input("How many nickels? ")) * 0.05
    total_money_inserted += int(input("How many pennies? ")) * 0.01
    return total_money_inserted

def make_coffee(drink):
    for ingredient, amount_required in MENU[drink]['ingredients'].items():
        INVENTORY[ingredient] -= amount_required
    INVENTORY['money'] += MENU[drink]['price']
    print(f"Here is your {drink}. Enjoy!")

while True:
    choice = input("What would you like? (espresso/latte/cappuccino): ").lower()

    if choice == 'off':
        break
    elif choice == 'report':
        print(f"Water: {INVENTORY['water']}ml")
        print(f"Milk: {INVENTORY['milk']}ml")
        print(f"Coffee: {INVENTORY['coffee']}g")
        print(f"Money: ${INVENTORY['money']:.2f}")
    elif choice in MENU:
        if check_resources(choice):
            money_inserted = process_coins()
            drink_price = MENU[choice]['price']
            if money_inserted < drink_price:
                print("Sorry, that's not enough money.  refunded:",money_inserted)
            else:

                change = money_inserted - drink_price
                if change > 0:
                    print(f"Here is ${change:.2f} dollars in change.")
                make_coffee(choice)
        else:
            continue
    else:
        print("Invalid input. Please select a valid option.")
