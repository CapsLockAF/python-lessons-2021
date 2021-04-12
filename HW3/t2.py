# Дано натуральне число. Визначити, чи буде це число: непарним, кратним 5.

natNum = int(input("Enter natural number: "))
val = 5

if natNum < 1:
    print(natNum, "is not a natural number")
elif natNum % 2 == 0:
    print(natNum, "is a paired natural number. Try again.")
elif natNum % val == 0:
    print(natNum, "is a multiple of", val)
else:
    print(natNum, "is a not multiple of", val)
