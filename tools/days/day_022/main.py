# Day 22
# Updated 2023, Jarid Prince

from days.day_022.files.helpers import *
from days.day_022.files.paddle import Paddle
from days.day_022.files.score import Score
from days.day_022.files.ball import Ball


def day_022():
    title("WONKY PONG")
    nls("A very bad implementation of Pong xD")
    # Initialise Screen
    screen = Screen()
    screen.bgcolor("black")
    screen.title("Pong")
    screen.setup(800, 600)
    rootwindow = screen.getcanvas().winfo_toplevel()
    rootwindow.call("wm", "attributes", ".", "-topmost", "1")
    rootwindow.call("wm", "attributes", ".", "-topmost", "0")
    screen.tracer(0)

    # Create Paddles, Ball and Score
    l_paddle = Paddle((-350, 0))
    r_paddle = Paddle((350, 0))
    ball = Ball()
    score = Score()

    # Listen to input on arrow keys and w, s
    screen.listen()
    screen.onkeypress(l_paddle.go_up, "w")
    screen.onkeypress(l_paddle.go_down, "s")
    screen.onkeypress(r_paddle.go_up, "Up")
    screen.onkeypress(r_paddle.go_down, "Down")

    # Start game
    gameon = True

    while gameon:
        # Set movement speed of ball, begin movement, prevent close
        time.sleep(ball.move_speed)
        screen.update()
        ball.move()

        # Handle bouncing
        if ball.ycor() > 280 or ball.ycor() < -280:
            ball.bounce("y")
        if (
            ball.distance(r_paddle) < 50
            and ball.xcor() > 320
            or ball.distance(l_paddle) < 50
            and ball.xcor() < 320
        ):
            ball.bounce("x")

        # Handle scoring/reset
        if ball.xcor() > 380:
            ball.reset_pos()
            score.point("left")
        if ball.xcor() < -380:
            ball.reset_pos()
            score.point("right")
