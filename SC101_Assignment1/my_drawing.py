"""
File: my drawing
Name: ann
----------------------
TODO:
"""

from campy.graphics.gobjects import GOval, GRect, GPolygon
from campy.graphics.gimage import GImage
from campy.graphics.gwindow import GWindow

window = GWindow(width=1248, height=702)


def main():
    """
    Title : Kirby!

    Kirby is my hero!! I hope it can accompany during this SC101 journey!
    """
    bg = GImage('bg.jpg')
    window.add(bg)
    # Kirby's left foot
    lf = GOval(60,25, x=550,y=603)
    lf.color = 'coral'
    lf.filled = True
    lf.fill_color = 'coral'
    window.add(lf)
    # Kirby's right foot
    rf = GOval(60, 25, x=650, y=603)
    rf.color = 'coral'
    rf.filled = True
    rf.fill_color = 'coral'
    window.add(rf)
    # Kirby's left hand
    lh = GOval(50,40, x= 520, y=520)
    lh.color = 'salmon'
    lh.filled=True
    lh.fill_color = 'pink'
    window.add(lh)
    # Kirby's right hand
    rh = GOval(50, 40, x=690, y=520)
    rh.color = 'salmon'
    rh.filled = True
    rh.fill_color = 'pink'
    window.add(rh)
    #Kirby's body
    body = GOval(160,160, x=550,y=460)
    body.color = 'pink'
    body.filled = True
    body.fill_color = 'pink'
    window.add(body)
    #Kirby's left eye
    le = GOval(22,55,x=613, y=488)
    le.filled=True
    window.add(le)
    leb = GOval(16,23,x=615, y=488 )
    leb.filled = True
    leb.fill_color = 'white'
    window.add(leb)
    # Kirby's right eye
    re = GOval(22, 55, x=648, y=488)
    re.filled = True
    window.add(re)
    reb = GOval(16, 23, x=650, y=488)
    reb.filled = True
    reb.fill_color = 'white'
    window.add(reb)
    # Kirby's mouth
    mouth = GOval(70,58,x=606,y=550)
    mouth.filled = True
    mouth.fill_color = 'coral'
    window.add(mouth)
    # star
    tri1 = GPolygon()
    tri1.add_vertex((520,540))
    tri1.add_vertex((440,540))
    tri1.add_vertex((480,485))
    tri1.color= 'yellow'
    tri1.filled = True
    tri1.fill_color = 'yellow'
    window.add(tri1)
    tri2 = GPolygon()
    tri2.add_vertex((520, 510))
    tri2.add_vertex((440, 510))
    tri2.add_vertex((480, 565))
    tri2.color = 'yellow'
    tri2.filled = True
    tri2.fill_color = 'yellow'
    window.add(tri2)








if __name__ == '__main__':
    main()
