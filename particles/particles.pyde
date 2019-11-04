class Particle:
    def __init__(self, cx, cy, d, r):
        self.px=0
        self.py=0
        self.cx=cx
        self.cy=cy
        self.d = d
        self.r = r
        self.theta = 0

    def update(self):
        self.theta=(self.theta+0.1)%360
        self.r -= 0.16
        self.px=self.cx+self.r*sin(self.theta)
        self.py=self.cy+self.r*cos(self.theta)
        
    
    def display(self):
        if self.r > 0:
            fill(random(0,255),random(0,255),random(0,255))
            ellipse(self.px, self.py, self.d, self.d)

p=[]

def setup():
    size(800,600)
    background(0)

def draw():
    for a in p:
        a.update()
        a.display()
        
def mouseClicked():
    p.append(Particle(mouseX, mouseY, 10, 100))
