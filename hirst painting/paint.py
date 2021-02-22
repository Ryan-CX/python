import colorgram
import random
import turtle as t
t.colormode(255)
johnny = t.Turtle()
johnny.shape('arrow')
johnny.speed(0)

# colors = colorgram.extract('image.jpg', 30)
color_list = [(222, 216, 106), (216, 179, 174), (216, 176, 183), (189, 99, 77), (188, 163, 122),
              (188, 143, 153), (180, 93, 110), (174, 204, 178), (157, 162, 50), (144, 87, 57), (143, 69, 84),
              (139, 22, 36), (134, 177, 144), (127, 168, 193), (123, 36, 29), (83, 160, 97), (77, 18, 27), (70, 73, 33),
              (60, 118, 74), (55, 155, 185), (47, 109, 150), (46, 32, 21), (24, 92, 49), (23, 48, 31), (19, 61, 119),
              (17, 38, 65)]

johnny.setheading(225)
johnny.up()
johnny.forward(300)
johnny.down()
johnny.setheading(0)
number_of_dots = 100




for dot_counts in range(1, number_of_dots + 1):
    johnny.dot(20, random.choice(color_list))
    johnny.up()
    johnny.forward(50)
    johnny.down()
    if dot_counts % 10 == 0:
        johnny.up()
        johnny.setheading(90)
        johnny.forward(50)
        johnny.setheading(180)
        johnny.forward(500)
        johnny.setheading(0)
        johnny.down()



# for color in colors:
#     r = color.rgb.r
#     g = color.rgb.g
#     b = color.rgb.b
#     new_color = (r, g, b)
#     color_list.append(new_color)


screen = t.Screen()
screen.exitonclick()
