#!/usr/bin/env python3

import sys
import os
import itertools

MARGIN  = 3
DEFAULT_WIDTH = int(os.popen('stty size', 'r').read().split()[1]) - MARGIN

 
class Pacman():
    """ PacMan Progress Bar: 
    Parameters:
        Start: It should be 0
        End: 
        Width: Size (in chars) of the bar. Default = Console Size
        Step: Current position in the progrressbar, Default 
    """
    def __init__(self, Start=0, End=100, Width=-1, Step=0):
        self.start = Start
        self.end = End

        self.percentage = 0
        self.step = Step

        self.len = self.end - self.start

        if ((Width - MARGIN) in range(0, DEFAULT_WIDTH)):
            self.width = Width - MARGIN
        else:
            self.width = DEFAULT_WIDTH

        self.bar = "-"
        self.pacman = itertools.cycle(["\033[1;33mC\033[m", "\033[1;33mc\033[m"])
        self.candy =  itertools.cycle(["\033[0;37mo\033[m","\033[0;37m \033[m","\033[0;37m \033[m"])
        self.candybar = [None] * self.width

        for i in range(self.width):
            self.candybar[i] = next(self.candy)

        for i in range(len(self.candybar)):
            self.write(self.candybar[i])
        self.write("]")

    def update(self, value = 1):
        self.step = self.step + value
        self.draw()

    def progress(self, value):
        self.step = value
        self.draw()

    def write(self, value='', encode='UTF-8'):
        sys.stdout.buffer.write(bytes(value, encode))

    def get_console_size(self):
        return int(os.popen('stty size', 'r').read().split()[1])

    def clear():
        self.step = 0
        self.percetage = 0

    def set_percentage(self):
        self.percentage = format((100 * float(self.step)/float(self.end)),'.1f')

    def draw(self):
        
        self.set_percentage()        

        porc = "\r"+ str(self.percentage)+"%["
        pos = (((self.step/ (self.end - self.start) * 100) * (self.width - len(porc)))/ 100 )
        

        self.write(porc)     

        for i in range(int(pos)):
            self.write(self.bar)

        self.write(next(self.pacman))       
        
        sys.stdout.flush()
       



