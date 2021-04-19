# Згенерувати 20 випадкових цілих чисел в діапазоні від -5 до 4,
# записати їх в список. Порахувати кількість додатних,
# від’ємних і нульових елементів.
# Вивести на екран елементи списку і пораховані кількості.

from random import randint

list1 = [randint(-4, 5) for i in range(20)]
negatives = len([i for i in list1 if i < 0])
positives = len([i for i in list1 if i > 0])
zeros = len([i for i in list1 if i == 0])

print(f"List: {list1}\n"
      f"An amount of positive values = {positives}\n"
      f"An amount of negative values = {negatives}\n"
      f"An amount of zero values = {zeros}\n ")
