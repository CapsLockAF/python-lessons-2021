# Користувач вводить число, програма повинна вивести на екран його опис.
# Наприклад, «додатне однозначне число», «від’ємне двозначне» тощо.

num = input("Input a number: ")
intNum = int(num)
length = len(num) - 1 if intNum < 0 else len(num)

if intNum == 0 or intNum == -0:
    print(num)
else:
    print("negative " + str(length) + "-digit number"
          if intNum < 0
          else "positive " + str(length) + "-digit number")
