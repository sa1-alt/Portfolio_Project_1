"""
Shopping cart program for pet-related items. 
Users are able to view their cart, add/remove items to it and view the total
cost of their cart.

Created using string manipulation only -- no lists.

"""

shopping_cart = ""
LINE = "-"*79
user_selection = ""
total_price = 0

# Greeting
print("Welcome to Paws n Cart!")

# Main Menu
while user_selection != "4":
    print("Please select one of the following options:\n"
          "1. Add an item to your cart\n"
          "2. Remove an item from your cart\n"
        #   "3. Update item quantity"
          "3. View the total cost of your cart\n"
          "4. Checkout\n")
    
    print(LINE)
    print(f"Your shopping cart:{shopping_cart}")
    print(LINE)
    
    user_selection = input("Enter the number of the option you would like:\n")

    # Add item
    if user_selection == "1":
        item_name = input("Enter the name of the item you would like to "\
                          "purchase: ")
        item_price = input("Enter the price of this item: ")
        item_quantity = 1
        try:
            item_float = float(item_price)
            total_price += item_float
            print(total_price)
        except ValueError:
            print("Invalid input")
            item_price = input("Enter the price of this item: ")
        
        shopping_cart += f"\n{item_name} \t\t £ {item_float:.2f} \tQuantity: "\
                         f"{item_quantity}"

    # Remove Item
    elif user_selection == "2":
        remove_item = input("Which item would like to remove?\n")
        if remove_item in shopping_cart:
            remove_index_item = shopping_cart.find(remove_item)
            remove_index_price = shopping_cart.find("£", remove_index_item) # index + 6 to remove entire price
            # Price to minus from total
            price_to_remove = shopping_cart[(remove_index_price+2):(remove_index_price+6)]
            total_price -= float(price_to_remove)

            shopping_cart = shopping_cart[:remove_index_item - 1] + shopping_cart[remove_index_price + 6:]  # -1 to include newline character
            
        else: 
            print("Item not in cart. Enter the name again:\n")
            remove_item = input("Which item would like to remove?\n")


    # # Quantities (not worth it?)
    # if user_selection == "3":
    #     item_update = input("Which item's quantity would you like to change? ")
    #     quantity_update = input("Enter the quantity total you would like: ")
    #     item_update_index = shopping_cart.find(item_update)
    #     quantity_index = shopping_cart.find("Quantity", item_update_index)
    #     shopping_cart = shopping_cart[:item_update_index-1] + shopping_cart[quantity_index+12:]



    # Total cost
    elif user_selection == "3": 
        print(LINE) 
        print(f"The total value of your cart is: £ {total_price:.2f}")
        print(LINE)