import tkinter as tk
from cProfile import label
from glob import escape
from tkinter import BOTH, Frame, Label, Button
import re

class RoundButton(tk.Canvas):
    def __init__(self, parent, text, command=None, width=100, height=100, bg="white", fg="black"):
        tk.Canvas.__init__(self, parent, width=width, height=height, bg=bg, highlightthickness=0)
        self.command = command

        self.create_oval(5, 5, width, height, outline=fg, fill=bg)
        self.create_text(width // 2, height // 2, text=text, fill=fg, font=("Helvetica", 18, "bold"))

        self.bind("<ButtonPress-1>", self._on_press)
        self.bind("<ButtonRelease-1>", self._on_release)

    def _on_press(self, event):
        self.configure(relief="sunken")

    def _on_release(self, event):
        self.configure(relief="raised")
        if self.command:
            self.command()


def on_click():
    print("Button clicked!")


# root = tk.Tk()
# root.title("Round Button Example")
# root.geometry("400x400")
#
# frame = tk.Frame(root, bg="black")
# frame.pack(fill=tk.BOTH, expand=True)
#
# # Пример кнопки
# round_button = RoundButton(frame, text="5", command=on_click, width=100, height=100, bg="#333333", fg="white")
# round_button.place(x=150, y=150)
#
# root.mainloop()

operations = ['+', '-', '*', '/']


def set_value_in_display(label, value):
    current_text = label.cget("text")
    if is_valid(current_text, value):
        new_text = f"{current_text}{value}"
        label.configure(text=new_text)


def is_valid(text, value):
    if len(text) == 0 and value in operations:
        return False
    elif len(text) > 0 and text[-1] in operations and value in operations:
        return False
    else:
        return True


def parser(text):
    list_math_operation = list()
    if len(text) > 0:
        part = ''
        for item in text:
            if item not in operations:
                part += item
            else:
                list_math_operation.append(int(part))
                list_math_operation.append(item)
                part = ''

        list_math_operation.append(int(part))
        return list_math_operation
    return math_list


def result_math_operation(label):
    text = label.cget("text")
    list_math_operation = list()
    try:
        list_math_operation = parser(text)
        result = list_math_operation[0]
        i = 1
        while i < len(list_math_operation):
            if list_math_operation[i] == "+":
                result += list_math_operation[i + 1]
            elif list_math_operation[i] == '-':
                result -= list_math_operation[i + 1]
            elif list_math_operation[i] == '*':
                result *= list_math_operation[i + 1]
            elif list_math_operation[i] == '/':
                if list_math_operation[i + 1] != 0:
                    result /= list_math_operation[i + 1]
                else:
                    clear_display(label)
                    set_value_in_display(label, "ZeroDivisionError")
                    return
            i += 2

        print(result)
        label.configure(text=str(result))

    except ValueError:
        clear_display(label)
        set_value_in_display(label,"Value error")


def clear_display(display):
    display.configure(text='')



def set_ui(root):
    color_interface = "black"
    frame = Frame(root, bg=color_interface)
    frame.pack(fill=BOTH, expand=1)
    color_button = "#333333"
    color_text= "white"
    digit_color = "#333333"  # Темно-серый
    operation_color = "#FF9500" # Оранжевый
    function_color = "#A5A5A5" # Светло-серый
    display_label = Label(frame, text='', bg=color_button,fg=color_text)
    display_label.grid(row=0, column=0, columnspan=4, sticky='nsew')
    list_key = [1, 2, 3, 4, 5, 6, 7, 8, 9, 0]
    rows = 4
    columns = 3
    list_button = []
    i = 0
    size_button = 3

    for row in range(1, rows, 1):
        for column in range(0, columns, 1):
            key_button = Button(frame, text=list_key[i], width=size_button, bg=color_button,fg=color_text,
                                command=lambda value=list_key[i]: set_value_in_display(display_label, value))
            #используем лямбу и создаем переменную для записи конктретного елемента со списка
            key_button.grid(row=row, column=column, sticky="nsew")
            list_button.append(key_button)
            i += 1
    key_button_zero = Button(frame, text=0, bg=color_button,fg=color_text, width=size_button,
                             command=lambda: set_value_in_display(display_label, 0))
    key_button_zero.grid(row=rows, column=1, sticky='nsew')

    # Добавляем кнопки операций

    for j, op in enumerate(operations):
        key_button_op = Button(frame, text=op, bg=operation_color,fg=color_text, width=size_button,
                               command=lambda value=op: set_value_in_display(display_label, value))
        key_button_op.grid(row=rows + 1 + j // 2, column=j % 2, sticky='nsew')

    key_button_clear = Button(frame, text="clear", bg=function_color,fg=color_text, command=lambda: clear_display(display_label))
    key_button_clear.grid(row=rows + 1, column=2, rowspan=2, sticky='nsew')

    key_button_equals = Button(frame, text="=", bg=color_button,fg=color_text, command=lambda: result_math_operation(display_label))
    key_button_equals.grid(row=rows + 3, column=0, columnspan=4, sticky='nsew')


root = tk.Tk()
root.geometry('300x200')
set_ui(root)
root.mainloop()

