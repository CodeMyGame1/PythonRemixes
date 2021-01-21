#Packages
# - Time
import time
import os
from config import clear

class memefunc():
    def __init__(self):
        #doesn't have any particular use
        self.options = {
            "a": "addSpace()",
            "l": "lowerToUpper()",
            "f": "flip()",
            "n": "numbers()",
            "i": "increment()",
            "s": "splitString()",
            "eo": "everyOther()",
            "e": "EXIT"
        }
    def addSpace(self, string):
        a = ""
        for letter in string:
            a = a + letter + " "
        return a
    def lowerToUpper(self, string):
        b = ""
        x = 0
        for letter in string:
            if x % 2 == 0:
                b = b + letter
            else:
                b = b + letter.capitalize()
            x = x + 1
        return b

    def flip(self, string1):
        c = ""
        for letter in string1:
            c = letter + c
        return c

    def numbers(self, limit):
        for i in range(1, limit):
            for x in range(1, i):
                print(x)
            for x in range(i, 1):
                print(x)
                print()
    
    def increment(self, upperLimit):
        for x in range(upperLimit):
            print(x)

    def splitString(self, stringo):
        for x in range(len(stringo) + 1):
            for i in range(x):
                self.returnString(stringo[i])
                print()

    def returnString(self, char):
        print(char, end="", flush=True)

    def everyOther(self, sentence):
        sentence = sentence.split(" ")
        todelete = []
        todeletearchive = []
        normaltext = ""
        counter = 0
        counter2 = 0
        for x in range(len(sentence)):
            if (x % 2 != 0):
                todelete.append(x)
        for y in range(len(todelete)):
            todeletearchive.append(sentence[todelete[len(todelete)-1]])
            del sentence[todelete[len(todelete)-1]]
            del todelete[len(todelete)-1]
        for x in range((len(sentence) + len(todeletearchive))-1):
            print(counter)
            if (x % 2 == 0):
                normaltext += (sentence[counter] + " ")
            elif (x % 2 != 0):
                normaltext += ("*" + todeletearchive[counter] + "* ")

            if (counter2 % 1 == 0):
                counter += 1
            else:
                counter2 += 0.5
        print(normaltext)
        print(" ".join(sentence))
    #Main Loop
    def mainloop(self):
        while True:
            clear()
            for key in self.options.keys():
                print(key.ljust(2) + " | " + self.options[key].rjust(10))
            userInput = input("Input: ")
            choice = input("Choice (enter e to exit): ")
            if choice == "l":
                result = self.lowerToUpper(userInput)
                print(result)
            elif choice == "a":
                result1 = self.addSpace(userInput)
                print(result1)
            elif choice == "f":
                result2 = self.flip(userInput)
                print(result2)
            elif choice == "n":
                self.numbers(int(userInput))
            elif choice == "i":
                self.increment(int(userInput))
            elif choice == "s":
                self.splitString(userInput)
            elif choice == "eo":
                self.everyOther(userInput)
            elif choice == "e":
                break
            print("Press Enter to continue")
            input()