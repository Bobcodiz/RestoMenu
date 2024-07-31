# Task 1: Menu Initialisation
def initialize_menu():
    menu = {
        "Appetizers": [
            {
                "name": "Spinach and Artichoke Dip",
                "description": "Creamy spinach, artichokes, and Parmesan cheese",
                "price": 7.55,
                "category": "Appetizers"
            },
            {
                "name": "Caesar Salad",
                "description": "Crisp romaine lettuce, croutons, and Caesar dressing",
                "price": 8.34,
                "category": "Appetizers"

            },
            {
                "name": "Garlic Parmesan Wings",
                "description": "Crispy chicken wings, garlic butter, and Parmesan cheese",
                "price": 9.90,
                "category": "Appetizers"
            }
        ],
        "Main Course": [
            {
                "name": "Lemon Herb Chicken",
                "description": "Grilled chicken breast with lemon, rosemary, and thyme",
                "price": 14.65,
                "category": "Main Course"
            },
            {
                "name": "Shrimp Scampi",
                "description": "Sautéed shrimp, garlic, and white wine sauce",
                "price": 18.45,
                "category": "Main Course"
            },
            {
                "name": "BBQ Ribs",
                "description": "Slow-cooked ribs, BBQ sauce, and coleslaw",
                "price": 22.15,
                "category": "Main Course"
            }
        ],
        "Desserts": [
            {
                "name": "Chocolate Lava Cake",
                "description": "Rich chocolate cake, molten chocolate center, and vanilla ice cream",
                "price": 5.75,
                "category": "Desserts"
            },
            {
                "name": "Blueberry Cheesecake",
                "description": "Creamy cheesecake, blueberry compote, and graham cracker crust",
                "price": 7.89,
                "category": "Desserts"
            },
            {
                "name": "Tiramisu",
                "description": "Coffee-flavored dessert, mascarpone cheese, and cocoa powder",
                "price": 8.90,
                "category": "Desserts"
            }
        ]
    }
    return menu


# Task 2: Add a dish
# Task 3: Update a dish price
# Task 4: Display Menu
# Task 5: Search for a dish

# Main Program
def main():
    menu = initialize_menu()
    while True:
        print("1.Add a dish")
        print("2.Update a dish price")
        print("3.Display Menu")
        print("4.Search for a dish")
        print("5.Exit")



