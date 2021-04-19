# У другому списку зберегти індекси парних елементів першого списку.
# Наприклад, якщо дано список зі значеннями 8, 3, 15, 6, 4, 2,
# то  другий треба заповнити значеннями 1, 4, 5, 6
# (або 0, 3, 4, 5 - якщо індексація починається з нуля),
# оскільки саме в цих позиціях першого масиву стоять парні числа.

from random import randint

lenList = int(input("Enter a length of list: "))
startRandom = int(input("A random range start from (<0): "))
endRandom = int(input("A random range end from (>0): "))

list1 = [randint(startRandom, endRandom) for i in range(abs(lenList))]
print(f"The old list: {list1}")

listEven = []
for i in range(len(list1)):
    if list1[i] % 2 == 0:
        listEven.append(i)
print(f"The old list: {listEven}")
