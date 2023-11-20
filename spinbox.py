from tkinter import *

window = Tk()
window.title('Spinbox')

w = Spinbox(window, from_=0, to = 10)
w.pack()

window.mainloop()