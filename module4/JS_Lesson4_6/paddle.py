from gameObject  import GameObject
class Paddle(GameObject):
    def __init__(self, canvas,x,y):
        self.width=80
        self.height=10
        ball=None
        item = canvas.create_rectangle(x-self.width/2, y-self.height/2,x +self.height/2, y+ self.height/2, fill='black')
    def set_ball(self):
        self.ball=ball
    def move(self, offset):
        coords = self.get.position()
        width = self.canvas.winfo_width()
        if coords[0] + offset >=0 and coords[2]+ offset<=width:
            super(Paddle,self).move(offset,0)
            if self.ball is not None:
                self.ball.move(offset,0)