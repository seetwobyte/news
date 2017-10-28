# nice design
import turtle
fred = turtle.Pen()
fred.color("red")
fred.width(3)
fred.speed(1)
for i in range(20):
    fred.circle(i * 3, 180)
    fred.right(45)
    
