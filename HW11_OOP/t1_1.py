# 1. В класі Person визначте метод compare_age(), який повертатиме
# результат порівняння віку людини з Вашим віком.
# При заданих об’єктах p1, p2 і p3, які будуть ініціалізовані
# name та age, буде повертатися повідомлення наступного формату:
# {other_person} is {older than / younger than / the same age as} me.

class Person:
    my_age = 36

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def compare_age(self):
        if self.my_age < self.age:
            print(f"{self.name} is older than me")
        elif self.my_age > self.age:
            print(f"{self.name} is younger than me")
        else:
            print(f"{self.name} is the same age as me")


c = Person("John", 60)
c.compare_age()
