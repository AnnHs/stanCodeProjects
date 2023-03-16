"""
File: draw line
Name: ann
-------------------------
TODO: draw a line by connecting 2 dots, and dots unshown once the line being created.
"""

from campy.graphics.gobjects import GOval, GLine
from campy.graphics.gwindow import GWindow
from campy.gui.events.mouse import onmouseclicked

SIZE = 5

#global variable
window = GWindow()
cir_count = 0
x = 0
y = 0

def main():
    """
    This program creates lines on an instance of GWindow class.
    There is a circle indicating the user’s first click. A line appears
    at the condition where the circle disappears as the user clicks
    on the canvas for the second time.
    """
    onmouseclicked(create_circle)


def create_circle(mouse):
    global cir_count ,x , y
    cir_count += 1
    if cir_count %2 != 0:
        circle = GOval(SIZE, SIZE, x=mouse.x - SIZE / 2, y=mouse.y - SIZE / 2)
        x = mouse.x
        y = mouse.y
        window.add(circle)
    else:
        cir_start = window.get_object_at(x, y)
        window.remove(cir_start)
        line = GLine(x,y,mouse.x, mouse.y)
        window.add(line)



if __name__ == "__main__":
    main()
