# 4. Display Menu
def display_menu(menu):
    for category in menu.keys():
        print(f"Category : {category}")
        for dish in menu[category]:
            print()
            print(f"Name: {dish['name']}")
            print(f"Description: {dish['description']}")
            print(f"Price: ${dish['price']}")
            print()
