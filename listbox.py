from tkinter import *

window = Tk()
window.title('Listbox')
window.geometry('200x200')

Lb = Listbox(window)
Lb.insert(1, 'Pyhon')
Lb.insert(2, 'Java')
Lb.insert(3, 'PostGre')
Lb.insert(4, 'C++')
Lb.pack()

window.mainloop()