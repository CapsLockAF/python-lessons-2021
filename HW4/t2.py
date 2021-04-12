# Задано чотирицифрове натуральне число.
#
# Знайти добуток цифр цього числа.
# Записати число в реверсному порядку.

num = input("Enter the 4-digit natural number: ")

sumNum = int(num[0]) + int(num[1]) + int(num[2]) + int(num[3])
revNum = num[3] + num[2] + num[1] + num[0]

print("Sum of digits: %6s\n"
      "Reverse: %12s" % (sumNum, revNum) if len(num) == 4
      else "Enter the 4-digit natural number")
