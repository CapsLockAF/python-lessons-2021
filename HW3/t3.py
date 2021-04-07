# Дано дійсне число. Визначити, яке це число: додатне, від’ємне, нуль.

num = float(input("Input number: "))

if num == 0:
    print("%.f equal 0" % num)
elif num < 0:
    print("%.f is negative" % num)
else:
    print("%.f is positive" % num)
