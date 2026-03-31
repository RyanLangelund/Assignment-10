"""
-----------------------------------------------------------------------
ASSIGNMENT 10A: THE RESILIENT PIZZA ENGINE
-----------------------------------------------------------------------
[ ] 1. Header Docstring included.
[ ] 2. Global constant TOPPINGS defined as a Tuple in ALL_CAPS.
[ ] 3. Function 'make_pizza' defines 4 specific parameters.
[ ] 4. 'make_pizza' uses a DEFAULT value for is_delivery.
[ ] 5. main() displays the Global Pantry list to the user.
[ ] 6. main() calls the function using KEYWORD ARGUMENTS.
-----------------------------------------------------------------------
"""

TOPPINGS = ("Pepperoni", "Sausage", "Mushrooms", "Onions")


def make_pizza(customer, size, topping, is_delivery=False):

    print("\n--- PIZZA ORDER ---")
    print(f"Customer: {customer}")
    print(f"Size: {size}")
    print(f"Topping: {topping}")

    if is_delivery:
        print("Order Type: Delivery")
    else:
        print("Order Type: Pickup")


def main():
    name = input("Enter your name: ").title()

    print(f"Topping Options: {TOPPINGS}")
    topping_choice = input("Choose a topping: ")

    size = input("Enter pizza size (Small/Medium/Large): ")

    delivery_input = input("Delivery? (yes/no): ").lower()

    try:
        if delivery_input == "yes":
            delivery = True
        else:
            delivery = False
    except:
        delivery = False
    make_pizza(customer=name, size=size, topping=topping_choice, is_delivery=delivery)


main()
