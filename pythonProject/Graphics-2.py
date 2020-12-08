import turtle
t = turtle.Turtle()
style = ("Calibri")

HEIGHT = 100
WIDTH = 40

def letterM():
    t.goto(0, HEIGHT)
    t.goto(20, 0)
    t.goto(40, HEIGHT)
    t.goto(40, 0)

letterM()
t.setheading(10)
t.penup()
t.forward(20)
t.stamp()

def letterD():
    t.goto(100, HEIGHT)
    t.goto(90, 0)
    t.goto(200, 0)


t.circle(100, 180)
t.left(90)
t.forward(200)
turtle.done()



"""
# This is D
turtle.circle(100, 180) #180 degrees of a circle radius 100
turtle.left(90)
turtle.forward(200)
turtle.done()



# This is B
turtle.pendown()
turtle.forward(25)
turtle.circle(26,180)
turtle.forward(25)
turtle.setheading(0)
turtle.forward(25)
turtle.circle(22,180)
turtle.forward(26)
turtle.setheading(270)
turtle.forward(95)
turtle.setheading(32)
turtle.penup()
turtle.forward(160)
turtle.mainloop()
"""
