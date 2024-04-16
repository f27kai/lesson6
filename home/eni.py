import turtle

t = turtle.Turtle()
t.speed(3)


t.circle(100)

for _ in range(2):
    t.forward(100)
    t.left(90)
    t.forward(200)
    t.left(90)

turtle.done()