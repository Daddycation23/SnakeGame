from turtle import Turtle, Screen
import time

move_distance = 20
starting_pos = [(0, 0), (-20, 0), (-40, 0)]
north = 90
south = 270
east = 180
west = 0
screen = Screen()
class Snake:
    def __init__(self):
        self.body = []
        self.create_snake_head()

    def create_snake_head(self):
        for pos in starting_pos:
            snake_head = Turtle("square")
            snake_head.color("white")
            snake_head.penup()
            snake_head.speed("fastest")
            snake_head.goto(0, 0)
            self.body.append(snake_head)
    def game_over(self):
        text_turtle = Turtle()
        text_turtle.color("pink")
        text_turtle.penup()
        text_turtle.hideturtle()
        text_turtle.goto(0, 100)
        text_turtle.write("U LOST!", align="center", font=("Arial", 20, "normal"))
        time.sleep(2)
        screen.bye()

    def exit_game(self):
        screen.bye()

    def move(self):

        for i in range(len(self.body) - 1, 0, -1):
            x_cor, y_cor = self.body[i - 1].position()
            self.body[i].goto(x_cor, y_cor)
        self.body[0].forward(move_distance)
        for segment in self.body[1:]:
            if self.body[0].distance(segment) < 10:  # Adjust the distance based on your preference
                self.game_over()



    def speedup(self):
        self.body[0].forward(move_distance * 2)

    def go_north(self):
        if self.body[0].heading() != south:
            self.body[0].setheading(north)


    def go_south(self):
        if self.body[0].heading() != north:
            self.body[0].setheading(south)

    def go_east(self):
        if self.body[0].heading() != west:
            self.body[0].setheading(east)

    def go_west(self):
        if self.body[0].heading() != east:
            self.body[0].setheading(west)

    def extend_body(self):
        new_segment = Turtle("square")
        new_segment.hideturtle()
        new_segment.color("white")
        new_segment.penup()
        x_cor, y_cor = self.body[-1].xcor(), self.body[-1].ycor()
        new_segment.teleport(x_cor, y_cor)
        self.body.append(new_segment)
        new_segment.showturtle()


    def reset(self):
        for bod in self.body:
            bod.teleport(1000, 1000)
        self.body.clear()
        self.create_snake_head()

