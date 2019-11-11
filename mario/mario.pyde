import os
path = os.getcwd()

class Creature:
    def __init__(self, x, y, r):
        self.x = x
        self.y = y
        self.r = r                
  
    def display(self):
        circle(self.x, self.y, self.r * 2)        
                                                                
class Game:
    def __init__(self, w, h, g):
        self.w = w
        self.h = h
        self.g = g
        self.mario = Creature(50, 50, 35)
        
    def display(self):
        stroke(0, 140, 0)
        fill(0, 140, 0)
        rect(0, self.g, self.w, self.h)
        noFill()
        stroke(0,0,0)
        self.mario.display()
        
game = Game(1024, 768, 600)

def setup():
    size(game.w, game.h)
    background(255, 255, 255)
    
def draw():
    background(255, 255, 255)
    game.display()
    
