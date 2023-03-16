"""
File: bouncing ball
Name: ann
-------------------------
TODO:
"""

from campy.graphics.gobjects import GOval
from campy.graphics.gwindow import GWindow
from campy.gui.events.timer import pause
from campy.gui.events.mouse import onmouseclicked

VX = 3
DELAY = 10
GRAVITY = 1
SIZE = 20
REDUCE = 0.9
START_X = 30
START_Y = 40

#global variables
window = GWindow(800, 500, title='bouncing_ball.py')
ball = GOval(SIZE, SIZE)
clicks = 0
vy = 0



def main():
    """
    This program simulates a bouncing ball at (START_X, START_Y)
    that has VX as x velocity and 0 as y velocity. Each bounce reduces
    y velocity to REDUCE of itself.
    """
    ball.filled = True
    window.add(ball, x = START_X, y = START_Y)
    onmouseclicked(bounce)


def bounce(m):
    global clicks, n, vy
    if clicks < 3:
        x = START_X
        y = START_Y
        while x < 800:
            while y + SIZE < 500:
                pause(DELAY)
                window.clear()
                x += VX
                vy += GRAVITY
                if y+vy+SIZE < 500:
                    y += vy
                else:
                    y = 500 - SIZE
                window.add(ball, x,y)
            vy = -vy
            if vy < 0:
                vy * REDUCE
            while vy < 0:
                pause(DELAY)
                window.clear()
                x += VX
                if vy+GRAVITY>0:
                    vy = 0
                else:
                    vy += GRAVITY
                y += vy
                window.add(ball, x, y)
        clicks += 1
        window.add(ball, x=START_X, y=START_Y)







if __name__ == "__main__":
    main()
