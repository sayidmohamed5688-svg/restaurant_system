import turtle

t = turtle.Turtle()
t.speed(3)

# Move to start position
t.penup()
t.goto(-200, 0)
t.pendown()

# Function to move without drawing
def move(x, y):
    t.penup()
    t.goto(x, y)
    t.pendown()

# ---------------- S ----------------
def draw_S():
    t.setheading(0)
    t.circle(20, 180)
    t.circle(-20, 180)

move(-200, 0)
draw_S()

# ---------------- A ----------------
move(-150, 0)
t.left(75)
t.forward(50)
t.right(150)
t.forward(50)
t.backward(25)
t.right(105)
t.forward(20)

# ---------------- Y ----------------
move(-90, 50)
t.setheading(-90)
t.forward(30)
t.backward(30)
t.left(45)
t.forward(30)
t.backward(30)
t.right(90)
t.forward(30)

# ---------------- I ----------------
move(-40, 0)
t.setheading(90)
t.forward(50)
t.backward(25)
t.right(90)
t.forward(10)
t.backward(20)

# ---------------- D ----------------
move(10, 0)
t.setheading(90)
t.forward(50)
t.right(90)
t.circle(-25, 180)

t.hideturtle()
turtle.done()