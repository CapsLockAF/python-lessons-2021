# Написати функцію square, яка приймає 1 аргумент - сторону квадрата,
# і повертає 3 значення(за допомогою кортежу): периметр квадрата,
# площу квадрата і діагональ квадрата.

def square(side):
    p = side * 4
    s = side ** 2
    d = side ** (1/2)
    return p, s, d


print(square(5))
