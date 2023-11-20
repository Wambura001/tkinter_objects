from tkinter import *

def action1():
  label.config(text="Student Information Selected")

def action2():
  label.config(text="Professor Information Selected")

def action3():
  label.config(text="Course Information Selected")

window = Tk()
window.title('Top-Down Menu with Buttons')
window.geometry('500x500')

#create menu widget
menu = Menu(window)

label = Label(window, text = 'Display Select an action').pack(pady = 10)

#create submenu for the menu
submenu = Menu(menu, tearoff=0)
submenu.add_command(label = 'Student Information', command = action1)
submenu.add_command(label = 'Professor Information', command = action2)
submenu.add_command(label = 'Course Information', command = action3)

#Add submenu to the menu
menu.add_cascade(label="Actions", menu=submenu)

#create buttons that open the menu
menu_button = Button(window, text = "Select Action", command=lambda: menu.post(0, 0)).pack()

#Attach the menu to the window
window.config(menu = menu)

window.mainloop()