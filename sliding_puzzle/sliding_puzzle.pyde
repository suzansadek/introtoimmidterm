import os
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
        image(self.img, self.c * RESOLUTION/NUM_COLS, self.r * RESOLUTION/NUM_ROWS)
        noFill()
        stroke(0,0,0)
        strokeWeight(5)
        rect(self.c * RESOLUTION/NUM_COLS, self.r * RESOLUTION/NUM_ROWS, RESOLUTION/NUM_COLS, RESOLUTION/NUM_ROWS)
    
class Puzzle(list):
    def __init__(self):
        for r in range(NUM_ROWS):
            for c in range(NUM_COLS):
                self.append(Tile(r, c))

    def show_tiles(self):
        for tile in self:
            tile.show()
            
        r = mouseY//(RESOLUTION/NUM_ROWS)
        c = mouseX//(RESOLUTION/NUM_COLS)
        stroke(255, 0, 0)
        noFill()
        strokeWeight(5)
        rect(c*200, r*200, 200, 200)
            
puzzle = Puzzle()

def setup():
    size(RESOLUTION, RESOLUTION)
    background(0,0,0)
    
def draw():
    puzzle.show_tiles()
