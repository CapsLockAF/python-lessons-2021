# Сформувати матрицю з чисел від 0 до 999, вивести її на екран.
# Порахувати кількість двозначних чисел в ній.
from random import randint

r = int(input("Rows: "))
c = int(input("Columns: "))
l = [[0 for col in range(c)] for row in range(r)]

count = 0
print("The old matrix:")
for i in range(r):
    for j in range(c):
        l[i][j] = randint(0, 999)
        print("%4d" % l[i][j], end="")

        if 100 > l[i][j] > 9:
            count += 1
    print()

print(f"2-digit numbers = {count}")
