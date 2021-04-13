# Для чисел, що вводяться користувачем,
# визначити відсоток додатних та від’ємних чисел.
# При введенні числа 0 закінчити роботу.
num = 1
pos = 0
neg = 0

while num != 0:
    num = int(input("Value: "))
    if num > 0:
        pos = pos + 1
    elif num < 0:
        neg += 1

if (pos + neg) != 0:
    percentPos = (pos * 100) / (pos + neg)
    percentNeg = 100 - percentPos

    print("Negative numbers = %.2f%%\n"
          "Positive numbers = %.2f%%" % (percentNeg, percentPos))

