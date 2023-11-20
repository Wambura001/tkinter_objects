from tkinter import *

ml = PanedWindow()
ml.pack(fill = BOTH, expand=1)

left = Entry(ml, bd=5)
ml.add(left)
m2 = PanedWindow(ml, orient = VERTICAL)
ml.add(m2)
top = Scale(m2, orient=HORIZONTAL)
m2.add(top)

mainloop()

