# Створіть словник, зв'язавши його з змінною school, і наповніть його
# даними, які б відображали кількість учнів в десяти різних класах
# (наприклад, 1а, 1б, 2б, 6а, 7в тощо.).
# Дізнайтеся скільки людей в певному класі.
# Уявіть, що в школі відбулися зміни, додайте їх в словник:
# - В трьох класах змінилося кількість учнів;
# - В школі з'явилося два нових класи;
# - В школі розформували один з класів.
# Виведіть вміст словника на екран.

classes = [("1a", "20"), ("1б", "15"), ("2г", "19"),
           ("3в", "18"), ("7а", "22"), ("9б", "1")]

school = dict(classes)


def create_class(obj, *argv):
    """arg should be a tuple or a list that includes two strings;
the function creates new key and value in dict"""
    new = dict(obj)
    for arg in argv:
        if arg[0] not in new:
            new[arg[0]] = arg[1]
        else:
            print(f"The key '{arg[0]}' in the dictionary exists already!")
    return new


def del_class(obj, *argv):
    """arg should be a single string;
the function remove the key in dict"""
    new = dict(obj)
    for arg in argv:
        if arg in new:
            new.pop(arg)
        else:
            print(f"The key '{arg}' in the dictionary doesn't exist!")
    return new


def change_class(obj, *argv):
    """arg should be a tuple or a list that includes two strings;
the function changes the value in key in dict"""
    new = dict(obj)
    for arg in argv:
        if arg[0] in new:
            new[arg[0]] = arg[1]
        else:
            print(f"The key '{arg[0]}' in the dictionary doesn't exist!")
    return new


def get_school_info(d):
    """prints a table as a string"""
    d2 = sorted(d.items())
    s = f"| Class  |Students|\n"
    buff = len(s) - 1
    for key, value in d2:
        s += f"{'-'*buff}\n|{key:^8}|{value:^8}|\n"
    return s


print(f"{get_school_info(school)}")

school1 = change_class(school, ("1a", 50), ("1б", 40), ("", 2000))
print(f"{get_school_info(school1)}")

school2 = create_class(school1, ("1a", 50), ("2a", 25), ("2в", 12))
print(f"{get_school_info(school2)}")

school3 = del_class(school2, "1a", "16k", "22")
print(f"{get_school_info(school3)}")

# just, I looked  functional possibilities in python:)
