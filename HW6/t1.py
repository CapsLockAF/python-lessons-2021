# Заповнити один список випадковими числами,
# інший - введеними з клавіатури числами,
# в третій записати суми відповідних елементів перших двох.
# Вивести вміст списків на екран.

from random import randint
countList1 = int(input("Enter a number of random integers of List 1: "))
valueList2 = input("Enter a queue of values of List 2 "
                   "separated by space: ")

list1 = [randint(0, 100) for i in range(countList1)]
list2 = [int(i) for i in valueList2.split(' ')]
sumLists = sum(list1 + list2)

print(f"List 1: {list1}\n"
      f"List 2: {list2}\n"
      f"Sum o lists = {sumLists}")
