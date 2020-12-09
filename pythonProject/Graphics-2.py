import turtle
t = turtle.Turtle()
# t.style = (Corbel)
t.pensize(4)

HEIGHT = 100
t.width = 40

def mov(x, y):
    t.up()
    t.setposition(0, 0)
    t.setheading(90)
    t.left(90)
    t.forward(x)
    t.right(90)


def letterM():
    t.goto(0, HEIGHT)
    t.goto(20, 0)
    t.goto(40, HEIGHT)
    t.goto(40, 0)


def A(size):
    t.right(16)
    t.forward(size)
    t.right(150)
    t.forward(size)
    t.backward(size / 2)
    t.right(105)
    t.forward(size / 3)


def B():
    t.forward(60)
    t.right(90)
    for i in range(18):
        t.right(9)
        t.forward(3)
        for i in range(18):
            t.right(13)
            t.backward(3)


def D():
    t.forward(60)
    t.right(90)
    t.forward(9)
    for i in range(13):
        t.right(13)
        t.forward(7)


def H():
    t.forward(60)
    t.backward(30)
    t.right(90)
    t.forward(30)
    t.left(90)
    t.forward(30)
    t.backward(60)


letterM()
t.setheading(10)
t.penup()
t.forward(20)
t.stamp()

mov(325, 400)
H()
mov(220, 400)
A()
mov(200, 400)
letterM()
mov(180, 400)
letterM()
mov(160, 400)
letterM()
mov(140, 400)
A()
mov(120, 400)
# 6;34

def letterD():
    t.goto(100, HEIGHT)
    t.goto(90, 0)
    t.goto(200, 0)


t.circle(100, 180)
t.left(90)
t.forward(200)
turtle.done()




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

