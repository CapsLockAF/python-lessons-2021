# Задано два символьних рядка із малих і великих латинських літер та цифр.
# Розробити програму, яка будує і друкує в алфавітному порядку множину
# літер, які є в обох масивах, і множини літер окремо першого
# і другого масивів.

lowSet = set(chr(lowers) for lowers in range(97, 123))
t = ("FXRFGKJHLUjsbfbjdfgdj26568749815hjbJVDhsgfkbH",
     "a854512111100GFfdh88")

t1 = set(t[0].lower()).intersection(lowSet)
t2 = set(t[1].lower()).intersection(lowSet)
t_equal = t1.union(t2)

print(f"Set 1 = {sorted(t1)}",
      f"Set 2 = {sorted(t2)}",
      f"Set1 + Set2 = {sorted(t_equal)}",
      sep="\n")
