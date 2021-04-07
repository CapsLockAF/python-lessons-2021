# Відомий РІК. Визначити, чи буде цей рік високосним,
# і до якого століття цей рік відноситься.

from math import floor

year = int(input("Input the year: "))

print("Leap Year, century: " + str(floor(year / 100 + 1))
      if year % 4 == 0 or year % 100 == 0 and year % 400 == 0
      else "NOT a Leap Year")

