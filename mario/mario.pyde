import os
path = os.getcwd()
                
class Game:
    def __init__(self, w, h, g):
        self.w = w
        self.h = h
        self.g = g
        
    def display(self):
        stroke(0, 140, 0)
        fill(0, 140, 0)
        rect(0, self.g, self.w, self.h)
        
game = Game(1024, 768, 600)

def setup():
    size(game.w, game.h)
    background(255, 255, 255)
    
def draw():
    background(255, 255, 255)
    game.display()
    
