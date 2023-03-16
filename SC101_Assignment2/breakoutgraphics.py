"""
stanCode Breakout Project
Adapted from Eric Roberts's Breakout by
Sonja Johnson-Yu, Kylie Jue, Nick Bowman, 
and Jerry Liao.

YOUR DESCRIPTION HERE
"""
from campy.graphics.gwindow import GWindow
from campy.graphics.gobjects import GOval, GRect, GLabel
from campy.gui.events.mouse import onmouseclicked, onmousemoved
from campy.graphics.gimage import GImage
import random

BRICK_SPACING = 5      # Space between bricks (in pixels). This space is used for horizontal and vertical spacing
BRICK_WIDTH = 40       # Width of a brick (in pixels)
BRICK_HEIGHT = 15      # Height of a brick (in pixels)
BRICK_ROWS = 10        # Number of rows of bricks
BRICK_COLS = 10        # Number of columns of bricks
BRICK_OFFSET = 50      # Vertical offset of the topmost brick from the window top (in pixels)
BALL_RADIUS = 10       # Radius of the ball (in pixels)
PADDLE_WIDTH = 75      # Width of the paddle (in pixels)
PADDLE_HEIGHT = 15     # Height of the paddle (in pixels)
PADDLE_OFFSET = 50     # Vertical offset of the paddle from the window bottom (in pixels)
INITIAL_Y_SPEED = 7    # Initial vertical speed for the ball
MAX_X_SPEED = 5        # Maximum initial horizontal speed for the ball
BRICK_COLORS = ['red', 'orange', 'yellow', 'green', 'blue']  # List of brick colors

# global variable
game_stated = False


class BreakoutGraphics:

    def __init__(self, ball_radius=BALL_RADIUS, paddle_width=PADDLE_WIDTH, paddle_height=PADDLE_HEIGHT,
                 paddle_offset=PADDLE_OFFSET, brick_rows=BRICK_ROWS, brick_cols=BRICK_COLS, brick_width=BRICK_WIDTH,
                 brick_height=BRICK_HEIGHT, brick_offset=BRICK_OFFSET, brick_spacing=BRICK_SPACING, title='Breakout'):

        # Create a graphical window, with some extra space
        self.window_width = brick_cols * (brick_width + brick_spacing) - brick_spacing
        self.window_height = brick_offset + 3 * (brick_rows * (brick_height + brick_spacing) - brick_spacing)
        self.window = GWindow(width=self.window_width, height=self.window_height, title=title)

        # Create a paddle
        self.paddle = GRect(paddle_width, paddle_height, x=(self.window_width-paddle_width)/2,
                       y=self.window_height-paddle_offset-paddle_height)
        self.paddle.filled = True
        self.window.add(self.paddle)

        # Center a filled ball in the graphical window
        self.ball = GOval(ball_radius*2, ball_radius*2, x=self.window_width/2-ball_radius,
                          y=self.window_height/2-ball_radius)
        self.ball.filled = True
        self.window.add(self.ball)
        self.b_r = BALL_RADIUS

        # Default initial velocity for the ball
        self.__dx = 0
        self.__dy = 0

        # Initialize our mouse listeners
        onmouseclicked(self.ball_move)
        onmousemoved(self.handle_paddle)

        # Draw bricks
        for i in range(brick_cols):
            for j in range(brick_rows):
                brick = GRect(brick_width, brick_height)
                brick.filled = True
                brick.fill_color = BRICK_COLORS[j // 2]
                brick.color = BRICK_COLORS[j // 2]
                self.window.add(brick, x=i*(brick_width+brick_spacing), y=j*(brick_height+brick_spacing))
        self.bricks_num = brick_cols*brick_rows


    def handle_paddle(self, event):
        if event.x <= self.paddle.width/2:
            self.paddle.x = 0
        elif event.x >= self.window.width-self.paddle.width/2:
            self.paddle.x = self.window.width-self.paddle.width
        else:
            self.paddle.x = event.x - self.paddle.width/2

    def ball_move(self, event):
        global game_stated
        if not game_stated:
            game_stated = True
            self.set_ball_velocity()

    def set_ball_velocity(self):
        self.__dy = INITIAL_Y_SPEED
        self.__dx = random.randint(1, MAX_X_SPEED)
        if random.random() > 0.5:
            self.__dx = -self.__dx

    def get_dx(self):
        return self.__dx

    def get_dy(self):
        return self.__dy

    def reflect_ball_x(self):
        self.__dx = -self.__dx

    def reflect_ball_y(self):
        self.__dy = -self.__dy

    def reset_ball(self):
        global game_stated
        self.ball.x = self.window_width/2-self.b_r
        self.ball.y = self.window_height/2-self.b_r
        self.__dx = 0
        self.__dy = 0
        game_stated = False
