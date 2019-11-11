import os
path = os.getcwd()

class Creature:
    def __init__(self, x, y, r, g):
        self.x = x
        self.y = y
        self.r = r
        self.g = g
        self.vy = 0
        self.vx = 0               
  
    def gravity(self):
        
        if self.y + self.r >= self.g:
            self.vy = 0
        else:
            self.vy += 0.4
            
            if self.y + self.r + self.vy > self.g:
                self.vy = self.g - (self.y+self.r)
            
    def update(self):
        self.gravity()
        self.y += self.vy
        self.x += self.vx
        
    def display(self):
        self.update()
        circle(self.x, self.y, self.r * 2)        
                                                                
class Game:
    def __init__(self, w, h, g):
        self.w = w
        self.h = h
        self.g = g
        self.mario = Creature(50, 50, 35, self.g)
        
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

    
