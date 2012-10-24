#!/usr/bin/env python
import time
from pacmanprogressbar import Pacman


if __name__ == "__main__":
    p = Pacman(end=100, text="asdadsasda")

    for x in range(p.len):
        p.update()
        time.sleep(.1)
        
    print("Finished")