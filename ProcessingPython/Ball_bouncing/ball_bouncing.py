from processing_py import *

class Ball:
    
    def __init__(self,x=0,y=0,x_speed=5,y_speed=2.3):
        self.x = x
        self.y = y
        self.x_speed = x_speed
        self.y_speed = y_speed
        
    def display(self):
        app.stroke(0)
        app.fill(127)
        app.ellipse(self.x,self.y,32,32)
        
    def update(self):
        self.x = self.x + self.x_speed
        self.y = self.y + self.y_speed
        
    def check_edges(self):
        if self.x > app.width or self.x < 0:
            self.x_speed = self.x_speed*-1
        elif self.y > app.height or self.y < 0:
            self.y_speed = self.y_speed*-1


app = App(420,340)
app.background(255,46)
b = Ball(0,2,4,3.3)  
b.update()
b.check_edges()
b.display()