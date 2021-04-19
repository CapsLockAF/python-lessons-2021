# У списку знайти елементи, які в ньому зустрічаються тільки один раз,
# і вивести їх на екран.

from random import randint

lenList = int(input("Enter a length of list: "))
startRandom = int(input("A random range start from (<0): "))
endRandom = int(input("A random range end from (>0): "))

list1 = [randint(startRandom, endRandom) for i in range(abs(lenList))]
print(f"The old list: {list1}")

print("single count elements: ")
for elem in list1:
    if list1.count(elem) == 1:
        print(elem, end="\t")
