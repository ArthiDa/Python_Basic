import turtle
turtle.bgcolor("black")
Cppsecrets = turtle.Screen()
Cppsecrets.title("Animation Circle ")
turtle=turtle.Turtle()
logic = 1
mod = 3
turtle.speed(0)
turtle.hideturtle()
for i in range(200):
    if mod%3 == 0:
        turtle.color("blue")
    elif logic:
        turtle.color("red")
        logic = 0
    else:
        turtle.color("green")
        logic = 1
    turtle.circle(i)
    turtle._rotate(20)
    mod += 1
