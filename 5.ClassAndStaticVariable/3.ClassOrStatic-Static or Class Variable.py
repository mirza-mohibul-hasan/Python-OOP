class Player:
    team_run = 0
    # static/class variable
    # not object dependent

    def __init__(self, run):
        self.run = run

    def hit_six(self):
        self.run += 6
        Player.team_run += 6

    def hit_four(self):
        self.run += 4
        Player.team_run += 4


# Class Variable can be accessed before creating a object
print("Team ", Player.team_run)

sakib = Player(0)
tamim = Player(0)
# step-01
print("Sakib ", sakib.run)
print("Tamim ", tamim.run)
print("Team", Player.team_run)
print("Team", Player.team_run)
# step-02
sakib.hit_four()
tamim.hit_six()

print("Sakib ", sakib.run)
print("Sakib ", tamim.run)
print("Team", Player.team_run)
print("Team", Player.team_run)

# class variable can be accessed with object
print("Team", sakib.team_run)
print("Team", tamim.team_run)
