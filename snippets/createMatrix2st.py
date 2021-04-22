from random import randint

r = int(input("Rows: "))
c = int(input("Columns: "))
l = [[0 for col in range(c)] for row in range(r)]

for i in range(r):
    for j in range(c):
        l[i][j] = randint(0, 100)
        print("%4d" % l[i][j], end="")
    print()
print()

# sum of diagonals
sum_m = 0
for i in range(r):
    print(f"{l[i][i]}\t", end="")
    sum_m += l[i][i]
print(f">>Sum of main diagonal = {sum_m}")

for i in range(r):
    print(f"{l[i][r-1-i]}\t", end="")
    sum_m += l[i][r-1-i]
print(f">>Sum of side diagonal = {sum_m}")

# replace in readable string
strList = str(l).replace("], ", "],\n").replace(",", ",\t")
print(strList)
