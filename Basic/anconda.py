# import package
import turtle 

turtle.speed(0)
turtle.up()
turtle.setpos(0,-100)
turtle.down()
radius = 100
inc = -100
for i in range(0,50):
    turtle.circle(radius)
    radius -= 2
    turtle.up()
    turtle.setpos(0,inc)
    turtle.down()
    inc += 2

for i in range(0,100):
    turtle.circle(radius)
    radius += 2
    turtle.up()
    turtle.setpos(0,inc)
    turtle.down()
    inc -= 2

