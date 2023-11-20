from tkinter import *

window = Tk()

w = Scale(window, from_=0, to=42).pack()
w = Scale(window, from_=0, to=200, orient = HORIZONTAL).pack()

window.mainloop()