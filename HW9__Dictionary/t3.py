# 3. У змінній записаний текст. Словом вважається послідовність непорожніх
# символів, які йдуть підряд, слова розділені одним або більше пробілом.
# Програмно створіть словник, в якому ключами є слова з речення,
# а значеннями – кількість входження в речення.

text = "Сталося        це це це це це  одного чудового  весняного дня " \
       "Ясне сонце було тепле й приязне й сталося це сталося сонце тепле"


def create_list(txt):
    arr_text = txt.lower().split()
    res = {word: arr_text.count(word) for word in arr_text}
    return res


print(create_list(text))

