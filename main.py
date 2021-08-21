from turtle import Screen
from snake import Snake
from scoreboard import Scoreboard
import time
from food import Food

score_points = 0
screen = Screen()

screen.bgcolor("black")
screen.setup(600, 600)

screen.tracer(0)


snake = Snake()
food = Food()
score = Scoreboard()
screen.listen()


screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")
game_on = True
while game_on:
    screen.update()
    time.sleep(0.1)
    snake.move()

    if snake.head.distance(food) < 15:
        food.refresh()
        score_points += 1
        score.keepscore(score_points)
        snake.extend()

    if snake.head.xcor() > 290 or snake.head.xcor() < -290 or snake.head.ycor() > 290 or snake.head.ycor() < -290:
        game_on = False
        score.game_over()


    for segment in snake.segments[1:]:
        if snake.head.distance(segment) < 10:
            game_on=False
            score.game_over()

screen.exitonclick()








screen.exitonclick()