# Матриця 5x4 заповнюється введенням з клавіатури (крім останніх елементів
# рядків). Програма повинна обчислювати суму введених елементів кожного
# рядка і записувати її в останній рядок.
# Наприкінці слід вивести отриману матрицю.

from random import randint

r = 4
c = 5
l = [[0 for col in range(c)] for row in range(r)]

print("The matrix:")
for i in range(r):
    sumRow = 0
    for j in range(c - 1):
        # input()
        l[i][j] = randint(0, 100)

        sumRow += l[i][j]
    l[i][c - 1] = sumRow
    print("{rowStr}".format(rowStr=str(l[i]).replace(",", "\t")))
