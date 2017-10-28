import turtle
import random
fred = turtle.Pen()

fred.shape("turtle")
fred.width(3)
fred.speed(1)

def square(size):
	for i in range(4):
		fred.forward(size)
		fred.left(90)

for i in range(100):
	x = random.randrange(-200, 200)
	y = random.randrange(-200, 200)
	fred.up()
fred.goto(x, y)
fred.down()
size = random.randrange(10, 200)
square(size)
