import os, random
path = os.getcwd()
NUM_ROWS = 4
NUM_COLS = 4
RESOLUTION = 800
class Tile:
    def __init__(self, r, c):
        self.r = r
        self.c = c
        self.v = r * NUM_COLS + c
        self.img = loadImage(path + "/images/" + str(self.v) + ".png")

    def show(self):
        if self.v != 15:
            image(self.img, self.c * RESOLUTION/NUM_COLS, self.r * RESOLUTION/NUM_ROWS)
            noFill()
            stroke(0,0,0)
            strokeWeight(5)
            rect(self.c * RESOLUTION/NUM_COLS, self.r * RESOLUTION/NUM_ROWS, RESOLUTION/NUM_COLS, RESOLUTION/NUM_ROWS)
    
    def swap(self, target):
        tmp_v= self.v
        tmp_img = self.img
        self.v = target.v
        self.img = target.img
        target.v = tmp_v
        target.img = tmp_img
        
        
class Puzzle(list):
    def __init__(self):
        for r in range(NUM_ROWS):
            for c in range(NUM_COLS):
                self.append(Tile(r, c))

        self.shuffle()
        
    def show_tiles(self):
        for tile in self:
            tile.show()
            
        r = mouseY//(RESOLUTION/NUM_ROWS)
        c = mouseX//(RESOLUTION/NUM_COLS)
        stroke(255, 0, 0)
        noFill()
        strokeWeight(5)
        rect(c*200, r*200, 200, 200)
        
    def get_tile(self, r, c):
        for t in self:
            if t.r == r and t.c == c:
                return t
        return False
    
    def shuffle(self):
        empty_tile = self.get_tile(NUM_ROWS-1, NUM_COLS-1)
        
        for i in range(10):
            neighbors = [[-1,0], [0,-1], [1,0], [0,1]]
            n = neighbors[random.randint(0,3)]
            next_tile = self.get_tile(empty_tile.r + n[0], empty_tile.c + n[1])
            
            if next_tile != False:
                empty_tile.swap(next_tile)
                empty_tile = next_tile
                
    def clicked(self):
        r = mouseY//(RESOLUTION/NUM_ROWS)
        c = mouseX//(RESOLUTION/NUM_COLS)
        tile = self.get_tile(r,c)
        for neighbor in [[-1,0], [0,-1], [1,0], [0,1]]:
            next_tile = self.get_tile(r + neighbor[0], c + neighbor[1])
            if next_tile != False and next_tile.v == 15:
                tile.swap(next_tile)
            
    
puzzle = Puzzle()

def setup():
    size(RESOLUTION, RESOLUTION)
    background(0,0,0)
    
def draw():
    background(0)
    puzzle.show_tiles()
    
def mouseClicked():
    puzzle.clicked()
    
