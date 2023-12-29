# # create menu when user input have fuctions:
# 1. add number buy
# 2. show person buy
# 3. show bill of today
# 4. Clear A person in person
# 5. clear all in person
# 6. exit program 

class Bill:
    def __init__(self, name, quantity, price, product_name):
        self.name = name
        self.quantity = quantity
        self.price = price
        self.product_name = product_name



    def total_bill(self):
        return self.quantity * self.price

def display_menu():
    print("1. Add a buyer")
    print("2. View buyer details")
    print("3. Show Total bill of today")
    print("4. Clear a person from the list")
    print("5. Clear buyer names")
    print("6. Exit")

def add_buyer(people):
    name = input("Enter the buyer's name: ")
    quantity = int(input("Enter product quantity: "))
    price = float(input("Enter price of product: "))
    product_name = input("Enter product name: ")

    person_bill = Bill(name, quantity, price, product_name)
    people.append(person_bill)

    print(f"{name.capitalize()} has been added as a buyer.")

def view_buyer_details(people):
    for i, person_bill in enumerate(people):
        print(f"Buyer {i + 1} - Name: {person_bill.name.capitalize()}")
        print(f"Product Quantity: {person_bill.quantity}")
        print(f"Total bill: {person_bill.price}")
        print(f"Product Name: {person_bill.product_name}")

def calculate_total_bill(people):
    total_day_bill = sum(person.total_bill() for person in people)
    print(f"Total bill for the day: {total_day_bill:.2f}")

def remove_buyer(people):
    name_to_delete = input("Enter the name of the buyer you want to delete: ")

    people = [person for person in people if person.name!= name_to_delete]
    print(f"{name_to_delete} has been deleted from the buyer list.")

def clear_buyer_names(people):
    people.clear()
    print("Buyer list cleared.")

people = []

while True:
    display_menu()
    choice = input("Enter your choice: ")
    if choice == "1":
        add_buyer(people)
    elif choice == "2":
        view_buyer_details(people)
    elif choice == "3":
        calculate_total_bill(people)
    elif choice == "4":
        remove_buyer(people)
    elif choice == "5":
        clear_buyer_names(people)
    elif choice == "6":
        print("Goodbye!")
        break
    else:
        print("Invalid choice. Please select a valid option.")


# class Bill:
#     def __init__(self, name, quantity, price, nameProduct):
#         self.name = str(name)
#         self.quantity = int(quantity)
#         self.price = float(price)
#         self.nameProduct = str(nameProduct)


# def totalBill(quantity, price):
#     total = quantity * price
#     return float(total)


# people = []

# product = ["Coca", "Pepsi", "C2", "numberOne", "revive"]

# total_day_bill = 0



# def display_menu():
#     print("1. Add a buyer")
#     print("2. View buyer details")
#     print("3. Show Total bill of today")
#     print("4. Clear A person in List total")
#     print("5. Clear buyer name")
#     print("6. Exit")


# while True:
#     display_menu()

#     choice = input("Enter your choice: ")

#     if choice == "1":
#         try:
#             num_people = int(input("Enter buyer number: "))
#         except ValueError:
#             print("Invalid input. Please enter an integer.")

#         for i in range(num_people):
#             name = str(input(f"Enter the buyer's name {i+1}: "))
#             quantity = int(input(f"Enter product quantity {i+1}: "))
#             price = float(input(f"Enter price of product {i+1}: "))
#             nameProduct = str(input(f"Enter product name {i+1}: "))

#             person_bill = Bill(name, quantity, price, nameProduct)
#             people.append(person_bill)

#             if person_bill.quantity < 10 and person_bill.price < 10000:
#                 print(
#                     "This person buys a small amount. Quantity:",
#                     person_bill.quantity,
#                     "Price",
#                     person_bill.price,
#                     "Buyer's name:",
#                     person_bill.name.capitalize(),
#                 )
#             else:
#                 print(
#                     "This person buys a big amount. Quantity:",
#                     person_bill.quantity,
#                     "Price:",
#                     person_bill.price,
#                     "Buyer's name:",
#                     person_bill.name.capitalize(),
#                 )

#             if person_bill.nameProduct in product:
#                 print("We have bought this product:", person_bill.nameProduct)
#             else:
#                 print(f"We don't have the product: {person_bill.nameProduct} in stock")

#     elif choice == "2":
#         for i, person_bill in enumerate(people):
#             print(
#                 f"""Buyer {i+1} - Name: {person_bill.name.capitalize()}
#                         Product Quantity: {person_bill.quantity}
#                         Total bill: {totalBill(person_bill.quantity, person_bill.price)}
#                         Product Name: {person_bill.nameProduct}"""
#             )

#     elif choice == "3":
#         total_day_bill = sum(totalBill(person.quantity, person.price) for person in people)
#         print(f"Total bill for the day: {total_day_bill}")

#     elif choice == "4":
#         name_to_delete = input("Enter the name of the buyer you want to delete: ")
#         people = [person for person in people if person.name != name_to_delete]
#         print(f"{name_to_delete} has been deleted from the buyer list.")

#     elif choice == "5":
#         people.clear()
#         print("Buyer list cleared.")

#     elif choice == "6":
#         print("Goodbye!")
#         break

#     else:
#         print("Invalid choice. Please select a valid option.")



