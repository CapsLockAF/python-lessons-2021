# Визначте атрибути fullname та email в класі Employee.
# При заданих first та last names:
# - В конструкторі сформуйте fullname звичайним з’єднанням через пробіл
# first та last name.
# В конструкторі сформуйте email з’єднанням first та last name через ‘.’
# між ними та приєднуючи  ‘@company.com’ наприкінці.

class Employee:
    def __init__(self, firstname, lastname):
        self.fullname = f"{firstname} {lastname}"
        self.email = f"{firstname}.{lastname}@company.com"


e = Employee("John", "Doe")

print(e.fullname)
print(e.email)
