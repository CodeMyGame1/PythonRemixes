# This is the original version, created by aaditisawesome
#User: https://github.com/aaditisawesome 
import time
import turtle
name = input("What is your name? ")
time.sleep(2)
print("Hello, "+ name)
time.sleep(1)
age = input("How old are you? ")
time.sleep(2)
print('Kool, next year you will be', str(int(age) + 1) , '!')
time.sleep(2)
color =input("What is you favorite color? ")
time.sleep(2)
print('Wow! Wait a second, lemme show you something you may like...')
time.sleep(2)
audit = turtle.Pen()
audit.speed(0)
audit.width(5)
audit.color(color)
if color == 'white':
    turtle.bgcolor("black")
else:
    turtle.bgcolor("white")
for i in range(72):
     for i in range(6):
             audit.circle(100, 90)
             audit.right(30)
     audit.up()
     audit.left(5)
     audit.down()
import time
print('I made this just for you,', name , '. It is', color, ', your favorite color! Dont you like it?')
time.sleep(2)
print('Well, nice meeting you! I gtg bi!')
input()