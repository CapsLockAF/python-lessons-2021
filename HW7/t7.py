# Змінити послідовність стовпців матриці так,
# щоб елементи її першого рядка були відсортовані за зростанням.

from random import randint

r = int(input("Rows: "))
c = int(input("Columns: "))
l = [[0 for col in range(c)] for row in range(r)]
print("old matrix")
for i in range(r):
    for j in range(c):
        l[i][j] = randint(0, 100)
        print("%4d" % l[i][j], end="")
    print()
###################################
s = sorted(l[0])
# workaround !!!!


print(f"{s}")
######################################
print("new matrix")
for i in range(r):
    for j in range(c):
        print("%4d" % l[i][j], end="")
    print()
