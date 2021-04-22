# Знайти максимальний елемент серед мінімальних елементів стовпців матриці
from random import randint

r = int(input("Rows: "))
c = int(input("Columns: "))
l = [[0 for col in range(c)] for row in range(r)]

for i in range(r):
    for j in range(c):
        l[i][j] = randint(0, 100)
        print("%4d" % l[i][j], end="")
    print()

minList = []
for j in range(c):
    colList = []
    for i in range(r):
        colList.append(l[i][j])
    minList.append(min(colList))
print(f"Max value from min elements of matrix columns is = {max(minList)}")
