import tkinter as tk

window = tk.Tk()
window.title('myButton')
window.geometry('300x200')

button = tk.Button(window, text='Hit me baby!', width=25, command=window.destroy)

button.pack()
window.mainloop()