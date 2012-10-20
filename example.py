#!/usr/bin/env python

import PacmanProgressbar


if __name__ == "__main__":
    p = PacmanProgressbar(End=100)

    for x in range(p.len):
        p.update()
        time.sleep(.18)
        
