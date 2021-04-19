# У списку випадкових цілих чисел поміняти місцями
# мінімальний і максимальний елементи

from random import randint

lenList = int(input("Enter a length of list: "))
startRandom = int(input("A random range start from (<0): "))
endRandom = int(input("A random range end from (>0): "))

list1 = [randint(startRandom, endRandom) for i in range(abs(lenList))]
print(f"The old list: {list1}")

maxElem = list1.index(max(list1))
minElem = list1.index(min(list1))

temp = list1[maxElem]
list1[maxElem] = list1[minElem]
list1[minElem] = temp

print(list1)
