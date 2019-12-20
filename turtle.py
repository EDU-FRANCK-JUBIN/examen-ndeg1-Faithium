# -*- coding: utf-8 -*-
"""
Created on Fri Dec 20 11:27:29 2019

@author: ilias
"""

import turtle
from random import randrange

# A NOTER
# JE NE PEUX PAS TESTER MON CODE CAR J'AI l'ERREUR AttributeError: module 'turtle' has no attribute 'Turtle'
# Obligé de redemarrer anaconda pour lancer à nouveau le code

class Rat:
    def __init__(self, name, color, x, y):
        self.name = name
        self.tortue = turtle.Turtle()
        self.tortue.color(color)
        self.tortue.up()
        self.tortue.goto(x, y)
        self.tortue.down()
        self.updateLocalPosition()
        
    def updateLocalPosition():
        self.position = self.tortue.xcor()
        
    def avancer(self):
        self.tortue.forward(randrange(6))
        self.updateLocalPosition()
        
    def estArrive(self):
        return self.position >= 1380
    
    def getParcours(self):
        return self.tortue.xcor()
    
    def stopper(self):
        self.tortue.done()

rats = [
        Rat("Michelangelo", "Orange", 50, -75),
        Rat("Leonardo", "Deep Sky Blue", 50, -235),
        Rat("Raphael", "Red", 50, -400),
        Rat("Splinter", "Dark Slate Gray", 50, -548),
        Rat("Rat5", "Pink", 50, -698)
]

gameFinished = False

while gameFinished:
    for rat in rats:
        rat.avancer
        if rat.estArrive():
            gameFinished = True
            break

# print sort rats by Rat.getParcours() (plus le temps)
print(rats.sort(key=lambda rat: rat.position))

for rat in rats:
    rat.stopper()