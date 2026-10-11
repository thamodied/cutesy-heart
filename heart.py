import turtle
import math
import time
screen = turtle.Screen()
screen.setup(700, 700)
screen.bgcolor("black")
screen.colormode(1.0)
screen.tracer(0)

t = turtle.Turtle()
t.hideturtle()
t.speed(0)

def heart_x(angle):
    return 16 * (math.sin(angle) ** 3)

def heart_y(angle):
    return 13 * math.cos(angle) - 5 * math.cos(2 * angle) - 2 * math.cos(3 *angle) - math.cos(4 *angle)

N = 200
outer_scale = 18.0
inner_scale = 5.0
steps = 20

c_outer = (1.0, 0.70, 0.78)
c_inner = (0.0, 0.0, 0.0)

for i in range(N):
    angle = 2 * math.pi * i / N

    xo = heart_x(angle) * outer_scale
    yo = heart_y(angle) * outer_scale

    xi = heart_x(angle) * inner_scale
    yi = heart_y(angle) * inner_scale

    for j in range (steps):
        f1 = j / steps
        f2 = (j + 1) / steps

        x1 = xo + (xi - xo) * f1
        y1 = yo + (yi - yo) * f1
        x2 = xo + (xi - xo) * f2
        y2 = yo + (yi - yo) * f2

        r = c_outer[0] + (c_inner[0] - c_outer[0]) * f1
        g= c_outer[1] + (c_inner[1] - c_outer[1]) * f1
        b = c_outer[2] + (c_inner[2] - c_outer[2]) * f1

        w = 2.2 - (1.7 * f1)

        t.pencolor(r, g, b)
        t.width(w)
        t.penup()
        t.goto(x1, y1)
        t.pendown()
        t.goto(x2, y2)

        screen.update()
        time.sleep(0.001)

    time.sleep(0.03)
turtle.done()
