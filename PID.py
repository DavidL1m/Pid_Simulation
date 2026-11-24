import numpy as np
import matplotlib
import turtle

#Global Params
TIMER = 0
SETPOINT = 10

#-------------

class Simulation(object):
    def __init__(self):
        self.screen = turtle.Screen()
        self.screen.setup(1280, 900)
        self.marker = turtle.Turtle()
        self.marker.penup()
        self.marker.left(180)
        self.marker.goto(15,SETPOINT)
        self.marker.color("red")
        self.sim = True
        self.timer = 0
        def cycle(self):
            while(self.sim):
                if 
def main():
    sim = Simulation()
    sim.cycle()
