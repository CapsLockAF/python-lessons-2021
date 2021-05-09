#  В класі Name визначте:
# *атрибути для first name та last name (fname та lname відповідно);
# *атрибут fullname що повертає first і last names;
# *атрибут initials який повертає ініціали (перші літери first та last
#  name, розділених ‘.’ .

class Name:
    def __init__(self, fname, lname):
        self.fullname = f"{fname} {lname}"
        self.initials = f"{fname[:1]}.{lname[:1]}."


name = Name("John", "Doe")

print(name.fullname)
print(name.initials)
