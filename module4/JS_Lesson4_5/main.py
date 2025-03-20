from tkinter import *
from tkinter import filedialog as fd


def insertText():
    file_name = fd.askopenfilename()
    f = open(file_name)
    text.insert(1.0, f.read())
    f.close()
def extractText():
    file_name = fd.asksaveasfilename()
    f = open(file_name, 'w')
    f.write(text.get(1.0, END))
    f.close()
def file_editor():
    root = Tk()
    text = Text(width = 25, height = 8)
    text.pack()
    Button(root, text = "Відкрити", command = insertText).pack()
    Button(root, text = "Зберегти", command = extractText).pack()
    root.mainloop()