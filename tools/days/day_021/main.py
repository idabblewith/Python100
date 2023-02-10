# Day 21
# Updated 2023, Jarid Prince

from days.day_021.files.helpers import *
from days.day_021.files.food import Food
from days.day_021.files.score import Score
from days.day_021.files.snake import Snake


def day_021():
    title("SNAKE GAME P2")
    # Creates Window
    screen = Screen()
    screen.setup(800, 800)
    screen.bgcolor("black")
    screen.colormode(255)
    screen.title("Snake Game")
    rootwindow = screen.getcanvas().winfo_toplevel()
    rootwindow.call("wm", "attributes", ".", "-topmost", "1")
    rootwindow.call("wm", "attributes", ".", "-topmost", "0")
    screen.tracer(0)
    # Instatiates Classes
    snake = Snake()
    food = Food()
    score = Score()
    # Listens to keypresses
    screen.listen()
    screen.onkey(snake.up, "w")
    screen.onkey(snake.left, "a")
    screen.onkey(snake.down, "s")
    screen.onkey(snake.right, "d")
    # Starts game
    gameon = True
    while gameon:
        screen.update()
        # Prevents window from auto closing
        time.sleep(0.1)
        snake.move()

        # Handles eating
        if snake.head.distance(food) < 15:
            print("nom nom nom")
            food.refresh()
            snake.extend()
            score.updatescore()

        # Keeps game going while within coordinates/game over if out
        if (
            snake.head.xcor() > 380
            or snake.head.xcor() < -380
            or snake.head.ycor() > 380
            or snake.head.ycor() < -380
        ):
            gameon = False

        # Ends game if collided with segment/distance too close
        for segment in snake.snake_seg[1:]:
            if snake.head.distance(segment) < 10:
                gameon = False

    # Runs game over logic
    if gameon == False:
        score.game_over()
    # Clean up
    screen.clear()
    screen.bye()
