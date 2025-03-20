from tkinter import *

def f(button):
    button["bg"] = "#C9A0DC"

def f1(event, button):
    button["bg"] = "#C9A0DC"

def simple_one(root):
    button = Button(root, text="Change Color", bg="white", command=lambda: f(button))
    button.place(x=0, y=0)  # задали позицію кнопці
    button.bind("<Button-3>", lambda event: f1(event, button))  # right mouse button
    button.pack()

root = Tk()  # створили об'єкт Тк
root.title("Color")  # Дали назву вікна
root.geometry("250x200")  # задали розміри вікна
root.configure(bg="black")  # Встановили йому колір

simple_one(root)
root.mainloop()


#simple 6
root.title("examples of indentations")
btn1= Button(text="Bottom")
btn1.pack(side=BOTTOM,expand=True,ipadx=10,ipady=10)

btn2 = Button(text="Right")
btn2.pack(side=RIGHT)


# simple position button 7
# btn1 = Button(text="Click me")
# btn1.place(relx=0.5,rely=0.5,anchor="c",width=80,height=40)
#
# btn2 = Button(text="Click me 2")
# btn2.place(x=20, y=30)


# for c in range(3): root.columnconfigure(index=c, weight=1)
# for r in range(3): root.rowconfigure(index=r, weight=1)
# for r in range(3):
#     for c in range(3):
#         btn = Button(text=f"({r},{c})")
#         btn.grid(row=r,column=c,ipadx=6,ipady=6,padx=4,pady=4,sticky=NSEW)

root.mainloop()
