import turtle
from turtle import Turtle, Screen
import time
import random
from Snake import Snake
from score import Score
from Apple import Apple
from PIL import Image, ImageFilter



screen = Screen()
screen.setup(width=1000, height=1000)
screen.title("Snake Game")
screen.bgcolor("black")

snake = Snake()
apple = Apple()

screen.listen()
screen.onkey(key="Up", fun=snake.go_north)
screen.onkey(key="Down",fun=snake.go_south)
screen.onkey(key="Left",fun=snake.go_east)
screen.onkey(key="Right", fun=snake.go_west)
screen.onkeypress(key="Escape", fun=snake.exit_game)

scoreboard = Score()

game_on = True

while game_on:
    screen.update()
    time.sleep(0.01)
    snake.move()
    if snake.body[0].distance(apple) < 20:
        apple_xcor, apple_ycor = random.randint(-480, 480), random.randint(-480, 480)
        apple.teleport(apple_xcor, apple_ycor)
        snake.extend_body()
        scoreboard.increase_score()

    if (
            snake.body[0].xcor() < -490
            or snake.body[0].xcor() > 490
            or snake.body[0].ycor() < -490
            or snake.body[0].ycor() > 490
    ):

        scoreboard.reset()
        snake.reset()



screen.exitonclick()