import turtle
fred = turtle.Pen()
fred.speed(0)
fred.color("purple")
fred.width(5)
for i in range(100):
    fred.forward(i * 2)
    fred.circle(i * 2, 90)
    fred.right(20)

# then hit the enter key and watch the magic
# purple spiral
