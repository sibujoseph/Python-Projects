import time
from tkinter import *

animation = Tk()
canvas = Canvas(animation, width=800, height=600)
canvas.pack()
canvas.create_polygon(10, 10, 10, 10, 60, 50, 60, 35)

for x in range(0, 140):
    canvas.move(1, 5, 0)
    animation.update()
    time.sleep(0.05)
