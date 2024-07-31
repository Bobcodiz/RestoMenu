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

    if category == '1':
        try:
            name = input('Enter the name of the Appetizer: ')
            description = input('Enter the description of the dish (Ingredients): ')
            p = UpdateDish.read_price()

            menu_to_update = menu.get("Appetizers")
            updated = {"name": name, "description": description, "price": p,"category": category}
            menu_to_update.append(updated)
            print("Appetizer added successfully")
            return menu_to_update
        except Exception as e:
            print("could not add the item to the menu")
            print(e)
            return

    elif category == '2':
        try:
            name = input('Enter the name of the Main Course Dish: ')
            description = input('Enter the description of the dish  (Ingredients): ')
            p = UpdateDish.read_price()

            menu_to_update = menu.get("Main Course")
            updated = {"name": name, "description": description, "price": p, "category": category}
            menu_to_update.append(updated)
            print("Main course added successfully")
            return menu_to_update
        except Exception as e:
            print("could not add the item to the menu")
            print(e)
            return

    elif category == '3':
        try:
            name = input('Enter the name of the Dessert: ')
            description = input('Enter the description of the dish (Ingredients): ')
            p = UpdateDish.read_price()

            menu_to_update = menu.get("Desserts")
            updated = {"name": name, "description": description, "price": p, "category": category}
            menu_to_update.append(updated)
            print("Dessert added successfully")
            return menu_to_update
        except Exception as e:
            print("could not add the dessert")
            print(e)
            return
