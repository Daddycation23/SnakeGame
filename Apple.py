import turtle
from turtle import Turtle
import random
def resize_gif(input_path, output_path, size):
    # Open the GIF image
    original = Image.open(input_path)

    # Resize the image
    resized = original.resize(size, Image.LANCZOS)

    # Save the resized image as a GIF
    resized.save(output_path, format="GIF", optimize=True, quality=95)

if __name__ == "__main__":
    # Set the paths and size
    input_gif_path = "apple-waving.gif"
    output_gif_path = "apple-waving.gif"
    new_size = (20, 20)  # Set the new width and height

    # Resize the GIF
    resize_gif(input_gif_path, output_gif_path, new_size)

class Apple(Turtle):
    def __init__(self):
        super().__init__()
        turtle.register_shape("apple-waving.gif")
        self.shape("apple-waving.gif")
        self.shapesize(20, 20, 20)
        apple_xcor, apple_ycor = random.randint(-480, 480), random.randint(-480, 480)
        self.penup()
        self.teleport(apple_xcor, apple_ycor)
