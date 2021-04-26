# Написати функцію date, яка приймає 3 аргументи - день, місяць і рік.
# Повернути True, якщо така дата є в нашому календарі,
# і False - в іншому випадку

our_date = (10, 12, 2021)


def date(d, m, y):
    return True if our_date == (d, m, y) else False


print(date(10, 12, 2021))
