# Задано символьний рядок,. Розробити програму, яка знаходить групи цифр,
# записаних підряд, і вилучає із них всі початкові нулі, крім останнього,
# якщо за ним знаходиться крапка. Друкує модифікований масив
# по сорок символів у рядку.

numSet = set(chr(num) for num in range(48, 58))
numSet.add(".")
val = "d123xx000.25xx00000005mm00.111d*/-55500dfsdf54786"
arr = []
row = "0" * 40
i = 0

# workaround!!!
while i < len(val):
    if val[i] in numSet:
        buff_i = i
        while val[buff_i] in numSet:

            buff_i += 1
            if buff_i == len(val):
                break

        row = val[i:buff_i]
        arr.append(row)
        i = buff_i
    i += 1
print(arr)







