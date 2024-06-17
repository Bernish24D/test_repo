import turtle as t

# Setup the screen
ground = t.Screen()
ground.bgpic("ground.png")
ground.addshape("p2.gif")
ground.addshape("p1.gif")
ground.addshape("ball.gif")

# Setup player 1
p1 = t.Turtle()
p1.penup()
p1.shape("p1.gif")
p1.goto(400, -200)

# Setup player 2
p2 = t.Turtle()
p2.penup()
p2.shape("p2.gif")
p2.goto(-400, 200)

# Setup score display for player 1
p1pen = t.Turtle()
p1pen.penup()
p1pen.hideturtle()
p1pen.goto(100, 250)
p1pen.color("white")
p1pen.write("p1 Score : 0", font=("Courier", 27, "bold"))

# Setup score display for player 2
p2pen = t.Turtle()
p2pen.penup()
p2pen.hideturtle()
p2pen.goto(-400, 250)
p2pen.color("white")
p2pen.write("p2 Score : 0", font=("Courier", 27, "bold"))

# Setup the ball
ball = t.Turtle()
ball.penup()
ball.shape("ball.gif")
ball.speed(200)

# Functions to move player 2
def p2up():
    y = p2.ycor()
    p2.sety(y + 7)

def p2down():
    y = p2.ycor()
    p2.sety(y - 7)

def p2right():
    x = p2.xcor()
    p2.setx(x + 7)

def p2left():
    x = p2.xcor()
    p2.setx(x - 7)

t.onkeypress(p2up, "w")
t.onkeypress(p2down, "s")
t.onkeypress(p2right, "d")
t.onkeypress(p2left, "a")

# Functions to move player 1
def p1up():
    y = p1.ycor()
    p1.sety(y + 7)

def p1down():
    y = p1.ycor()
    p1.sety(y - 7)

def p1right():
    x = p1.xcor()
    p1.setx(x + 7)

def p1left():
    x = p1.xcor()
    p1.setx(x - 7)

t.onkeypress(p1up, "u")
t.onkeypress(p1down, "j")
t.onkeypress(p1right, "k")
t.onkeypress(p1left, "h")

# Ball movement direction control
ball_dx = 2
ball_dy = 2
p2score = 0
p1score = 0

t.listen()

while True:
    x = ball.xcor()
    y = ball.ycor()
    ball.setpos(x + ball_dx, y + ball_dy)

    if p2.distance(ball) < 50:  # Check if player 2 is near the ball
        # Adjust ball direction to move away from player 2
        if ball.xcor() > p2.xcor():
            ball_dx = abs(ball_dx)  # Move right
        else:
            ball_dx = -abs(ball_dx)  # Move left
        if ball.ycor() > p2.ycor():
            ball_dy = abs(ball_dy)  # Move up
        else:
            ball_dy = -abs(ball_dy)  # Move down

    if p1.distance(ball) < 50:  # Check if player 1 is near the ball
        # Adjust ball direction to move away from player 1
        if ball.xcor() > p1.xcor():
            ball_dx = abs(ball_dx)  # Move right
        else:
            ball_dx = -abs(ball_dx)  # Move left
        if ball.ycor() > p1.ycor():
            ball_dy = abs(ball_dy)  # Move up
        else:
            ball_dy = -abs(ball_dy)  # Move down

    if ball.ycor() < -280:
        ball_dy = abs(ball_dy)

    if ball.ycor() > 280:
        ball_dy = -abs(ball_dy)

    if ball.xcor() < -450:
        ball.goto(0, 0)
        p1pen.clear()
        p1score += 1
        p1pen.write(f"p1 Score : {p1score}", font=("Courier", 27, "bold"))

    if ball.xcor() > 450:
        ball.goto(0, 0)
        p2pen.clear()
        p2score += 1
        p2pen.write(f"p2 Score : {p2score}", font=("Courier", 27, "bold"))
