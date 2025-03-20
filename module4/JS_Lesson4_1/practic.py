# importing only those functions which 
# are needed 
from tkinter import *

# creating tkinter window 
win = Tk()
win.title("Marshal")
txt= ["I'm Slim Shady, yes I'm the real Shady","All you other Slim Shadys are just imitating","So won't the real Slim Shady please stand up"]
for i in txt:
    label = Label(win, text=i, bg="yellow", fg="blue")
    label.pack()
    label.configure(font=("Arial", 12))







enty = Entry()
enty.pack(pady=10)
button_destroy = Button(text="Destroy", command=win.destroy,bg= "red", fg="white")
button_destroy.pack()
# Execute Tkinter 
win.mainloop()
