import turtle
f = turtle.Pen()

f.speed(0)
f.color("green")
f.width(5)
for i in range(100):
    f.forward(i * 2)
    f.circle(i * 2, 90)
    f.right(20)
#this creates a rose.
