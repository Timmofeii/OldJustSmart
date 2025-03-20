import tkinter as tk

window = tk.Tk()  # створення об'єкта Tkinter
window.title("HomeWork")  # встановлення назви вікна
window.geometry("300x200")  # встановлення розміру вікна

label = tk.Label(text="start text")  # додавання мітки з текстом
label.pack()  # упаковка мітки

entry = tk.Entry(window)  # додавання поля для введення тексту
entry.pack(pady=10)  # упаковка поля з відступом

# функція для зміни тексту в мітці при натисканні кнопки
def changeText():
    new_text = entry.get()  # отримання тексту з поля введення
    label.configure(text=new_text)  # встановлення нового тексту в мітку

button = tk.Button(text="Click to change the text")  # додавання кнопки
button.configure(command=changeText)  # встановлення команди для кнопки
button.pack(pady=10)  # упаковка кнопки з відступом

window.mainloop()  # запуск головного циклу програми