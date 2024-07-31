# 4. Display Menu
def display_menu(menu):

    for category in menu.keys():
        for dish in menu[category]:
            print(f"Name: {dish['name']}")
            print(f"Description: {dish['description']}")
            print(f"Price: {dish['price']}")
            print(f"Category: {dish['category']}")
            print()
