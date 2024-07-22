from turtle import Turtle

class Score(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        with open("data.txt", mode="r") as file:
            self.high_score = int(file.read())
        self.color("pink")
        self.penup()
        self.hideturtle()
        self.goto(0, 0)
        self.update_scoreboard()

    def update_scoreboard(self):
        self.clear()
        self.write(f"Score: {self.score} / High Score: {self.high_score}", align="center", font=("Arial", 16, "normal"))


    def reset(self):
        if self.score > int(self.high_score):  # Convert high_score to int for comparison
            self.high_score = str(self.score)
            with open("data.txt", mode="w") as file:
                file.write(f"{self.high_score}")
        self.score = 0
        self.update_scoreboard()

    def increase_score(self):
        self.score += 10
        self.clear()
        self.update_scoreboard()

