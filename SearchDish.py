def search_dish(menu):
    dish_name = input("Enter the dish name\nDish : ")

    for category, dishes in menu.items():
        for dish in dishes:
            if dish["name"] == dish_name:
                return dish
    return None


def print_dish(menu):

    dish = search_dish(menu)

    if dish is None:
        print(f"The dish was not found!!")
    else:
        print(f"Name : {dish['name']}")
        print(f"Description : {dish['description']}")
        print(f"Price : ${dish['price']}")
        print(f"Category : {dish['category']}")
