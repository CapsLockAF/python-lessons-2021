# Написати функцію is_prime, яка приймає 1 аргумент - число від 0 до 1000,
# і повертає True, якщо воно просте, і False - в іншому випадку

def is_prime(x):
    for j in range(2, x):
        if x % j == 0:
            return False
    return True

# 2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61 ...


print(is_prime(12))
