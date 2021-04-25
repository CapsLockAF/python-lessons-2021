# Задано символьний рядок. Розробити програму, яка вилучає з цього рядка
# всі повторні входження цифр і знаків арифметичних операцій.

val = "1g122345++-1ggFF=*//"
symbols = set("+-*/=0123456789")
print(val)

l_val = list(val)
i = 1
while i < len(l_val):
    if l_val[i] in symbols and l_val[i] in l_val[:i]:
        l_val.pop(i)
        i -= 1
    i += 1
print("".join(l_val))


