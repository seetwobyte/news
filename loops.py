import turtle
fred = turtle.Pen()
fred.speed(0)
fred.width(5)
fred.color("green")
for i in range(100):
    fred.forward(i*2)
    fred.circle(i*2, 90)
    fred.right(20)
# please add more files
