# Задано n рядочків символів.  Розробити програму, яка визначає і друкує
# окремо приголосні та голосні малі літери латинського алфавіту,
# які є в кожному рядку.

chars = [
         [chr(capital) for capital in range(65, 91)],
         [chr(lower) for lower in range(97, 123)]]

t = ("DhddhbjDSSDgio",
     "1hjjhe3yf*/-dh",
     "dsjhfh3jsdg4jhd",
     "fdshHGDs1233dfS",
     "")

lowers = set(chars[1])
capitals = set(chars[0])

for i in t:
     l = set(i).intersection(lowers)
     c = set(i).intersection(capitals)
     print(f"String << {i} >> includes:")
     print(f"Lower case characters: {l}" if len(l) != 0
           else "No lower case characters",
           f"Capital case characters: {c}\n" if len(c) != 0
           else "No capital case characters\n", sep="\n")

