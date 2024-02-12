class House:
    cnt = 1

    def __init__(self, window, door):
        self.id = House.cnt
        self.window = window
        self.door = door
        House.cnt += 1

    def view(self):
        print(f"House {self.id} has:")
        print(f"\tWindow: {self.window}")
        print(f"\tDoor: {self.door}")

    def __add__(self, another):
        new_window = self.window + another.window
        new_door = self.door + another.door
        new_house = House(new_window, new_door)
        return new_house


h1 = House(6, 4)
h2 = House(4, 1)
h1.view()
h2.view()

h3 = (h1 + h2)
h3.view()
