from UpdateDish import read_price


def add_dish(menu):
    print("             ===========================")
    print("                   Dish Categories")
    print("             ===========================")
    print("             1. Appetizers")
    print("             2. Main Courses")
    print("             3. Desserts")
    print()

    category = input('Enter the category of dish to add: ')

    name = input('Enter the name of the Dessert: ')
    if check_duplicate(menu, name):
        print("The Dish Already Exist!")
        return

    description = input('Enter the description of the dish (Ingredients): ')
    dish_price = read_price()

    if dish_price is None:
        print("Returning to main!")
        return

    if category == '1' or category == 'Appetizers':
        menu["Appetizers"].append({"name": name, "description": description, "price": dish_price,
                                   "category": "Appetizers"})
        print("Appetizer added successfully")
    elif category == '2' or category == 'Main Courses':
        menu["Main Course"].append({"name": name, "description": description, "price": dish_price,
                                    "category": "Main Course"})
        print("Main course added successfully")
    elif category == '3' or category == 'Desserts':
        menu["Desserts"].append({"name": name, "description": description, "price": dish_price, "category": "Desserts"})
        print("Desserts added successfully")
    else:
        print("Invalid category")
        return add_dish(menu)


def check_duplicate(menu, dish_name):
    for dish_category in menu.keys():
        for dish in menu[dish_category]:
            if dish["name"] == dish_name:
                return True
    return False
