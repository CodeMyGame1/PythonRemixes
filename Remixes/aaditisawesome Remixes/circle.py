#Original code remixed from: aaditisawesome
#User: https://github.com/aaditisawesome 
import time
import turtle
import random
class MyTurtle(turtle.Turtle):
    def __init__(self):
        turtle.Turtle.__init__(self)
        self.showturtle()
        self.name = ""
        self.age = 0
        self.color1 = ""
        self.repeato = 0
    def writeclear(self, text, sleep):
        self.write(text, font=("Arial", 16, "normal"))
        time.sleep(sleep)
        self.reset()
    def intro(self):
        self.goto(0, 0)
        self.write("What is your name? ", font=("Arial", 16, "normal"))
        self.name = input()
        self.reset()
        self.writeclear("Hello, %s" % (self.name), 1)
        self.write("How old are you? ", font=("Arial", 16, "normal"))
        self.age = input()
        self.reset()
        self.writeclear('Kool, next year you will be %d!' % (int(self.age) + 1), 2)
        self.write("What is your favorite color? ", font=("Arial", 16, "normal"))
        self.color1 = input()
        self.reset()
        self.writeclear('Just one more question, sorry!', 2)
        self.write("Enter a positive integer ", font=("Arial", 16, "normal"))
        self.repeato = int(input())
        self.reset()
        self.writeclear("Wow! Wait a second, lemme show you something you may like...", 2)
    def pattern(self): #make pattern adjustible to different values, oops that kinda failed
        for i in range(self.repeato):
            for c in range(int(self.repeato/12)):
                self.circle(100, self.repeato*1.25)
                self.right(30)
            self.up()
            self.left(self.repeato * 18)
            self.down()
    def outro(self):
        print('I made this just for you, %s. It is %s, your favorite color! Dont you like it?' % (self.name, self.color1))
        print('Well, nice meeting you! I gtg bi!')
audit = MyTurtle()
audit.intro()
audit.speed(0)
audit.width(5)
audit.color(audit.color1)
if audit.color1 == 'white':
    audit.bgcolor("black")
else:
    audit.bgcolor("white")
audit.pattern()
audit.outro()