import turtle
t = turtle.Turtle()
t.width(2)
t.pencolor("lightBlue")
t.pensize(6)


HEIGHT = 50 # Letter D wont adjust to the height as i commented out the first one
WIDTH = 40


def letterM():
    t.goto(0, HEIGHT)
    t.goto(20, 0)
    t.goto(40, HEIGHT)
    t.goto(40, 0)


def letterU():
    t.goto(50, HEIGHT)
    t.goto(50, 0)
    t.goto(90, 0)
    t.goto(90, HEIGHT)


def letterH():
    t.goto(100, 0)
    t.goto(100, HEIGHT / 2)
    t.goto(140, HEIGHT / 2)
    t.goto(140, HEIGHT)
    t.goto(140, 0)


def letterA():
    t.goto(150, HEIGHT)
    t.goto(190, HEIGHT)
    t.goto(190, HEIGHT / 2)
    t.goto(150, HEIGHT / 2)
    t.goto(190, HEIGHT / 2)
    t.goto(190, 0)


def letterM2():
    t.goto(200, HEIGHT)
    t.goto(220, 0)
    t.goto(240, HEIGHT)
    t.goto(240, 0)


def letterM3():
    t.goto(250, HEIGHT)
    t.goto(270, 0)
    t.goto(290, HEIGHT)
    t.goto(290, 0)


def letterA2():
    t.goto(300, HEIGHT)
    t.goto(340, HEIGHT)
    t.goto(340, HEIGHT / 2)
    t.goto(300, HEIGHT / 2)
    t.goto(340, HEIGHT / 2)
    t.goto(340, 0)

"""
def letterD():
    t.goto(350, HEIGHT)
    t.goto(390, HEIGHT)
    t.goto(390, 0)
    t.goto(350, 0)
    t.goto(390, 0)
"""

letterM()
t.setheading(0)
t.penup()
t.forward(10)
t.pendown()


letterU()
t.setheading(0)
t.penup()
t.forward(10)
t.pendown()


letterH()
t.setheading(0)
t.pendown()
t.penup()
t.forward(10)
t.pendown()


letterA()
t.setheading(0)
t.penup()
t.forward(10)
t.pendown()


letterM2()
t.setheading(0)
t.penup()
t.forward(10)
t.pendown()


letterM3()
t.setheading(0)
t.penup()
t.forward(10)
t.pendown()


letterA2()
t.setheading(0)
t.penup()
t.forward(10)
t.pendown()

# First method of letter D
"""
letterD()
t.circle(WIDTH, HEIGHT)
t.left(90)
t.penup()
t.forward(30)
t.pendown()
"""
# I used two methods for letter D

# Genuine looking letter D
t.circle(26, 180)
t.left(90)
t.forward(52)
t.penup()
t.left(90)
t.forward(60)

# Letter B
t.pendown()
t.forward(25)
t.circle(13,180)
t.forward(25)
t.setheading(0)
t.forward(26)
t.circle(13,180)
t.forward(26)
t.setheading(270)
t.forward(52)
t.setheading(32)
t.penup()
t.forward(60)


turtle.done()
# turtle.mainloop()
