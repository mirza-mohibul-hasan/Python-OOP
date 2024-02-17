class Player:
    def __init__(self, run):
        self.run = run
        self.team_run = run  # instance variable, object dependent

    def hit_six(self):
        self.run += 6
        self.team_run += 6

    def hit_four(self):
        self.run += 4
        self.team_run += 4

    def get_team_run(self):
        return self.team_run


sakib = Player(0)
tamim = Player(0)
# step-01
print("Sakib ", sakib.run)
print("Tamim ", tamim.run)
print("Team", sakib.team_run)
print("Team ", tamim.team_run)
# step-02
sakib.hit_four()
tamim.hit_six()

print("Sakib ", sakib.run)
print("Sakib ", tamim.run)
print("Team", sakib.team_run)
print("Team ", tamim.team_run)
