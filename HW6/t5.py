# Заповнити список випадковими додатними і від’ємними цілими числами.
# Вивести його на екран.
# Видалити з списку всі від’ємні елементи і знову вивести.

from random import randint

lenList = int(input("Enter a length of list: "))
startRandom = int(input("A random range start from (<0): "))
endRandom = int(input("A random range end from (>0): "))

list1 = [randint(startRandom, endRandom) for i in range(abs(lenList))]
print(f"The old list: {list1}")

j = 0
while j < len(list1):
    if list1[j] < 0:
        list1.pop(j)
        j -= 1
    j += 1
print(f"The New list: {list1}")
