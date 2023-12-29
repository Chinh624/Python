
from abc import ABCs, abstractclassmethod, abstractmethod
class Person:
    count = 0
    def __init__(self, name, age):
        self._name = name
        self._age = age
        Person.increment_count()

    @classmethod
    def increment_count(cls):
        cls.count += 1

    @staticmethod
    # def cls_information():
    #     print("\nClass information: \n- Class name: " + str(Person.__name__) + '\n Base Classes: ' + str(
    #         Person.__bases__) + '\n- Number of Person: ' + str(Person.count) + '\n')
    
    def __str__(self):
        return '- My name is ' + self._name + "\n- I am " + str(self._age) + " years old"
    
    def cls_information():
        print("\nClass information: \n- Class name: " + str(Person.__name__) + '\n Base Classes: ' + str(
            Person.__bases__) + '\n- Number of Employee: ' + str(Person.count) + '\n')
        
        
print("Person")
person1 = Person("Truong", 24)
person2 = Person("Chinh", 20)

print(person1)
print(person2)


class Employee(Person):
    count = 0

    def __init__(self, name, age, salary, bonus):
        super().__init__(name, age)
        self.__salary = salary
        self.__bonus = bonus
        Employee.increment_count()

    @classmethod
    def increment_count(cls):
        cls.count += 1

    @staticmethod
    def cls_information():
        print("\nClass information: \n- Class name: " + str(Employee.__name__) + '\n Base Classes: ' + str(
            Employee.__bases__) + '\n- Number of Employee: ' + str(Employee.count) + '\n')


    def __str__(self):
        return super().__str__() + "\n- My salary is $" + str(self.__salary) + " Bonus " + str(
            self.__bonus) + "\n"
print("\nEmployee: ")
employee1 = Employee("John", 30, 50000, 20)
employee2 = Employee("Jane", 25, 60000, 10)
employee3 = Employee("Bob", 35, 75000, 20)

print(employee1)
print(employee2)
print(employee3)


class Manager(Person):
    count = 0

    def __init__(self, name, age, salary, bonus):
        super().__init__(name, age)
        self.__salary = salary
        self.__bonus = bonus
        Manager.increment_count()

    @classmethod
    def increment_count(cls):
        cls.count += 1

    @staticmethod
    def cls_information():
        print("\nClass information: \n- Class name: " + str(Manager.__name__) + '\n Base Classes: ' + str(
           Manager.__bases__) + '\n- Number of Manager: ' + str(Manager.count) + '\n')

    def totalSalary(self):
        total = self.__salary + self.__bonus
        return int(total)

    def __str__(self):
        return super().__str__() + "\n- My salary is $" + str(self.__salary) + " Bonus " + str(
            self.__bonus) + "\n- Total salary: $" + str(self.totalSalary()) + "\n"

print("\nManager")
manager1 = Manager("John", 30, 50000, 20)
manager2 = Manager("Jane", 25, 60000, 10)
manager3 = Manager("Bob", 35, 75000, 20)

print(manager1)
print(manager2)
print(manager3)

Manager.cls_information()
Employee.cls_information()
Person.cls_information()



