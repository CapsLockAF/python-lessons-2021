# Записати в рядок декілька афоризмів з філософії Пайтона:
# Beautiful is better than ugly
# Explicit is better than implicit
# Simple is better than complex
# Complex is better than complicated
# Readability counts
#
# Вивести весь текст у верхньому регістрі (всі великі літери)
# Вивести весь текст у нижньому регістрі (всі великі літери)

s = "Beautiful is better than ugly\n" +\
    "Explicit is better than implicit\n" +\
    "Simple is better than complex\n" +\
    "Complex is better than complicated\n" +\
    "Readability counts\n"

print(s.upper(), s.lower(), sep="\n")
