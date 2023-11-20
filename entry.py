from tkinter import *

window = Tk()
window.title('Entry')
window.geometry('499x200')

Label(window, text = "First Name").grid(row = 0)
Label(window, text = "Last Name").grid(row = 1)

firstName = Entry(window).grid(row=0, column=1)
lastName = Entry(window).grid(row=1, column=1)

window.mainloop()