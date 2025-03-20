import tkinter
from tkinter import *
from warnings import catch_warnings


def addElement(listBoxFrom,listBoxTo):
    try:
        product =listBoxFrom.get(listBoxFrom.curselection())
        listBoxTo.insert(END,product)
    except tkinter.TclError:
        print("No item selected")
def removeElement(listBox):
    try:
        listBox.delete(listBox.curselection())
    except tkinter.TclError:
        print("Not item selected to remove")
def transferElement(listBoxFrom,listBoxTo):
    addElement(listBoxFrom, listBoxTo)
    removeElement(listBoxFrom)

def shop_market(listItems):
    root = Tk()
    root.title("ShopList")
    root.geometry("400x300")
    frame = Frame(root)
    frame1 = Frame(root)
    market = Listbox(frame)

    for product in listItems:
     market.insert(END,product)
    basket = Listbox(frame1)
    buttonFrame = Frame(root)
    buttonAdd = Button(buttonFrame, text=">>>", compound="center",command=lambda: transferElement(market,basket))
    buttonReturn = Button(buttonFrame, text="<<<", compound="center",command= lambda :transferElement(basket,market))
    frame.grid(row=0, column=0)
    buttonFrame.grid(row=0, column=1)
    frame1.grid(row=0, column=2)
    market.grid()
    basket.grid()
    buttonAdd.grid(row=0, column=0)
    buttonReturn.grid(row=1, column=0)

    root.mainloop()
# shop_market(["Potato","tomato",'corn'])

def practicCanvas():
    root = Tk()
    root.title("Simple Oval")
    canvas = Canvas(root, width=400, height=400, bg="white")
    canvas.create_oval(50,50,250,150)
    canvas.create_oval(170,170,250,250,outline="green",width=10,activeoutline="green",fill="lime green")
    canvas.pack()
    root.mainloop()


def canvas():
    root = Tk()
    my_canvas = Canvas(root,width=400,height=400,bg="black")
    my_canvas1''.pack()
    my_canvas.create_oval(100,100,300,300,outline="black",width=1,fill="white")
    my_canvas.create_arc(100,100,300,300,start=180,extent=90,outline="black",width=1,fill="#2A6EBB")
    # canvas.create_arc(100, 100, 300, 300, start=180, extent=270, outline="black", width=1, fill="#2A6EBB")
    root.mainloop()
canvas()



