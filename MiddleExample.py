# # Get the input string from the user
# inputString = input("Enter a string: ")

# # Get the character whose appearance count you want to check
# inputChoice = input("Enter a character to check: ")

# # Count the appearances of the inputChoice in the inputString
# show = inputString.count(inputChoice)

# # Check if the count is greater than 3
# if show >= 2:
#     charactersAppear = [char for char in inputString 
#                         if char == inputChoice]
#     # Print all occurrences of the character
#     print("Characters that appear more than 3 times:", charactersAppear)
# else:
#     # Print a message if the character appears 3 times or fewer
#     print("Character appears 3 times or fewer.")


arrays = []

for i in range(1,10+1):
    arrays.append(i)

print(arrays)

def factorial(n):
    if (n == 0):
        return 1
    if (n <= 1):
        for j in range(1,n+1):
            output = 1
            output = output * i
        return output
    
  

print(factorial(len(arrays)))

# arrays = list(range(1, 10 + 1))

# def factorial(n):
#     if n == 0:
#         return 1
#     if n >= 1:
#         output = 1
#         for j in range(1, n + 1):
#             output = output * j
#         return output


# def calculate_total_partial_factorial(nn):
#     total_partial_factorial = 0
#     for i in str(nn):
#         total_partial_factorial += factorial(int(i))
#     return total_partial_factorial

# Define the 'arrays' list after the 'calculate_total_partial_factorial' function.



# # Calculate the total partial factorial after defining the 'arrays' list.

# total_partial_factorial = calculate_total_partial_factorial(arrays)
# print("Total partial factorial:", total_partial_factorial)



       
       
class Person:
    count = 0
    
    def __init__(self, name, age):
        self.__name = name
        self.__age = age
        self.welcome()  
        Person.increment_count()  

    def welcome(self, alert="Hello"):
        self.alert = alert

    @classmethod
    def increment_count(cls):
        cls.count += 1

    def introduce(self):
        return f"{self.alert}, my name is {self.__name} and I am {self.__age} years old."

person1 = Person("Tung", 21)
person2 = Person("Chinh", 20)
person3 = Person("Chinh", 20)

print(person1.introduce())
print(person2.introduce())
print(person3.introduce())
print(f"Number of Person objects created: {Person.count}")








