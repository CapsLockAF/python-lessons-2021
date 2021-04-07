# Дано номер місця у плацкартному вагоні.
# Визначити, яке це місце: верхнє або нижнє, в купе або бічне.

seat = int(input("Enter the seat number: "))

if seat < 1 or seat > 53:
    print(seat, "There is no such place in the carriage")
elif seat % 2 == 0:
    print(seat, "is a top side seat" if seat > 36 else
                "is a top seat in the compartment")
else:
    print(seat, "is a down side seat" if seat > 35 else
                "is a down seat in the compartment")
