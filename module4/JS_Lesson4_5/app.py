from tkinter import filedialog as fd
from tkinter import *
from tkinter.messagebox import askyesno
from zlib import DEF_BUF_SIZE
from zoneinfo import reset_tzpath
from file_worker import FileWorker


def open_file():
    return fd.askopenfile()


class Application:

    def ui(self):
        root = Tk()
        root.title("File_writer")
        text = Text(root)
        text.grid(row=0, column=0)
        button_save = Button(text="Open")
        button_open = Button(text="Save")
        button_open.grid(row=1, column=0)
        button_save.grid(row=2, column=0)
        return root


fw = FileWorker()


# продолжить написание чтения и записи в файл, после связать с кнопками и в прод)))
def read_file(file_path):
    if file_path:
        with open(file_path, 'r') as file:
            return file.readlines()
    return []


# this function writing in Tk.Text
def write_in_tk_text(text, string):
    text.insert(END, string)


def open_button(text, line_list, fill_path_var):
    file_path = fd.askopenfilename()
    if file_path:
        fill_path_var.set(file_path)
        line_list = read_file(file_path)
    for line in line_list:
        text.insert(END, line)



def save_changes(text, file_path):
    if file_path:
        if askyesno(title="Saving", message='Do you want to save changes?'):
            lines =text.get('1.0',END)
            with open(file_path,'w') as file:
                for line in lines:
                    file.write(line)
        print("save")
    else:
        print("Any file don't open")

def lesson_simple():
    BUTTON_WIDTH = 5
    root = Tk()
    root.title("File_writer")
    root.configure(bg='black')
    text = Text(root, wrap=WORD, bg="black", fg="white")
    text.grid(row=0, column=0)
    lines_list = []
    fill_path = StringVar()
    button_save = Button(text="Open", width=BUTTON_WIDTH, command=lambda: open_button(text, lines_list, fill_path))

    button_open = Button(text="Save", width=BUTTON_WIDTH,
                         command=lambda: save_changes(text, fill_path.get()))
    button_open.grid(row=1, column=0)
    button_save.grid(row=2, column=0)
    # lines = read_file(choice_file())

    # for line in lines:
    #
    #     text.insert(END, line)
    root.mainloop()


lesson_simple()
# нужно прописать "закрытие" файла чтобы если файл уже открыт и нажать еще раз открыть, то спрашиволось ли сохранить изменения и убирался текст с окна