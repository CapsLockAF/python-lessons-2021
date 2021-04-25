# chars = [[chr(i) for i in range(32)] +
#          [chr(i) for i in range(32, 48)] +
#          [chr(i) for i in range(58, 65)] +
#          [chr(i) for i in range(91, 97)] +
#          [chr(i) for i in range(123, 128)],
#          [chr(num) for num in range(48, 58)],
#          [chr(capital) for capital in range(65, 91)],
#          [chr(lower) for lower in range(97, 123)]]
# print("Grouped char-list:")
# for row in chars:
#     print(f"{row}")
# print()

newChars = [[chr(i) for i in range(32)],
            [chr(i) for i in range(32, 48)],
            [chr(num) for num in range(48, 58)],
            [chr(i) for i in range(58, 65)],
            [chr(capital) for capital in range(65, 91)],
            [chr(i) for i in range(91, 97)],
            [chr(lowers) for lowers in range(97, 123)],
            [chr(i) for i in range(123, 128)]]
print("Grouped char-list:")
for row in newChars:
    print(f"{row}")
print()
