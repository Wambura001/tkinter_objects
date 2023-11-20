from tkinter import *

window = Tk()
window.title("Checkbutton")
window.geometry('500x300')

var1 = IntVar()
Checkbutton(window, text='male', variable=var1).grid(row=0, sticky=W)
var2 = IntVar()
Checkbutton(window, text='female', variable=var2).grid(row=1, sticky=W)

window.mainloop()