# Випадкові числа в діапазоні від -5 до 5 розкласти на два списки:
#  в один помістити тільки додатні,
#  у другий - тільки від’ємні.
# Числа, рівні нулю, ігнорувати.
# Вивести на екран всі згенеровані випадкові числа і елементи обох списків.

from random import randint

lenList = int(input("Enter a length of list: "))

list1 = [randint(-5, 5) for i in range(abs(lenList))]
negatives = [i for i in list1 if i < 0]
positives = [i for i in list1 if i > 0]

print("The full list: ")
for i in list1:
    print("%s" % i, end=", ")
print("\nPositive values: ")
for i in positives:
    print("%s" % i, end=", ")
print("\nNegative values: ")
for i in negatives:
    print("%s" % i, end=", ")
