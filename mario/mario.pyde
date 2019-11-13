add_library('minim')
import os, random
path = os.getcwd()
player = Minim(this)

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
        self.slice = 0
        self.direction = RIGHT 
        self.frames = frames             
  
    def gravity(self):
        
        if self.y + self.r >= self.g:
            self.vy = 0
        else:
            self.vy += 0.4
            
            if self.y + self.r + self.vy > self.g:
                self.vy = self.g - (self.y+self.r)
        
        for p in game.platforms:
            if self.y + self.r <= p.y and self.x + self.r >= p.x and self.x - self.r <= p.x + p.w:
                self.g = p.y
                break

            self.g = game.g
            
    def update(self):
        self.gravity()
        self.y += self.vy
        self.x += self.vx
            
        
    def display(self):
        self.update()
        # circle(self.x, self.y, self.r * 2)
        if self.direction == RIGHT:
            image(self.img, self.x - self.img_w//2 - game.x_shift, self.y - self.img_h//2, self.img_w, self.img_h, self.slice * self.img_w, 0, (self.slice + 1) * self.img_w, self.img_h)        
        elif self.direction == LEFT:
            image(self.img, self.x - self.img_w//2 - game.x_shift, self.y - self.img_h//2, self.img_w, self.img_h, (self.slice + 1) * self.img_w, 0, (self.slice) * self.img_w, self.img_h)
    
    def distance(self, target):
        return ((self.x - target.x)**2 + (self.y - target.y)**2) **0.5
    
    
class Mario(Creature):
    def __init__(self, x, y, r, g, img, w, h, frames):
        Creature.__init__(self, x, y, r, g, img, w, h, frames)
        self.key_handler = {LEFT:False, RIGHT:False, UP:False}                                                               
        self.alive = True
        self.jump_sound = player.loadFile(path + "/sounds/jump.mp3")
        self.kill_sound = player.loadFile(path + "/sounds/kill.mp3")
               
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
            self.vy = -12
            self.jump_sound.rewind()
            self.jump_sound.play()
        
        self.y += self.vy
        self.x += self.vx
        
        if frameCount % 5 == 0 and self.vx != 0 and self.vy == 0:
            self.slice = (self.slice + 1) % self.frames
        
        if self.x - self.r < 0:
            self.x = self.r
            
        for g in game.gombas:
            if g.distance(self) <= self.r + g.r:
                if self.vy > 0:
                    game.gombas.remove(g)
                    self.kill_sound.rewind()
                    self.kill_sound.play()
                else:
                    self.alive = False

        if self.x >= game.w//2:
            game.x_shift += self.vx
        
class Gomba(Creature):
    def __init__(self, x, y, r, g, img, w, h, frames, x1, x2):
        Creature.__init__(self, x, y, r, g, img, w, h, frames)
        self.vx = random.randint(1,5)
        self.x1 = x1
        self.x2 = x2
        
    def update(self):
        self.gravity()
        
        if self.x < self.x1:
            self.direction = RIGHT
            self.vx *= -1
        elif self.x > self.x2:
            self.direction = LEFT
            self.vx *= -1
        
        if frameCount % 10 == 0:
            self.slice = (self.slice + 1) % self.frames
            
        self.y += self.vy
        self.x += self.vx

class Platform:
    def __init__(self, x, y, w, h, img):
        self.x = x
        self.y = y
        self.w = w
        self.h = h
        self.img = loadImage(path + "/images/" + img)
        
    def display(self):
        fill(0, 255, 0)
        # rect(self.x, self.y, self. w, self.h)        
        image(self.img, self.x - game.x_shift, self.y, self.w, self.h)
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              
class Game:
    def __init__(self, w, h, g):
        self.w = w
        self.h = h
        self.g = g
        self.x_shift = 0
        self.background_sound = player.loadFile(path + "/sounds/background.mp3")
        self.background_sound.play()
        self.mario = Mario(50, 50, 35, self.g, "mario.png", 100, 70, 11)
        self.platforms = []
        for i in range(3):
            x = 200 + i * 300
            y = 500 - i * 100
            self.platforms.append(Platform(x, y, 200, 50, "platform.png"))
            
        self.gombas = []
        for i in range(4):
            self.gombas.append(Gomba(random.randint(200, 800), 50, 35, self.g, "gomba.png", 70, 70, 5, 200, 800))
            
        self.bg_images = []
        for i in range(1, 6):
            self.bg_images.append(loadImage(path + "/images/layer_0" + str(i) + ".png"))
        
    def display(self):
        if self.mario.alive == False:
            fill(255,0,0)
            textSize(15)
            text("Game over", 500, 350)
            self.background_sound.close()
            return
        
        # stroke(0, 140, 0)
        # fill(0, 140, 0)
        # rect(0, self.g, self.w, self.h)
        # noFill()
        # stroke(0,0,0)
        cnt = 1
        x = 0
        for img in self.bg_images[::-1]:
            if cnt == 1:
                x = self.x_shift//4
            elif cnt == 2:
                x = self.x_shift//3
            elif cnt == 3:
                x = self.x_shift//2
            elif cnt == 4 or cnt == 5:
                x = self.x_shift
            
            cnt += 1
            width_right = x % self.w
            width_left = self.w - width_right
            
            image(img, 0, 0, width_left, self.h, width_right, 0, self.w, self.h)
            image(img, width_left, 0, width_right, self.h, 0, 0, width_right, self.h)
        
        for p in self.platforms:
            p.display()
            
        for g in self.gombas:
            g.display()
            
        self.mario.display()
        
game = Game(1280, 720, 585)

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
    
def mouseClicked():
    global game
    if game.mario.alive == False:
        game = Game(1280, 720, 585)
    
    
    
