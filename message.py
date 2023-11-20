from tkinter import *

window = Tk()
window.title("message")
window.geometry("300x300")

ourMessage = 'I am Wambura The Great'
messageVar = Message(window, text = ourMessage)
messageVar.config(bg='lightgreen')
messageVar.pack()

window.mainloop()
