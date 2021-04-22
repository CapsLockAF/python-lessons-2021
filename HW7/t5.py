# Дві матриці заповнюються введенням з клавіатури.
# В елементи третьої матриці такої ж розмірності записати більші з
# відповідних елементів перших двох.

from random import randint

r = int(input("Rows: "))
c = int(input("Columns: "))

l1 = [[0 for col1 in range(c)] for row1 in range(r)]
l2 = [[0 for col2 in range(c)] for row2 in range(r)]
lmax = [[0 for col3 in range(c)] for row3 in range(r)]

print("Matrix 1:")
for i in range(r):
    for j in range(c):
        l1[i][j] = randint(0, 100)
        print("%4d" % l1[i][j], end="")
    print()
print("Matrix 2:")
for i in range(r):
    for j in range(c):
        l2[i][j] = randint(0, 100)
        print("%4d" % l2[i][j], end="")
    print()
print("Compared matrix:")
for i in range(r):
    for j in range(c):
        if l1[i][j] > l2[i][j] or l1[i][j] == l2[i][j]:
            lmax[i][j] = l1[i][j]
        else:
            lmax[i][j] = l2[i][j]
        print("%4d" % lmax[i][j], end="")
    print()
