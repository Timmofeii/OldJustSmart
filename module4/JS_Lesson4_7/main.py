from tkinter import Tk
from game import Game

if __name__ == '__main__':
    root = Tk()
    root.title('Break those Bricks!')
    game = Game(root)
    game.mainloop()
