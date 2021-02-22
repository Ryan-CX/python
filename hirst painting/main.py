import turtle as t
import random

t.colormode(255)
colors = ["CornflowerBlue", "DarkOrchid", "IndianRed", "DeepSkyBlue", "LightSeaGreen", "wheat", "SlateGray", "SeaGreen"]


def random_color():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    random_color = (r, g, b)
    return random_color


johnny = t.Turtle()
johnny.shape('turtle')
johnny.color('black')
num_sides = 4
next_direction = [0, 90, 180, 270]
johnny.pensize(0)
johnny.speed(0)


def draw_start(section):
    for num_sides in range(int(360 / section)):
        johnny.pencolor(random_color())
        # johnny.forward(15)
        # johnny.setheading(random.choice(next_direction))
        # johnny.forward(15)
        johnny.circle(200)
        johnny.setheading(johnny.heading() + section)
        

draw_start(5)









screen = Screen()
screen.exitonclick()
