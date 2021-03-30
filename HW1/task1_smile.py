firstSymbol = input("Input the first symbol: ")
secondSymbol = input("Input the second symbol: ")

row_1 = firstSymbol*2 + secondSymbol + firstSymbol*4 + secondSymbol + firstSymbol*2
row_2 = firstSymbol + secondSymbol*3 + firstSymbol*2 + secondSymbol*3 + firstSymbol
row_3 = row_1
row_4 = firstSymbol*10
row_5 = secondSymbol*2 + firstSymbol*6 + secondSymbol*2
row_6 = firstSymbol + secondSymbol*2 + firstSymbol*4 + secondSymbol*2 + firstSymbol
row_7 = firstSymbol*3 + secondSymbol*4 + firstSymbol*3

print(firstSymbol*10 + "\n", row_1 + "\n", row_2 + "\n",\
     row_3 + "\n", row_4 + "\n", row_5 + "\n",\
          row_6 + "\n", row_7 + "\n", firstSymbol*10)

