import os
path = os.getcwd()

class Creature:
    def __init__(self, x, y, r, g, img, w, h, frames):
        self.x = x
        self.y = y
        self.r = r
        self.g = g
        self.vy = 0
        self.vx = 0
        self.img = loadImage(path + "/images/" + img)
        self.img_w = w
        self.img_h = h
        self.slice = 7
        self.direction = RIGHT 
        self.frames = frames             
  
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
        # circle(self.x, self.y, self.r * 2)
        if self.direction == RIGHT:
            image(self.img, self.x - self.img_w//2, self.y - self.img_h//2, self.img_w, self.img_h, self.slice * self.img_w, 0, (self.slice + 1) * self.img_w, self.img_h)        
        elif self.direction == LEFT:
            image(self.img, self.x - self.img_w//2, self.y - self.img_h//2, self.img_w, self.img_h, (self.slice + 1) * self.img_w, 0, (self.slice) * self.img_w, self.img_h)
            
class Mario(Creature):
    def __init__(self, x, y, r, g, img, w, h, frames):
        Creature.__init__(self, x, y, r, g, img, w, h, frames)
        self.key_handler = {LEFT:False, RIGHT:False, UP:False}                                                               
                           
    def update(self):
        self.gravity()
        
        if self.key_handler[LEFT] == True:
            self.vx = -5
            self.direction = LEFT
        elif self.key_handler[RIGHT] == True:
            self.vx = 5
            self.direction = RIGHT
        else:
            self.vx = 0
        
        if self.key_handler[UP] == True and self.y+self.r == self.g:
            self.vy = -15
        
        self.y += self.vy
        self.x += self.vx
        
        if frameCount % 5 == 0 and self.vx != 0 and self.vy == 0:
            self.slice = (self.slice + 1) % self.frames
        
        if self.x - self.r < 0:
            self.x = self.r
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          
class Game:
    def __init__(self, w, h, g):
        self.w = w
        self.h = h
        self.g = g
        self.mario = Mario(50, 50, 35, self.g, "mario.png", 100, 70, 11)
        
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

def keyPressed():
    if keyCode == LEFT:
        game.mario.key_handler[LEFT] = True
    elif keyCode == RIGHT:
        game.mario.key_handler[RIGHT] = True
    elif keyCode == UP:
        game.mario.key_handler[UP] = True
    
def keyReleased():
    if keyCode == LEFT:
        game.mario.key_handler[LEFT] = False
    elif keyCode == RIGHT:
        game.mario.key_handler[RIGHT] = False
    elif keyCode == UP:
        game.mario.key_handler[UP] = False   
    
    
    
    
