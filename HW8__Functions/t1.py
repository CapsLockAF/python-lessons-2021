# Написати функцію arithmetic, яка приймає 3 аргументи: перші 2 - числа,
# третій - операцію, яка повинна бути здійснена над ними.
# Якщо третій аргумент +, додати їх; якщо -, то відняти; *- помножити;
# / - розділити(перше на друге).В інших випадках повернути рядок
# "Невідома операція".

def arithmetic(x, y, sign):
    if sign == "+":
        return x + y
    elif sign == "-":
        return x - y
    elif sign == "*":
        return x * y
    elif sign == "/":
        return x / y
    else:
        return "Unknown operation"


print(arithmetic(2, 3, "3"))
