# # # # value = 2_000_000
# # # # formatted_value = f"{value:,}".replace(",", ".")
# # # # print(formatted_value)


# # # # Import pandas package
# # import math
# # import random

# # # #1
# # # width = int(input('Enter width: '))
# # # #input height
# # # height = int(input('Enter height: '))

# # # Perimeter = (width + height) / 2

# # # Area  = (width * height)

# # # print(f"""Perimeter, {Perimeter}
# # #     'Area', {Area} """)


# # # # #2

# # centimeters = float(input("Enter length in centimeters: "))

# # centimeters_to_decimeters = 0.1  
# # centimeters_to_inches = 0.393701  


# # decimeters = centimeters * centimeters_to_decimeters
# # inches = centimeters * centimeters_to_inches

# # print(f"{centimeters} centimeters is equal to {decimeters:.2f} decimeters")
# # print(f"{centimeters} centimeters is equal to {inches:.2f} inches")



# # # #4


# # # #8
# # # Input string
# # # input_string = "Today is Sunday and we don't need to wake up at 6 am"

# # # #ddung split de tach tung chu ra thanh mot list 
# # # words = input_string.split()
# # # #in ra do dai cua cai chuoi
# # # word_count = len(words)

# # # number_position = None

# # # for i, word in enumerate(words):
# # #     #check xem co phai so kkhong
# # #     if word.isdigit():
# # #         number_position = i + 1  

# # # print("Number of words in the string:", word_count)

# # # if number_position is not None:
# # #     print("Number is present in the string at position:", number_position)
# # # else:
# # #     print("No number found in the string.")

# # # 5

# # random_number = random.randint(10, 150)

# # normalized_number = (random_number - 10) / (150 - 10)

# # print(f"Random Integer: {random_number}")
# # print(f"Normalized Number: {normalized_number:.2f}")

# # #7
# # import math
# # # thu vien toan hoc
# # # method detal
# # def calculate_delta(number1, number2, number3):
# #     return number2 ** 2 - 4 * number1 * number3
# # # input number1, number2, number3
# # number1 = float(input("Enter number 1: "))
# # number2 = float(input("Enter number 2: "))
# # number3 = float(input("Enter number 3: "))
# # #conglution delta
# # delta = calculate_delta(number1, number2, number3)

# # if delta > 0:
# #     print("Equation has two solutions")
# #     x1 = (-number2 + math.sqrt(delta)) / (2 * number1)
# #     x2 = (-number2 - math.sqrt(delta)) / (2 * number1)
# #     print("x1 =", x1)
# #     print("x2 =", x2)
# # elif delta == 0:
# #     print("Equation has a single solution")
# #     x1 = - number2 / (2 * number1)
# #     print("x1 = x2", x1)
# # else:
# #     print("Equation has no real solution")

# # #11

# # from datetime import datetime

# # birthday_input = input("Enter your birthday (DD-MM-YYYY): ")

# # try:
# #     birthday_date = datetime.strptime(birthday_input, "%d-%m-%Y")

# #     weekday_name = birthday_date.strftime("%A")
# #     month_name = birthday_date.strftime("%B")

# #     today = datetime.now()
# #     age = today.year - birthday_date.year - ((today.month, today.day) < (birthday_date.month, birthday_date.day))

# #     print(f"Weekday Name: {weekday_name}")
# #     print(f"Month Name: {month_name}")
# #     print(f"Your current age: {age} years")

# # except ValueError:
# #     print("Invalid date format. Please use DD-MM-YYYY format.")





# # class Students:
# #     def __init__(self, subject, mark, name, birthday):
# #         self.subject = str(subject)
# #         self.mark = int(mark)
# #         self.name = str(name)
# #         self.birthday = str(birthday)


# # def totalMark(students):
# #     total = sum(student.mark for student in students)
# #     average = total / len(students)
# #     return average

# # students =[]
# # try:
# #     quantity = int(input("Enter a quantity of students :"))
# # except ValueError:
# #     print("please enter a quantity of students is a Number")
        
# # for i in range(quantity):
# #     subject = str(input(f"Subject {i+1}:"))
# #     mark = float(input(f"Mark {i+1}:"))
# #     name = str(input(f"Name {i+1}:"))
# #     birthday = str(input(f"Birthday {i+1}:"))
    
# #     list_students = Students(subject, mark, name, birthday)
# #     students.append(list_students)


# # for i, list_students in enumerate(students):
# #     print(f"""Student {i+1} :
# #              - Subject: {list_students.subject.title()}
# #              - Mark : {list_students.mark}
# #              - Name : {list_students.name.capitalize()}
# #              - Birth day: {list_students.birthday}""")
    
# # average_mark = totalMark(students)
# # print(f"Total Average Mark: {average_mark}")



# # inputString = str(input('Enter a String :'))

# # location = inputString.split()

# # len_inputString = len(location)

# # print(len_inputString)

# # number_position = None

# # for i, word in enumerate(location):
# #     if word.isdigit():
# #         number_position = i + 1
    

