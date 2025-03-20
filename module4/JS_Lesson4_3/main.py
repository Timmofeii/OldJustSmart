from cProfile import label
from tkinter.messagebox import *
from tkinter import *
from PIL import ImageTk
from PIL import Image
from tkinter.simpledialog import *


def first():
    root = Tk()

    text = Text(root, height=4, width=10, font="ubuntu 14", wrap=WORD,bd=5)
    text1 = Text(root, height=4, width=10, font="ubuntu 14", wrap=WORD, bd=5)
    text.pack(side=TOP)
    text1.pack(side=BOTTOM)
    text.insert("1.0", "Add this text \n in start first row")
    # text.delete("1.0",END)
    message = text.get("1.0", END) + " from root"
    text1.insert("1.0", message)
    root.mainloop()

first()
def full_listbox(list_box, list):
    for i in list:
        list_box.insert(END, i)


def second():
    root = Tk()
    list_box = Listbox(root, text="number", height=3, width=15, selectmode=EXTENDED, selectbackground="green")
    list_box2 = Listbox(root, height=5, width=15, selectmode=SINGLE, selectbackground="green")

    list1 = [1, 2, 3, 4]
    list2 = ["one", "two", 'three', 'four']
    full_listbox(list_box, list1)
    full_listbox(list_box2, list2)
    list_box.pack()
    list_box2.pack()
    root.mainloop()


def third():
    root = Tk()
    frame = Frame(root, bg="green", bd=5)
    frame1 = Frame(root, bg="red", bd=5)
    button = Button(frame, text="Button")
    button1 = Button(frame1, text="Button 1")
    frame.pack()
    frame1.pack()
    button.pack()
    button1.pack()
    root.mainloop()


# third()

def show_selection(var):
    print(f"Selected option: {var.get()}")

def checkButton():
    root = Tk()
    # my_png= tkinter.PhotoImage(file="C:\\done.png")
    # resized_image= my_png.resize((50, 50), Image.ANTIALIAS)
    # my_png= ImageTk.PhotoImage(resized_image)
    # root.geometry("200x200")
    var = StringVar(value="Option 1")

    check = Checkbutton(root, text="1 choice", variable=var, onvalue=1, offvalue=0)
    check1 = Checkbutton(root, text="Choice 2", variable=var, onvalue=0, offvalue=1)
    radiobutton= Radiobutton(root, text="Option 3", variable=var, value="Option 3", command=lambda :show_selection(var))#image=my_png,
    radiobutton.pack(anchor=W)
    check.pack(anchor=W)
    check1.pack(anchor=W)
    root.mainloop()



def toggle_continue(check_var,button):
    if check_var.get() == 1:
        button.config(state=NORMAL)
    else:
        button.config(state=DISABLED)

def simple_using_ckeck_buttom():
    root = Tk()

    check_var = IntVar()

    check_button = Checkbutton(root, text="I agree to the terms and conditions", variable=check_var, command=lambda :toggle_continue(check_var,continue_button))
    check_button.pack(pady=10)

    continue_button = Button(root, text="Continue", state=DISABLED)
    continue_button.pack(pady=10)
    root.mainloop()
# simple_using_ckeck_buttom()



def setMessage(entry,label):
    if(askyesno(title="Get",message="Transfer data?")):
        label['text']=entry.get()
        entry.delete(0,END)
def messagebox():# check function
    root = Tk()
    root.title("MessageBox")
    root.geometry("200x300")
    entry = Entry(root)
    label = Label(root)
    button = Button(root,text="Rewrite",command= lambda :setMessage(entry,label))
    entry.pack()
    label.pack()
    button.pack()
    root.mainloop()
# messagebox()
# this function printed text by 1 character at a time
def update_text(root,text,label):
    global index
    if index<len(text):
        label.config(text=label.cget('text')+text[index])
        index +=1
        root.after(100,update_text,root,text,label)

def askSimple():
    root = Tk()
    root.geometry("200x200")
    root.configure(bg="black")

    name = askstring("Enter inf","Enter your name:",parent=root)
    if (1!=None):
        print(f"Your name {name}." )
    else:
        print("Please enter your name!")
    age = askinteger("Enter inf"," Enter your age",parent=root,minvalue=0,maxvalue=125,)
    if (age!=None):
        print(f"Your age in years {age}.")
    else:
        print("Not found information about age")
    weight = askfloat("Enter inf","Enter your weight", parent=root, minvalue=0.0,maxvalue=200.0)
    if (weight!=None):
        print(f"Your weight is {weight}.")
    else:
        print("Not found information about weight")
    label = Label(root,text=f"",font=('Helvetica',16),bg='black',fg="#00FF00")
    label.pack(pady=20)
    text_inf= f"Your age in years {age}.\nYour weight is {weight}.\nYour name {name}."

    update_text(root,text_inf,label)
    root.mainloop()
index = 0
# askSimple()

def canvasSimple():
    root = Tk()
    root.geometry("300x200")
    root.title("CanvasSimple")
    canvas= Canvas(root,bg="white",width=250,height=200)
    photo_path = "done.png"
    try:
        image = Image.open(photo_path)
        my_png = ImageTk.PhotoImage(image)

        # Add the image to the canvas
        canvas.create_image(90, 90, anchor=tk.CENTER, image=my_png)
    except Exception as e:
        print("Error loading image:",e)
    canvas.pack(fill='both',expand=True)
    canvas.create_line(1,1,299,299)
    canvas.create_rectangle(50,50,100,100,fill="red")
    canvas.create_oval(150,150,300,300,fill="yellow")
    canvas.create_text(300,300, text= "Hello Canvas")
    points = [50, 150, 100, 50, 150, 150]

    # Creating the polygon
    canvas.create_polygon(points, outline='black', fill='blue', width=2)
    canvas.create_arc(200,200,500,500,width=2,fill="pink")

    root.mainloop()
canvasSimple()