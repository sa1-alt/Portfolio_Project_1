# Function to display cart contents and prices
def cart_display():
    print(f"{LINE}\nShopping Cart:\n")
    if not cart_items:
        print("Your cart is empty")
    else:
        for (item, price) in zip(cart_items, cart_prices):
            quantity_index = ITEM_LIST.index(item)

            print(f"£ {price:6.2f} \t {item:40} \t Quantity: "
                  f"{item_quantity[quantity_index]}")          
    print(LINE)

# Function to display numbered item list
def item_menu():
    for num, name in enumerate(ITEM_LIST, start=1):
       print(f"{num}:  {name}")

# Function to add item
def add_item():
    cart_items.append(ITEM_LIST[item_selection])
    cart_prices.append(ITEM_PRICES[item_selection])
    item_quantity[item_selection] += 1

# function to remove item
def remove_item():
    cart_items.remove(ITEM_LIST[item_remove])
    cart_prices.remove(ITEM_PRICES[item_remove])
    item_quantity[item_remove] -= 1

# Function to make item selection check dynamic if I decide to add more items
# to the ITEM_LIST
def valid_selections():
    valid_selections_list = []
    for i in range(len(ITEM_LIST) + 1):
        if i == 0:
            continue
        else:
            valid_selections_list.append(str(i))
    return valid_selections_list

MAIN_MENU = """
Main Menu
1. Add an item to your cart
2. Remove an item from your cart
3. View the total cost of your cart
4. Checkout

Enter your selection here (1-4): """

ITEM_LIST = ["Whiskas Cat Food (7kg)", "Aquarian Goldfish Flake Food (50g)",
            "Nature's Touch Wild Hay (1kg)", "Mixed Corn for Chickens (20kg)", 
            "Harrington's Dry Adult Dog Food (15kg)"]
ITEM_PRICES = [17.50, 5.95, 7.49, 23.49, 34.99]

menu_selection = ""
item_selection = ""
cart_items = []
cart_prices = []
cart_total = 0
item_quantity = [0, 0, 0, 0, 0]

LINE = "-"*79

# Greeting
print()
print("Welcome to Paws n Cart!")

while menu_selection != "4":
    cart_display()
    menu_selection = input(MAIN_MENU)
    
    while menu_selection not in ["1", "2", "3", "4"]:
        print("*Invalid input* Try again")
        menu_selection = input(MAIN_MENU)
        
    # Adding an item
    if menu_selection == "1":
        print()
        item_menu()
        item_selection = input(f"\nWhich item would you like to add. "\
                               f"Enter 1-5 or 0 to return to the Main Menu:\n")

        if item_selection == "0":  # Return to main menu
                    continue

        while item_selection not in valid_selections():
            print("*Please enter a valid input*")
            item_selection = input(f"\nWhich item would you like to add. "\
                                   f"Enter 1-5 or 0 to return to the Main Menu:\n")

        item_selection = int(item_selection) - 1  # Correct indexing
       
        if ITEM_LIST[item_selection] in cart_items:
            item_quantity[item_selection] += 1
            cart_total += ITEM_PRICES[item_selection]
        else:
            add_item()
            cart_total += ITEM_PRICES[item_selection]

    # Removing an item
    elif menu_selection == "2":
        print()
        item_menu()

        item_remove = input(f"\nWhich item would you like to remove. "\
                            f"Enter 1-5 or 0 to return to the Main Menu:\n")

        if item_remove == "0":  # Return to main menu
                continue

        while (item_remove not in valid_selections()
               and ITEM_LIST[int(item_remove)-1] not in cart_items):
            print("Please enter a valid input")
            item_remove = input(f"\nWhich item would you like to remove. "\
                                f"Enter 1-5 or 0 to return to the Main Menu:\n")

        item_remove = int(item_remove) - 1  # Correct indexing

        if item_quantity[item_remove] > 1:
            item_quantity[item_remove] -= 1
            cart_total -= ITEM_PRICES[item_remove]
        else:
            remove_item()
            cart_total -= ITEM_PRICES[item_remove]
       
    # Displaying total cost of cart items
    elif menu_selection == "3":
        print("\nYour cart total: £ {:.2f}".format(cart_total))
        print()
        checkout_option = input("Enter 1 to checkout or 2 return to the "\
                                "main menu: ")
        
        while checkout_option not in ["1", "2"]:
             print("Please enter a valid input")
             checkout_option = input("Enter 1 to checkout or 2 return to the "\
                                     "main menu: ")
        if checkout_option == "1":
            print("Thanks for visiting Paws n Cart!")
            break
        else:
            continue
else:
    print("Thanks for visiting Paws n Cart!")

        


                

    


 