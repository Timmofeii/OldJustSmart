from turtle import Screen

class Window(Screen):
    def __init__(self):
        super().__init__()  # Initialize the parent class
        self.title("PingPong")
        self.bgcolor("black")
        self.setup(width=800, height=600)
        self.listen()