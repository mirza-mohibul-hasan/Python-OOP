class Ball:
    def __init__(self, type, color) -> None:
        self.type = type
        self.color = color

    def compare(self, ball):
        if(self.type == ball.type):
            print("Both balls are of the type: " + self.type)
        else:
            print("Balls aren't the same")

ball1 = Ball("Football","Red")
ball2 = Ball("Basketball","Blue-white")
ball3 = Ball("Football","White")

ball1.compare(ball2) # we are only sending the reference to ball2, not the whole object
ball1.compare(ball3)