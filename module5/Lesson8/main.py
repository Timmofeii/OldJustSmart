import os

try:
    os.system("pip3 install pyinstaller")
except Exception as e:
    print(f"Виникла помилка під час встановлення PyInstaller: {e}")

try:
    os.system("pyinstaller -F file.py")
    print("file.py has been made into an exe")
except Exception as e:
    print("there was a problem with making file.py into an exe")

# Подальші команди, якщо встановлення PyInstaller вдалося або виникла помилка
print("Продовжувати роботу з PyInstaller...")
