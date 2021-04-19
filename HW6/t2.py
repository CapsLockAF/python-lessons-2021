# Заповнити список дійсними числами введенням з клавіатури.
# Порахувати суму і добуток елементів списку.
# Вивести на екран сам список, отримані суму і добуток його елементів.

values = input("Enter a queue of values of List 2 "
               "separated by space (1 2 ... x): ")

list1 = [float(i) for i in values.split(' ')]
sumList1 = sum(list1)
multList1 = 1
for i in list1:
    multList1 *= i

print(f"List: {list1}\n"
      f"Sum = {sumList1:.2f}\n"
      f"Multiple = {multList1:.2f}")
