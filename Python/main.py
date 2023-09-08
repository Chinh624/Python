# import math
# # thu vien toan hoc
# # method detal
# def calculate_delta(number1, number2, number3):
#     return number2 ** 2 - 4 * number1 * number3
# # input number1, number2, number3
# number1 = float(input("Enter number 1: "))
# number2 = float(input("Enter number 2: "))
# number3 = float(input("Enter number 3: "))
# #conglution delta
# delta = calculate_delta(number1, number2, number3)

# if delta > 0:
#     print("Equation has two solutions")
#     x1 = (-number2 + math.sqrt(delta)) / (2 * number1)
#     x2 = (-number2 - math.sqrt(delta)) / (2 * number1)
#     print("x1 =", x1)
#     print("x2 =", x2)
# elif delta == 0:
#     print("Equation has a single solution")
#     x1 = - number2 / (2 * number1)
#     print("x1 = x2", x1)
# else:
#     print("Equation has no real solution")


# class Person:
#   def __init__(self, name, age):
#     self.name = name
#     self.age = age

#   def __str__(self):
#     return f"{self.name}({self.age})"

# p1 = Person(n, y)

# print(p1)

# while True:
#     try:
#         n = int(input("Enter n number for while: "))
#         break
#     except ValueError:
#         print("Invalid input. Please enter an integer.")

# def totalArray(ar):
#     total = 0
#     for elementarray in ar:
#         total += elementarray
#     return total

# arrayOdd = []
# arrayEven =[]
# i = 1
# while i in range(n):
#     if i % 2 != 0:
#         arrayOdd.append(i)
#     else:
#         arrayEven.append(i)
#     i += 1

# sum_odd = sum(arrayOdd)
# sum_even = sum(arrayEven)

# print(arrayOdd)
# print(arrayEven)
# print("Total array odd :", sum_odd)
# print("Total array odd :", sum_even)


class Bill:
    def __init__(self, name, quantity, price, nameProduct):
        self.name = str(name)
        self.quantity = int(quantity)
        self.price = float(price)
        self.nameProduct = str(nameProduct)

def totalBill(quantity, price):
    total = quantity * price
    return float(total)

people = []

product = ["Coca", "Pepsi", "C2", "numberOne", "revive"]
total_day_bill = 0

def display_menu():
    print("1. Add a buyer")
    print("2. View buyer details")
    print("3. Show Total bill of today")
    print("4. Clear buyer name")
    print("5.Exit")
while True:
    display_menu()

    choice = input("Enter your choice: ")

    if choice == "1":
        try:
            num_people = int(input("Enter buyer number: "))
        except ValueError:
            print("Invalid input. Please enter an integer.")

        for i in range(num_people):
            name = str(input(f"Enter the buyer's name {i+1}: "))
            quantity = int(input(f"Enter product quantity {i+1}: "))
            price = float(input(f"Enter price of product {i+1}: "))
            nameProduct = str(input(f"Enter product name: {i+1}: "))
            
            person_bill = Bill(name, quantity, price, nameProduct)
            people.append(person_bill)
            
            if person_bill.quantity < 10 and person_bill.price < 10000:
                print("This person buys a small amount. Quantity:", person_bill.quantity, "Price", person_bill.price, "Buyer's name:", person_bill.name.capitalize())
            else:
                print("This person buys a big amount. Quantity:", person_bill.quantity, "Price:", person_bill.price, "Buyer's name:", person_bill.name.capitalize())

            if person_bill.nameProduct in product:
                print("We have bought this product:", person_bill.nameProduct)
            else:
                print(f"We don't have the product: {person_bill.nameProduct} in stock")
                
    elif choice == "2":
        for i, person_bill in enumerate(people):
            print(f"Buyer {i+1} - Name: {person_bill.name.capitalize()}, Product Quantity: {person_bill.quantity}, Total bill: {totalBill(person_bill.quantity, person_bill.price)}, Product Name: {person_bill.nameProduct}")

    elif choice == "3":
        total_day_bill = sum(totalBill(person.quantity, person.price) 
    for person in people)
        print(f"Total bill for the day: {total_day_bill}")
        
    elif choice == "4":
        people.clear()
        print(people)
        
    elif choice == "5":
        print("Goodbye!")
        break

    else:
        print("Invalid choice. Please select a valid option.")
