# У програмі генерується випадкове ціле число від 0 до 100.
# Користувач повинен його відгадати не більше ніж за 10 спроб.
# Після кожної невдалої спроби повинно повідомлятися чи більше чи
# менше введене користувачем число, ніж те, що загадане.
# Якщо за 10 спроб число не відгадане, то вивести загадане число.

from random import randint

randNum = randint(0, 100)
step = 0
print(randNum)
while True:

    if step >= 10:
        print("All attempts have been used!:("
              " The random value = %d" % randNum)
        break

    userNum = int(input("Enter your number: "))

    if userNum > randNum:
        print("The input number %d more than the random value" % userNum)
    elif userNum < randNum:
        print("The input number %d less than the random value" % userNum)
    else:
        print("The input number %d equal the random value %d"
              % (userNum, randNum))
        break

    step = step + 1
