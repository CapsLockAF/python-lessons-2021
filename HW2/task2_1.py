from math import pi

# Задана вага в грамах. Визначити вагу в тонах і кілограмах
weight = float(input("Input the weight in grams: "))
print("The weight in kilograms:", str(weight/1000) + " kg\n",
      "The weight in tonnes:", str(weight/1000000) + " tons")

# Відомий обсяг інформації в байтах. Перевести в кілобайти, мегабайти
bytesValue = int(input("Input the value in bytes: "))
print("The info in kilobytes:", str(bytesValue/1024) + " kb\n",
      "The info in megabytes:", str(bytesValue/1024**2) + " mb")

# Користувач вводить два числа. Одне присвоюється одній змінній, а друге -
# іншій. Необхідно поміняти значення змінних так, щоб значення першої
# виявилося в другій, а другої - у першій.
val1 = input("Input the first value: ")
val2 = input("Input the second value: ")
buff = val1
val1 = val2
val2 = buff
print("Changed first value:", val1, "\n",
      "Changed second value:", val2)

# Обчислити площу і периметр прямокутника за заданими шириною і висотою
recWeight = float(input("Input the weight of rectangle: "))
recHeight = float(input("Input the height of rectangle: "))
recSquare = recWeight * recHeight
recPerimeter = recWeight*2 + recHeight*2
print("Square = %.2f and perimeter = %.2f " % (recSquare, recPerimeter))

# Обчислити площу і периметр кола по заданому радіус
radius = float(input("Input the circle radius: "))
length = 2 * pi * radius
square = pi * radius ** 2
print("Length = %.2f and square = %.2f" % (length, radius))

# по двом введеним користувачем катетам прямокутного трикутника обчислити
# довжину гіпотенузи
leg1 = float(input("Input the first leg: "))
leg2 = float(input("Input the second leg: "))
hypotenuse = (leg1 ** 2 + leg2 ** 2) ** (1/2)
print("Hypotenuse = %.2f" % hypotenuse)