# # if number_position is not None:
# #     print("Number is present in the string at position:", number_position)
# # else:
# #     print("No number found in the string.")





# # import math

# # def euclidean_distance(x1, y1, x2, y2):
# #     return math.sqrt((x1 - x2)**2 + (y1 - y2)**2)

# # def manhattan_distance(x1, y1, x2, y2):
# #     return abs(x1 - x2) + abs(y1 - y2)

# # # Function to calculate Cosine distance
# # def cosine_distance(x1, y1, x2, y2):
# #     dot_product = x1 * x2 + y1 * y2
# #     magnitude1 = math.sqrt(x1**2 + y1**2)
# #     magnitude2 = math.sqrt(x2**2 + y2**2)
# #     return 1 - (dot_product / (magnitude1 * magnitude2))

# # # Get input for the first point
# # x1 = float(input("Enter the x-coordinate of the first point: "))
# # y1 = float(input("Enter the y-coordinate of the first point: "))

# # # Get input for the second point
# # x2 = float(input("Enter the x-coordinate of the second point: "))
# # y2 = float(input("Enter the y-coordinate of the second point: "))

# # euclidean = euclidean_distance(x1, y1, x2, y2)
# # manhattan = manhattan_distance(x1, y1, x2, y2)
# # cosine = cosine_distance(x1, y1, x2, y2)

# # print(f"Euclidean Distance: {euclidean}")
# # print(f"Manhattan Distance: {manhattan}")
# # print(f"Cosine Distance: {cosine}")

# class Customer:
#     def __init__(self,name,product,quantity):
#         self.name = str(name)
#         self.product = str(product)
#         self.quantity = int(quantity)


# def display_menu():
#     print("1. Add a customer")
#     print("2. find john")
#     print("3. Show customer buy >2")
#     print("4. clear customer")
#     print("5. Exit")

# customers = []
# while True:
#     display_menu()

#     choice = input("Enter your choice: ")

#     if choice == "1":
#       try:
#           CustomerNumber = int(input("Enter a quantity of customer :"))
#       except ValueError:
#           print("please enter a quantity of students is a Number")
          
#       for i in range(CustomerNumber):
#           name = str(input(f"Name {i+1}:"))
#           product = str(input(f"Product {i+1}:"))
#           quantity = float(input(f"Quantity {i+1}:"))
          
#           list_customer = Customer(name,product,quantity)
#           customers.append(list_customer)
          
#       for i, list_customer in enumerate(customers):
#           print(f"""Customer {i+1}:
#                         - Subject: {list_customer.name.title()}
#                         - Mark: {list_customer.product.title()}
#                         - Name: {list_customer.quantity}""")
#     if choice == "2":
# #print customer name jhon
#       for i, nameCustomer in enumerate(customers):
#           if nameCustomer.name.lower() == "john":
#               print(f"Customer {i+1}")
#               print(f" - Name: {nameCustomer.name.title()}")
#               print(f" - Product: {nameCustomer.product.title()}")
#               print(f" - Quantity: {nameCustomer.quantity} kg")
#           else:
#             print(f"Not customer'{nameCustomer.name.title()}' in CustomerList")
            
#     if choice == "3":
# # show customer buy pork
#         for i, customer in enumerate(customers):
#             if customer.product.lower() == "pork" and customer.quantity > 2:
#                 print(f"Customer {i+1} bought Pork over 2kg:")
#                 print(f" - Name: {customer.name.title()}")
#                 print(f" - Product: {customer.product.title()}")
#                 print(f" - Quantity: {customer.quantity} kg")
#             else:
#                 print("Not one customer buy on 2kg ")
        
#     elif choice == "4":
#         customers.clear()
#         print(customers)
        
# # exit program
#     elif choice == "5":
#         print("Goodbye!"
#         break
    
#     else:
#         print("Invalid choice. Please select a valid option.")






# for i,customer in enumerate(CustomerList):
#     if customer.lower() == "john":
#         print(f"co then {customer} at index {i}")



# for i,product in enumerate(ProductList):
#     if product.lower() == "peer" and product.lower() == "pork":
#         print(f"co then {product} at index {i}")



    





#tao mot cai mang de luu tru cac phan tu.
numbers = []
#bat dau.
i = int(input("Enter a number start: "))
#ket thuc.
n = int(input("Enter a number end: "))
# chay for de them cac phan tu vao numbers = phuong thuc append.
for i in range(n+1):
  numbers.append(i)

# tim mot so trong numbers va kiem tra xem co no trong numbers khong.
search_Number = int(input(f"Enter the number you want in from {i} to from {n}: "))
list_index = []
#tao mot cai mang de luu so chan tu vong lap for
for digit in str(search_Number):
    #chay vong lap de them phan tu vao list_index
    list_index.append(int(digit))
    #chay vong lap for de them phan tu vao elemntEven
    evenElement =[]
for k in list_index:
    if k % 2 == 0:
        evenElement.append(k)

sortNumber = list(sorted(evenElement))
print(f"Number {search_Number} Has even digits {sortNumber}")


        
