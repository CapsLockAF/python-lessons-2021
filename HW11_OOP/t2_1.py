# Modify the SecurityDoor class adding a custom close_and_lock()  method.
# Use super(). Try and implement it with composition.
class Door:
    def __init__(self, status="closed"):
        self.status = status

    def open(self):
        self.status = "open"

    def close(self):
        self.status = "closed"

    def is_open(self):
        return self.status == "open"


class SecurityDoor(Door):

    def __init__(self, locked=False):
        super().__init__()
        self.locked = locked

    def open(self):
        print("Try open")
        if not self.locked:
            return super().open()

    def close_end_lock(self):
        print("try close and lock")
        super().close()
        self.locked = True


door = Door()
print(f"1.the door is {door.status}")
door.open()
print(f"2.the door is {door.status}")
door.close()
print("the door is open" if door.is_open() else "the door is closed")

door1 = SecurityDoor()

print(f"-----.door  is {door1.status}")
door1.open()
print(f"-----.door locked is {door1.locked}")
print(f"-----.door  is {door1.status}")
door1.close_end_lock()
print(f"-----.door locked is {door1.locked}")
print(f"-----.door  is {door1.status}")
door1.open()
print(f"-----.door locked is {door1.locked}")
print(f"-----.door  is {door1.status}")
