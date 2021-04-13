# Дано число P  і число H. Користувач вводить послідовність чисел.
# Визначити: суму тих чисел, які менше P; добуток чисел, які більші за H;
# кількість чисел, що знаходяться  в діапазоні значень від P до H.
# При введенні числа рівного P або H, припинити обчислення
# та вивести результат.

P = int(input("P: "))
H = int(input("H: "))
summ = 0
mult = 1
count = 0
num = 0

while num != P and num != H:
    num = int(input("Value: "))

    if num < P:
        summ = summ + num
    elif num > H:
        mult = mult * num
    elif P < num < H:
        count += 1

print("Sum of numbers = %d\n"
      "Product of numbers = %d\n"
      "Amount of numbers = %d"
      % (summ, mult, count))
