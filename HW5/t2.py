# Вводяться десять натуральних чисел більше  2.
# Порахувати, скільки серед них чисел, що кратні 5-ти.

step = 0
count = 0

while True:

    if step == 10:
        print("Multiples of 5: %d numbers" % count)
        break

    num = int(input("Input  number: "))
    if num <= 2:
        print("The input value must be greater than 2")
    elif num % 5 == 0:
        count += 1
        step = step + 1
    else:
        step = step + 1
