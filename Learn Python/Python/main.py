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
    def __init__(self, name, quantity, price, nameproduct):
        self.name = str(name)
        self.quantity = int(quantity)
        self.price = float(price)
        self.nameproduct = str(nameproduct)

def totalBill(quantity, price):
    total = quantity * price
    return total

num_people = int(input("Nhập số người mua: "))
people = []

for i in range(num_people):
    name = input(f"Enter the buyer's name {i+1}: ")
    quantity = int(input(f"Enter product quantity {i+1}: "))
    price = float(input(f"Enter price of product {i+1}: "))
    nameproduct = input("Enter product name: ")

    person_bill = Bill(name, quantity, price, nameproduct)
    people.append(person_bill)

    if person_bill.quantity < 10 and person_bill.price < 10.000:
        print("This person buys a small amount. Quantity:", person_bill.quantity, "Total bill:", person_bill.price, "Buyer's name:", person_bill.name)
    else:
        print("This person buys a large amount. Quantity:", person_bill.quantity, "Total bill:", person_bill.price, "Buyer's name:", person_bill.name)

for i, person_bill in enumerate(people):
    total = totalBill(person_bill.quantity, person_bill.price)
    print(f"Buyer {i+1} - Name: {person_bill.name}, Product Quantity: {person_bill.quantity}, Total bill: {total}, Product Name: {person_bill.nameproduct}")



