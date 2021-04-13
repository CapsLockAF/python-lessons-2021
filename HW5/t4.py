# Вивести на екран «прямокутник», утворений з двох видів символів.
# Контур прямокутника повинен складатися з одного символу,
# а "заливка" - з іншого.

border = input("Enter a border char: ")
fill = input("Enter a fill char: ")
widthSide = 30
heightSide = 10

i: int = 0

while i < heightSide:
    print(border * widthSide if i == 0 or i == (heightSide - 1) else
          border + fill * (widthSide - 2) + border)
    i += 1
