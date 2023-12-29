from abc import ABC, abstractmethod


# class Person(ABC):
#     def __init__(self, name, age):
#         self._name = str(name)
#         self._age = age

#     @classmethod
#     def increment_count(cls):
#         pass

#     @abstractmethod
#     def get_salary(self):
#         pass

#     @classmethod
#     def cls_information(cls):
#         pass

#     def __str__(self):
#         return f"My name is {self._name}, Age {self._age}"


# class Employee(Person):
#     emp_count = 0

#     def __init__(self, name, age, salary):
#         super().__init__(name, age)
#         self.__salary = salary
#         Employee.increment_count()

#     @classmethod
#     def increment_count(cls):
#         cls.emp_count += 1

#     def get_salary(self):
#         return self.__salary

#     @classmethod
#     def cls_information(cls):
#         print(
#             f"\nClass information: \n- Class name: {cls.__name__}\n Base Classes: {cls.__bases__}\n- Number of Employee: {cls.emp_count}\n"
#         )

#     def __str__(self):
#         return f"{super().__str__()}\n- My salary is ${self.__salary}\n"


# class Manager(Person):
#     man_count = 0

#     def __init__(self, name, age, salary, bonus):
#         super().__init__(name, age)
#         self.__salary = salary
#         self.__bonus = bonus
#         Manager.increment_count()

#     @classmethod
#     def increment_count(cls):
#         cls.man_count += 1

#     def get_salary(self):
#         total = self.__salary + self.__bonus
#         return total

#     @classmethod
#     def cls_information(cls):
#         print(
#             f"\nClass information: \n- Class name: {cls.__name__}\n Base Classes: {cls.__bases__}\n- Number of Manager: {cls.man_count}\n"
#         )

#     def __str__(self):
#         return f"{super().__str__()}\n- My salary is ${self.__salary}\n- Bonus is ${self.__bonus}\n- My total salary is ${self.get_salary()}"


# manager1 = Manager("Chinh", 18, 200000, 2000)
# manager2 = Manager("Truong", 18, 200000,1000)
# print(manager1)
# print(manager2)
# Manager.cls_information()


# Employee1 = Employee("Goku",18,200000)
# Employee2 = Employee("Vegeta",19,200000)

# print(Employee1)
# print(Employee2)

# Employee.cls_information()


class BankAccount:
    account_count = 0

    def __init__(self, name, id, balance):
        self._id = id
        self._name = name
        self._balance = balance
        BankAccount.increment_count()

    @property
    def id(self):
        return self._id

    @classmethod
    def increment_count(cls):
        cls.account_count += 1

    @property
    def name(self):
        return self._name

    @name.setter
    # get name
    def name(self, value):
        self._name = value

    @property
    def balance(self):
        return self._balance
    @balance.setter
    def balance(self, value):
        self._balance = value
    #  deposit
    
    def deposit(self, amount):
        if amount > 0:
            self._balance += amount
            return f"Deposit  New balance: {self._balance}"
    # withdraw
    def withdraw(self, amount):
        if 0 < amount <= self._balance:
            self._balance -= amount
            return f"Withdrawal. New balance: {self._balance}"
    
    # show infomartion account id name balance
    def __str__(self):
        return f"Account ID: {self._id}\nAccount Name: {self._name}\nBalance: {self._balance}"

    @classmethod
    # count quantity create 
    def cls_information(cls):
        print("Number of accounts: " + str(cls.account_count))



account1 = BankAccount("John Doe", 1,20000)
print(account1)
# nap
deposit_result = account1.deposit(2000)
print(deposit_result)
# rut
withdrawal_result = account1.withdraw(1000)
print(withdrawal_result)
# show
print(account1)




BankAccount.cls_information()
