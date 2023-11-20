from tkinter import *

window = Tk()
window.title("Radio Button")
window.geometry("300x300")

v = IntVar()
Radiobutton(window, text='Artificial intellgence', variable=v, value=1).pack(anchor=W)
Radiobutton(window, text='Smart computing', variable=v, value=1).pack(anchor=W)
Radiobutton(window, text='Business Administration', variable=v, value=1).pack(anchor=W)
Radiobutton(window, text='Hotel Management', variable=v, value=1).pack(anchor=W)
Radiobutton(window, text='Korean Studies', variable=v, value=1).pack(anchor=W)
Radiobutton(window, text='EAP', variable=v, value=1).pack(anchor=W)
Radiobutton(window, text='KAP', variable=v, value=1).pack(anchor=W)

window.mainloop()