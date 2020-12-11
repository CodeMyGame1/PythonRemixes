import turtle
import time

a = turtle.Turtle()
intro = turtle.Turtle()

length = 20
def draw_bar():
    for x in range(2):
        a.forward(200)
        a.left(90)
        a.forward(20)
        a.left(90)
def progress():
    a.begin_fill()
    for x in range(2):
        a.forward(length)
        a.left(90)
        a.forward(20)
        a.left(90)
    a.end_fill()

def setup():
    a.speed(0)
    intro.speed(0)
    a.penup()
    a.backward(100)
    a.pendown()
    intro.penup()
    intro.setposition(0, -100)
    intro.pendown()
    draw_bar()

setup()
for x in range(10):
    progress()
    intro.reset()
    intro.penup()
    intro.setposition(0, -100)
    intro.pendown()
    intro.write(str((length/200)*100) + "%", font=('Arial', 16, 'normal'))
    length += 20
    time.sleep(1)

