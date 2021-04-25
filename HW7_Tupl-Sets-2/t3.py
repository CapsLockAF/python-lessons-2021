# Задано символьний рядок. Розробити програму, яка будує і друкує в
# алфавітному порядку множину малих, множину великих латинських  літер,
# які містяться у заданому рядку, і множину цифр, яких немає у рядку.
newChars = [
            [chr(num) for num in range(48, 58)],
            [chr(capital) for capital in range(65, 91)],
            [chr(lowers) for lowers in range(97, 123)],
            ]

for i in range(3):
    newChars[i] = set(newChars[i])

val = "DCBAqwertyuiondcbvghdgvjscbGDVHFGCDGFCGHJ12547*/--"

set_val = set(val)

lowers = sorted(set_val.intersection(newChars[2]))
capitals = sorted(set_val.intersection(newChars[1]))
nums = sorted(newChars[0].difference(set_val))

print(f"String << {val} >>")
print(f"Lower case characters: {lowers}" if len(lowers) != 0
      else "No lower case characters",
      f"Capital case characters: {capitals}" if len(capitals) != 0
      else "No capital case characters",
      f"The numbers are not in the string: {nums}" if len(nums) != 0
      else "There are no numbers", sep="\n")
