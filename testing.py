
# list = "orange,apple,chair,pear"

# occurence = list.find("chair")
# # print(occurence)

# if occurence == 0:
#     list = list[:len("chair")+1]
#     print(list)
# else:
#     list = list[:occurence-1] + list[occurence + len("chair"):]
# # print(list)

# done = False
# pointer = 0
# counter = 1

# while (not done):
#     comma_index = list.find(",", pointer)

#     if (comma_index == -1):
#         done = True
#         comma_index = len(list)

#     print("Item {:1}: \t {}".format(counter, list[pointer:comma_index]))
#     pointer = comma_index + 1
#     counter += 1


# # (Lining Up The Decimal Point)
# numbers = [4.8, 49.723, 456.781, -72.18, 5, 13]
# for number in numbers:
#     print(f'{number:6.2f}')



# my_str = "orange,apple"
# start_point = 0
# done = False
# print("-"*80)
# print("\x1B[4m" + "Your cart contents:" + "\x1B[0m") # UNDERLINE
# while True:
#     comma_index = my_str.find(",", start_point)
    
#     if comma_index == -1:
#         print(my_str[start_point:len(my_str)])
#         break
#     print(my_str[start_point:comma_index])
#     # print()
#     start_point = comma_index + 1
# print("-"*80)

# print(my_str.split("."))

# ITEM_LIST = ["Whiskas Cat Food (7kg)", "Aquarian Goldfish Flake Food (50g)",
#             "Nature's Touch Wild Hay (1kg)", "Mixed Corn for Chickens (20kg)", 
#             "Harrington's Dry Adult Dog Food (15kg)"]
# ITEM_PRICES = [17.50, 5.95, 7.49, 23.49, 34.99]


# cart_items = []
# cart_prices = []
# cart_total = 0
# item_quantity = [1, 2, 3]

# for i in range(len(cart_items)):
#             print(f"£ {cart_prices[i]:6.2f} \t {cart_items[i]:45} \t Quantity: ")
#         for item in ITEM_LIST:
#             if item in cart_items:
#                 quantity_index = ITEM_LIST.index(item)
#                 print(item_quantity[quantity_index])  # Printing corresponding item quantities instead of in a serial


item_list = [1, 2, 3]
thing_list = ["a", "b", "c"]

print(list(zip(item_list, thing_list)))
# for (item, thing) in zip(item_list, thing_list):
#     print(item, thing)


