# У матриці 10x10 поміняти значення елементів у кожному рядку,
# розташовані відповідно на головній та бічній діагоналях.

from random import randint

size = 10
l = [[0 for col in range(size)] for row in range(size)]
print("old matrix: ")
for i in range(size):
    for j in range(size):
        l[i][j] = randint(0, 100)
        print("%4d" % l[i][j], end="")
    print()

for i in range(size):
    tmp = l[i][i]
    l[i][i] = l[i][size - 1 - i]
    l[i][size - 1 - i] = tmp

print("new matrix: ")
for i in range(size):
    for j in range(size):
        print("%4d" % l[i][j], end="")
    print()
