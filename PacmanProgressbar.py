#!/usr/bin/env python3

import sys
import os
import itertools

MARGIN = 3
DEFAULT_WIDTH = int(os.popen('stty size', 'r').read().split()[1]) - MARGIN

PACMAN = ["\033[1;33mC\033[m", "\033[1;33mc\033[m"]
CANDY = ["\033[0;37mo\033[m", "\033[0;37m \033[m", "\033[0;37m \033[m"]


class Pacman():
    """ PacMan Progress Bar:
    Parameters:
        Start: It should be 0
        End: Defines the dimension of the bar in an amount of items or steps
        Width: Size (in chars) of the bar. Default = Console Size
        Step: Current position in the progrressbar, Default 0
        Text: Write some text at the beginning of the line
    """
    def __init__(self, Start=0, End=100, Width=-1, Step=0, Text=''):
        self.start = Start
        self.end = End

        self.percentage = 0
        self.step = Step

        if (Text != ''):
            self.text = Text + ': '
        else:
            self.text = ''

        self.len = self.end - self.start

        if ((Width - MARGIN) in range(0, DEFAULT_WIDTH)):
            self.width = Width - MARGIN
        else:
            self.width = DEFAULT_WIDTH

        self.bar = "-"
        self.pacman = itertools.cycle(PACMAN)
        self.candy = itertools.cycle(CANDY)
        self.candybar = [None] * self.width

        for i in range(self.width):
            self.candybar[i] = next(self.candy)

        for i in range(len(self.candybar)):
            self.__write(self.candybar[i])
        self.__write("]")

    def update(self, value=1):
        """ Update the progress in the bar
            Parameter: value, is the incresing size of the bar. By default 1
        """
        self.step = self.step + value
        self.__draw()

    def progress(self, value):
        """ Set the progress in the bar
            Parameter: value, is the specify size of the bar. No default value
        """
        self.step = value
        self.__draw()

    def __write(self, value='', encode='UTF-8'):
        sys.stdout.buffer.write(bytes(value, encode))

    def __set_percentage(self):
        self.percentage = format((100 * float(self.step) / float(self.end)), '.1f')

    def __draw(self):

        self.__set_percentage()

        porc = "\r" + str(self.text) + str(self.percentage) + "%["
        pos = (((self.step / (self.end - self.start) * 100) * (self.width - len(porc))) / 100)

        self.__write(porc)

        for i in range(int(pos)):
            self.__write(self.bar)

        self.__write(next(self.pacman))

        sys.stdout.flush()

        if (self.step == self.len):
            self.__write("\n")

