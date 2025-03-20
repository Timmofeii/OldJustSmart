from tkinter import *


class Paint(Frame):
    def __init__(self, parent):
        Frame.__init__(self, parent)
        self.parent = parent
        self.color = "black"
        self.brush_size = 3
        self.setUI()

    def set_brush_size(self, brush_size):
        self.brush_size = brush_size

    def set_color(self, color):
        self.color = color

    def draw(self, event):
        self.canv.create_oval(event.x - self.brush_size,
                              event.y - self.brush_size,
                              event.x + self.brush_size,
                              event.y + self.brush_size,
                              fill=self.color, outline=self.color)

    def create_buttons(self, row, items, command_func):
        buttons = []
        for index, item in enumerate(items):
            button = Button(self, text=item, width=10, command=lambda item=item: command_func(item))
            button.grid(row=row, column=index + 1, sticky=E + W)
            buttons.append(button)
            self.grid_columnconfigure(index + 1, weight=1)
        return buttons

    def setUI(self):
        self.parent.title("Paint")
        self.pack(fill=BOTH, expand=1)
        self.columnconfigure(6, weight=1)
        self.rowconfigure(2, weight=1)
        self.canv = Canvas(self, bg="white")
        self.canv.grid(row=2, column=0, columnspan=10, padx=5, pady=5, sticky=E + W + S + N)
        self.canv.bind("<B1-Motion>", self.draw)
        color_lab = Label(self, text="Color:")
        color_lab.grid(row=0, column=0, padx=6)
        colors = ['green', 'blue', 'yellow', 'black', 'white', "red"]
        list_size = [2, 5, 7, 10, 13, 16, 20, 25, 30]

        self.color_buttons = self.create_buttons(0, colors, self.set_color)
        self.size_buttons = self.create_buttons(1, list_size, self.set_brush_size)

        clear_btn = Button(self, text="CLEAR", width=10, command=lambda: self.canv.delete("all"))
        clear_btn.grid(row=0, column=len(colors) + 1, sticky=W)

        size_lab = Label(self, text="SIZE:")
        size_lab.grid(row=1, column=0, padx=5)


def main():
    root = Tk()
    root.attributes('-fullscreen', True)
    app = Paint(root)
    root.mainloop()


if __name__ == '__main__':
    main()
