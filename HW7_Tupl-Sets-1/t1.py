# Вивести на екран послідовність привітань, але таким чином, щоб ті,
# хто записаний за іменами, вітати словом «Hello», а «Mr.» чи «Mrs.»
# вітати Good morning.

names = ("Ann", "Bob", "Elizabeth", "Mr. McMullen", "Mrs. Smith")
for name in names:
    print(f"Good morning, {name}!" if "." in name
          else f"Hello {name}!")
print()

# Створити список, що містить цифри, літери алфавіту (великі та малі),
# спеціальні символи;
chars = []
for c in range(128):
    chars.append(chr(c))
print(f"Chars = {chars}\n")

# Розділити список на декілька, кожний з яких містить тільки цифри,
# тільки літери тощо;
newChars = [[chars[i] for i in range(32)],
            [chars[i] for i in range(32, 48)],
            [chars[num] for num in range(48, 58)],
            [chars[i] for i in range(58, 65)],
            [chars[capital] for capital in range(65, 91)],
            [chars[i] for i in range(91, 97)],
            [chars[lowers] for lowers in range(97, 123)],
            [chars[i] for i in range(123, 128)]]
print("Grouped char-list:")
for row in newChars:
    print(f"{row}")
print()

# Конвертувати списки в кортежі;
for i in range(len(newChars)):
    newChars[i] = tuple(newChars[i])
print("Tuples in list:")
for row in newChars:
    print(f"{row}")

# Ввести з клавіатури почергово цифру, літеру чи спецсимвол і повернути
# відповідно індекс входження у відповідний кортеж;
print()
inputValue = "h"
for i in range(len(newChars)):
    if inputValue in newChars[i]:
        print(f"Index of '{inputValue}' = "
              f"newChars[{i}][{newChars[i].index(inputValue)}]\n")
        break

# Відобразити реверс одного з кортежів

rev_t = newChars[2][::-1]
print(f"Old tuple {newChars[2]}:\n"
      f"Reversed tuple {rev_t}")

