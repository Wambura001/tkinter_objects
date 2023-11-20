from tkinter import *

window = Tk()
window.title('Canvas')
window.geometry('300x300')

canvas = Canvas(window, width=50, height=100)
canvas.pack()

canvas_height=20
canvas_width=200

y = int(canvas_height / 2)
canvas.create_line(0, y, canvas_width, y)

window.mainloop()