from tkinter import *

window = Tk()

label = Label(text="Заголовок")
button1 = Button(text="Button1")
button2 = Button(text="Button2")
entry = Entry()
label.pack()

button1.configure(bg="#000", fg="#ff0")
button1.pack()
button2.pack()

label.configure(text="New Txt", font=("Arial", 25))
label.pack()
entry.pack()
window.title("Hello World!")
window.mainloop()
