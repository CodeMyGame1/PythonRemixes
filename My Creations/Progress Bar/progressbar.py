import turtle
import time

class ProgressBar():
    def __init__(self):
        self.a = turtle.Turtle()
        self.intro = turtle.Turtle()
        self.length = 20
    def draw_bar(self):
        for x in range(2):
            self.a.forward(200)
            self.a.left(90)
            self.a.forward(20)
            self.a.left(90)
    def progress(self):
        self.a.begin_fill()
        for x in range(2):
            self.a.forward(self.length)
            self.a.left(90)
            self.a.forward(20)
            self.a.left(90)
        self.a.end_fill()
    def run(self):
        for x in range(10):
            self.progress()
            self.intro.reset()
            self.intro.penup()
            self.intro.setposition(0, -100)
            self.intro.pendown()
            self.intro.write(str((self.length/200)*100) + "%", font=('Arial', 16, 'normal'))
            self.length += 20
            time.sleep(1)
    def setup(self):
        self.a.speed(0)
        self.intro.speed(0)
        self.a.penup()
        self.a.backward(100)
        self.a.pendown()
        self.intro.penup()
        self.intro.setposition(0, -100)
        self.intro.pendown()
        self.draw_bar()
        self.run()

progressbar = ProgressBar()
progressbar.setup()
