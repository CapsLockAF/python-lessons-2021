# Чи можна в квадратному залі площею S помістити круглу сцену радіусом R
# так, щоб від стіни до сцени був прохід не менше K?

S = float(input("Square of hall: "))
R = float(input("Radius: "))
K = float(input("Passage: "))

recSide = S ** (1/2)
print("Allowed" if recSide - R >= K else "Not allowed")
