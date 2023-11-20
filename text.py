from tkinter import *

window = Tk()
window.title("text")

T = Text(window, height = 5, width = 30)
T.pack()

T.insert(END, "This is \nWambura \nThe Great")
window.mainloop()