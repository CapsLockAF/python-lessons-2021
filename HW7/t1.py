# Порахувати суми кожного рядка і кожного стовпця матриці.
# Доповнити її стовпцем, який містить суми елементів рядків та рядком,
# елементами якого є суми елементів стовпців.
from random import randint

r = int(input("Rows: "))
c = int(input("Columns: "))
l = [[0 for col in range(c)] for row in range(r)]
print("The old matrix:")
for i in range(r):
    for j in range(c):
        l[i][j] = randint(0, 100)
        print("%4d" % l[i][j], end="")
    print()

#################################
arrSumCols = [0]

for i in range(r):
    sumRow = 0
    for j in range(c):
        sumRow += l[i][j]
    l[i].append(sumRow)

for j in range(c):
    sumCol = 0
    for i in range(r):
        sumCol += l[i][j]
    arrSumCols.insert(-1, sumCol)

l.append(arrSumCols)

print("The New matrix:")
for i in range(r + 1):
    for j in range(c + 1):
        print("%4d" % l[i][j], end="")
    print()
