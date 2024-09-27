import turtle
import time
import random

sc = turtle.Screen()
sc.bgcolor("blue")
delay = 0.1
segments = []
score = 0
high_score = 0

snake = turtle.Turtle()
snake.shape("circle")
snake.color("green")
snake.penup()
snake.goto(0,100)
snake.direction = "stop"

def move():
    if snake.direction == "up":
        y = snake.ycor()
        snake.sety(y+20)

    if snake.direction == "down":
        y = snake.ycor()
        snake.sety(y-20)

    if snake.direction == "left":
        x = snake.xcor()
        snake.setx(x-20)

    if snake.direction == "right":
        x = snake.xcor()
        snake.setx(x+20)
def go_up():
    snake.direction = "up"

def go_down():
    snake.direction = "down"

def go_left():
    snake.direction = "left"

def go_right():
    snake.direction = "right"

sc.listen()
sc.onkey(go_up,"w")
sc.onkey(go_down,"s")
sc.onkey(go_left,"a")
sc.onkey(go_right,"d")

food = turtle.Turtle()
food.shape("circle")
food.pencolor("red")
food.penup()
food.goto(100,100)

while True:
    sc.update()
    move()
    time.sleep(delay)
    if snake.distance(food)<20:
        x = random.randint(-200,200)
        y = random.randint(-200,200)
        food.penup()
        food.goto(x,y)
        food.pendown()
       #
        segment = turtle.Turtle()
        segment.shape("circle")
        segment.pencolor("grey")
        segment.penup()
        segment.goto(200,200)
        segments.append(segment)

    for i in range(len(segments)-1,0,-1):
        x = segments[i-1].xcor()
        y = segments[i-1].ycor()
        segments[i].goto(x,y)
        
    if len(segments)>0:
        x = snake.xcor()
        y = snake.ycor()
        segments[0].goto(x,y)




        

sc.mainloop()