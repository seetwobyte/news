from Tkinter import *
import random
import time

WIDTH = 800
HEIGHT = 600

tk = TK()
canvas = Canvas(tk, width=WIDTH, height=HEIGHT)
tk.title("Drawing")
canvas.pack()

ball = canvas.create_ocal(10, 10, 60, fill="orange")
xspeed = 5
yspeed = 5

while True:
    canvas.move(ball, xspeed, yspeed)
    pos = canvas.coords(ball)
    if pos[3] >= HEIGHT or pos[1] <= 0:
        yspeed = -yspeed
    if pos[2] >= WIDTH or pos[0] <= 0:
        xspeed = -xspeed
    tk.update()
    time.sleep(0.01)

tk.mainloop()
