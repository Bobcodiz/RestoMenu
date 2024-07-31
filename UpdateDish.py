from SearchDish import search_dish


def update_dish(menu):
    print("\t\tDish Update\n")

    dish = search_dish(menu)

    if dish is None:
        print("The Dish Was Not Found!")
        return

    dish_price = read_price()

    if dish_price is None:
        print("Returning To Menu.")
        return

    dish['price'] = dish_price
    print("\tPrice Updated Successfully")


def read_price():
    trials = 10
    while trials > 0:
        try:
            price = input("\tEnter The Dish Price : ")
            price = float(price.strip())
            return price
        except ValueError:
            trials = trials - 1
            print("The Price Entered Is Not A Valid Amount.")
            print(f"{trials} Trial(s) Remaining.")
    return None
