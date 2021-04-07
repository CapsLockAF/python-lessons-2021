# Дано натуральне число. Визначити, чи буде це число: парним, кратним 4.

natNum = int(input("Enter natural number: "))
val = 4
if natNum < 1:
    print(natNum, "is not a natural number")
elif natNum % 2 != 0:
    print(natNum, "is not a paired natural number")
elif natNum % val == 0:
    print(natNum, "is a multiple of", val)
else:
    print(natNum, "is a not multiple of", val)
