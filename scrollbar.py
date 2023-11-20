from tkinter import *

window = Tk()
window.title(Scrollbar)

scrollbar = Scrollbar(window)
scrollbar.pack(side = RIGHT, fill = Y)
mylist = Listbox(window, yscrollcommand = scrollbar.set)
for line in range(100):
  mylist.insert(END, 'Smart Computing' + str(line))
mylist.pack( side = LEFT, fill = BOTH)
scrollbar.config(command = mylist.yview)

window.mainloop()