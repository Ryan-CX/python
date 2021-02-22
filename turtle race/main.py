from turtle import Turtle, Screen
import  random
is_race_on = False
screen = Screen()
screen.setup(width=500, height=400)  #500 wide 400 height
user_bet = screen.textinput(title='Make your bets.', prompt='Which turtle will win? Enter the color.')
colors = ['red', 'orange', 'purple', 'yellow', 'green', 'blue']
y_position = [-50, -100, 0, 50, 100, 150]
all_turtles = []

for index in range(0,6):
    new_turtle = Turtle(shape='turtle')
    new_turtle.penup()
    new_turtle.color(colors[index])
    new_turtle.goto(x=-230, y=y_position[index])
    all_turtles.append(new_turtle)

if user_bet:
    is_race_on = True

while is_race_on:
    for turtle in all_turtles:
        random_distance = random.randint(0, 10)
        turtle.forward(random_distance)

        if turtle.xcor() > 230:
            is_race_on = False
            winning_color = turtle.pencolor()
            if winning_color == user_bet:
                print(f"you won, the {winning_color} is the winner! ")
            else:
                print(f"you lost, the {winning_color} is the winner! ")















screen.exitonclick()