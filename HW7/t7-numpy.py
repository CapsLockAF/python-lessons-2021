# Змінити послідовність стовпців матриці так,
# щоб елементи її першого рядка були відсортовані за зростанням.

import numpy as np

r = int(input("Rows: "))
c = int(input("Columns: "))
l = np.random.randint(100, size=(r, c))
print("old matrix")
for i in range(r):
    for j in range(c):
        # l[i][j] = randint(0, 100)
        print("%4d" % l[i][j], end="")
    print()
###################################

sortArr = l[:, l[0].argsort()]

print("new matrix")
for i in range(r):
    for j in range(c):
        print("%4d" % sortArr[i][j], end="")
    print()
