#!/usr/bin/env python
import time

from PacmanProgressbar import Pacman


if __name__ == "__main__":
    p = Pacman(End=100)

    for x in range(p.len):
        p.update()
        time.sleep(.1)
        
    print("Finalizado")