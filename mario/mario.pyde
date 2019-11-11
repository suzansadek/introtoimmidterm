import os
path = os.getcwd()
                
class Game:
    def __init__(self, w, h, g):
        # add attributes here for width, height and ground

        
    def display(self):
        # draw ground here with color coding: 0, 140, 0
        
        
game = Game(1024, 768, 600)

def setup():
    size(game.w, game.h)
    background(255, 255, 255)
    
def draw():
    background(255, 255, 255)
    game.display()
    
