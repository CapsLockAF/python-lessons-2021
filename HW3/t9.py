# Відома грошова сума. Розміняти її купюрами 200, 100, 10 і монетою 1 грн.,
# якщо це можливо.

amount = int(input("Input sum: "))
banknote_200 = 0
banknote_100 = 0
banknote_10 = 0

if amount >= 200:
    banknote_200 = int(amount / 200)
    amount %= 200
if amount > 100:
    banknote_100 = int(amount / 100)
    amount %= 100
if amount > 10:
    banknote_10 = int(amount / 10)
    amount %= 10

print("200 UAH * %i \n 100 UAH * %i \n 10 UAH * %i \n 1 UAH * %i"
      % (banknote_200, banknote_100, banknote_10, amount) if amount > 0
      else "Enter positive number")
