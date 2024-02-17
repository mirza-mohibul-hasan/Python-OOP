class Player:
    def __init__(self, run):
        self.run = run

    def hit_six(self):
        self.run += 6

    def hit_four(self):
        self.run += 4


sakib = Player(0)
tamim = Player(0)
# step-01
print("Sakib ", sakib.run)
print("Sakib ", tamim.run)
# step-02
sakib.hit_four()
tamim.hit_six()

print("Sakib ", sakib.run)
print("Sakib ", tamim.run)
