# Написати функцію season, яка приймає 1 аргумент-номер місяця(від1 до 12),
# і повертає пору року, якій цей місяць належить(зима, весна,літоабо осінь)

def season(month):
    if 3 > month > 0 or month == 12:
        return "winter"
    elif 6 > month > 2:
        return "spring"
    elif 9 > month > 5:
        return "summer"
    elif 12 > month > 8:
        return "autumn"
    else:
        return "Enter from 1 to 12"


print(season(9))
