import tkinter as tk
root = tk.Tk()
root.title("HomeWork")
root.geometry("250x200")
lab1 = tk.Label(root, text="First")
lab1.grid(row=0, column=0)
lab2 = tk.Label(root, text="Second")
lab2.grid(row=1, column=0)

e1 = tk.Entry(root)
e1.grid(row=0, column=1)
e2 = tk.Entry(root)
e2.grid(row=1, column=1)
root.mainloop()