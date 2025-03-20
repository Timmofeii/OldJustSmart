import tkinter as tk
from tkinter import Label
from zipfile import sizeCentralDir
from random import choice

text_label = "Sum_nambers"


def sum(entry1, entry2):
    return int(entry1.get()) + int(entry2.get())


def set_value(label, entry1, entry2):
    label.configure(text=f"{text_label}: {sum(entry1, entry2)}")


def simple_one():
    label = Label(text="Result: ")
    label.grid()
    win = tk.Tk()
    win.title("Grid")
    win.geometry("250x200")
    entry1 = tk.Entry()
    entry1.grid(row=0, column=0)
    entry2 = tk.Entry()
    entry2.grid(row=0, column=1)
    button = tk.Button(text="result", activebackground="green", compound="center")
    button.grid(row=1, column=0, columnspan=2)
    win.mainloop()





def compas():
    window = tk.Tk()
    window.title("Compass Layout")
    window.geometry("400x400")
    west = tk.Label(window, text="West")
    west.pack(side=tk.LEFT, anchor="w")
    north = tk.Label(window, text="North")
    north.pack(side=tk.TOP, anchor="n")
    east = tk.Label(window, text="East")
    east.pack(side=tk.RIGHT, anchor="e")
    south = tk.Label(window, text="South")
    south.pack(side=tk.BOTTOM, anchor="s")
    list_side= [west,north,east,south]
    button = tk.Button(window, text="Choice way", compound='center',command=lambda :random_side(list_side))

    button.pack(expand=True)# почитаты

    window.mainloop()
def all_one_color(list, color):
  for label in list:
    change_color(label,color)
def random_obj(list):
  return choice(list)

def change_color(label,color):
   label['fg'] = color

def random_side(list):
  all_one_color(list, "white")
  label = random_obj(list)
  change_color(label, "red")

compas()
def practic_one():
  root = tk.Tk()
  root.title("Color")
  root.geometry("200x200")
  label = tk.Label(root, text = "Sum number" , fg = "blue")
  label.grid(row=0,column=0)
  entry = tk.Entry(root)
  entry.grid(row=1,column=0)
  entry2 = tk.Entry()
  entry2.grid()
  button = tk.Button(root, text = "=")
  button.grid(row=2,column=0)
  root.mainloop()
# practic_one()
