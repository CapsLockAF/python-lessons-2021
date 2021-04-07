# Залежно від вибору користувача, обчислити площу або прямокутника,
# або трикутника, або круга. Якщо обрані прямокутник або трикутник,
# то треба запросити довжини сторін; круга – його радіус.

# "rectangle" = 1, "triangle" = 2, "circle" = 3
# the angle of triangle equal 90 deg

from math import pi

shape = int(input("The shape: "))
square = 0
shapes = ["rectangle", "triangle", "circle"]

if shape == 3:
    radius = float(input(shapes[shape - 1] + " radius: "))
    square = pi * radius ** 2
elif 0 < shape < 3:
    sideRec1 = float(input(shapes[shape - 1] + " side 1: "))
    sideRec2 = float(input(shapes[shape - 1] + " side 2: "))
    if shape == 1:
        square = sideRec1 * sideRec2
    elif shape == 2:
        square = sideRec1 * sideRec2 / 2

print(shapes[shape - 1] + " :square is = %.2f" % square
      if 0 < shape < 4
      else "1, 2, 3")
