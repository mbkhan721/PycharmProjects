import turtle
t = turtle.Turtle()

HEIGHT = 100
WIDTH = 40

def letterM():
    t.goto(0, HEIGHT)
    t.goto(20, 0)
    t.goto(40, HEIGHT)
    t.goto(40, 0)


def letteri():
    t.setheading(90)
    t.forward(50)
    t.penup()
    t.forward(20)
    t.setheading(0)
    t.pendown()
    t.circle(5)
# to add space, pick up turtle, move
letterM()
t.setheading(10)
t.penup()
t.forward(20)
t.pendown()
letterM()
turtle.mainloop()
