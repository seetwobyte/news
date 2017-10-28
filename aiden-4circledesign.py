
import turtle
fred = turtle.Pen()
fred.color("black")
fred.speed(0)
fred.width(4)

for i in range(100):
        fred.circle(i * 3)
        fred.left(10)

# then hit the enter Key and watch the magic
