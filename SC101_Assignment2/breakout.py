"""
stanCode Breakout Project
Adapted from Eric Roberts's Breakout by
Sonja Johnson-Yu, Kylie Jue, Nick Bowman,
and Jerry Liao.

YOUR DESCRIPTION HERE
"""

from campy.gui.events.timer import pause
from breakoutgraphics import BreakoutGraphics

FRAME_RATE = 10         # 100 frames per second
NUM_LIVES = 3			# Number of attempts

# gobal variable
graphics = BreakoutGraphics()


def main():
    global graphics
    lives = NUM_LIVES

    while True:
        if lives == 0 or graphics.bricks_num == 0:
            break
        pause(FRAME_RATE)
        graphics.ball.move(graphics.get_dx(), graphics.get_dy())
        if graphics.ball.x <= 0 or graphics.ball.x >= graphics.window.width - graphics.ball.width:
            graphics.reflect_ball_x()
        if graphics.ball.y <= 0:
            graphics.reflect_ball_y()
        elif graphics.ball.y >= graphics.window.height:
            lives -= 1
            graphics.reset_ball()

        # collision check
        ball_ul = graphics.window.get_object_at(graphics.ball.x, graphics.ball.y)
        ball_ur = graphics.window.get_object_at(graphics.ball.x + graphics.ball.width, graphics.ball.y)
        ball_bl = graphics.window.get_object_at(graphics.ball.x, graphics.ball.y + graphics.ball.height)
        ball_br = graphics.window.get_object_at(graphics.ball.x + graphics.ball.width,
                                                graphics.ball.y + graphics.ball.height)
        if ball_ul is not None:
            reflection(ball_ul)
        elif ball_ur is not None:
            reflection(ball_ur)
        elif ball_bl is not None:
            reflection(ball_bl)
        elif ball_br is not None:
            reflection(ball_br)


def reflection(ball):
    global graphics
    # remove the hit brick and reflect the ball
    if ball != graphics.paddle:
        graphics.window.remove(ball)
        graphics.bricks_num -= 1
        graphics.reflect_ball_y()
    # when hit paddle, reflect
    else:
        if graphics.get_dy() > 0:
            graphics.reflect_ball_y()

if __name__ == '__main__':
    main()
