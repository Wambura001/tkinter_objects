from tkinter import *

window = Tk()
window.title('Frame')
# window.geometry('100x100')

frame = Frame(window)
frame.pack()

buttonframe = Frame(window).pack(side=TOP)
# buttonframe.pack(side = BOTTOM)

saveButton = Button(frame, text = 'Save', fg = 'red', bg = "DarkBlue").pack(side = LEFT)
editButton = Button(frame, text="Edit", fg = "brown").pack(side = LEFT)
deleteButton = Button(frame, text="Delete", fg = "blue").pack(side = LEFT)
closeButton = Button(frame, text="Close", fg = "black").pack(side = BOTTOM)

window.mainloop()