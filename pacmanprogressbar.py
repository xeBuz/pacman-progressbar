#!/usr/bin/env python
# coding: utf-8

# pacmanprogress.py

import sys
import os
import itertools

__version__ = "0.3.1"

MARGIN = 3
DEFAULT_WIDTH = int(os.popen('stty size', 'r').read().split()[1]) - MARGIN

PACMAN = ["\033[1;33mC\033[m", "\033[1;33mc\033[m"]
CANDY = ["\033[0;37mo\033[m", "\033[0;37m \033[m", "\033[0;37m \033[m"]


class Pacman():
    """PacMan Progress Bar"""

    def __init__(self, start=0, end=100, width=-1, step=0, text=''):
        """Create a new instance

        Parameters:
            start: It should be 0
            end: Defines the bar's dimenssion in an amount of items or steps
            width: Size (in chars) of the bar. Default = Console Size
            step: Current position in the progrressbar, Default 0
            text: Write some text at the beginning of the line

        """
        self.start = start
        self.end = end
        self.percentage = 0
        self.step = step
        self.text = text + ': ' if text != '' else ''
        self.len = self.end - self.start
        if ((width - MARGIN) in range(0, DEFAULT_WIDTH)):
            self.width = width - MARGIN
        else:
            self.width = DEFAULT_WIDTH
        self.bar = "-"
        self.pacman = itertools.cycle(PACMAN)
        self.candy = itertools.cycle(CANDY)
        self.candybar = [None] * self.width

        for i in range(self.width):
            self.candybar[i] = next(self.candy)

        for i in range(len(self.candybar)):
            self._write(self.candybar[i])
        self._write("]")

    def _write(self, value='', encode='UTF-8'):
        if sys.version_info.major == 3:
            sys.stdout.buffer.write(bytes(value, encode))
        else:
            sys.stdout.write(value)

    def _set_percentage(self):
        step = float(self.step)
        end = float(self.end)
        self.percentage = format((100 * step / end), '.1f')

    def _draw(self):
        self._set_percentage()
        porc = "\r" + str(self.text) + str(self.percentage) + "%["
        pos = (((self.step / (self.end - self.start) * 100)
               * (self.width - len(porc))) / 100)
        self._write(porc)
        for i in range(int(pos)):
            self._write(self.bar)
        self._write(next(self.pacman))
        sys.stdout.flush()

        if self.step == self.len:
            self._write("\n")

    def update(self, value=1):
        """ Update the progress in the bar
            Parameter: value, is the incresing size of the bar. By default 1
        """
        self.step = self.step + float(value)
        self._draw()

    def progress(self, value):
        """ Set the progress in the bar
            Parameter: value, is the specific size of the bar. No default value
        """
        self.step = float(value)
        self._draw()
