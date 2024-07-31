import UpdateDish


def add_dish(menu):
    print("             ===========================")
    print("                   Dish Categories")
    print("             ===========================")
    print("             1. Appetizers")
    print("             2. Main Courses")
    print("             3. Desserts")
    print()

    category = input('Enter the category of dish to add: ')

    if category == '1' or category == 'Appetizers':
        try:
            name = input('Enter the name of the Appetizer: ')
            description = input('Enter the description of the dish (Ingredients): ')
            p = UpdateDish.read_price()
            menu["Appetizers"].append({"name": name, "description": description, "price": p, "category": "Appetizers"})
            print("Appetizer added successfully")

        except Exception as e:
            print("could not add the item to the menu")
            print(e)
            return

    elif category == '2' or category == 'Main Courses':
        try:
            name = input('Enter the name of the Main Course Dish: ')
            description = input('Enter the description of the dish  (Ingredients): ')
            p = UpdateDish.read_price()
            menu["Main Course"].append(
                {"name": name, "description": description, "price": p, "category": "Main Course"})
            print("Main course added successfully")
        except Exception as e:
            print("could not add the item to the menu")
            print(e)
            return
    elif category == '3' or category == 'Desserts':
        try:
            name = input('Enter the name of the Dessert: ')
            description = input('Enter the description of the dish (Ingredients): ')
            p = UpdateDish.read_price()
            menu["Desserts"].append({"name": name, "description": description, "price": p, "category": "Desserts"})
            print("Dessert added successfully")
        except Exception as e:
            print("could not add the dessert")
            print(e)
            return
    else:
        print("Invalid category")
        return add_dish(menu)
