import os
path = os.getcwd()
NUM_ROWS = 4
NUM_COLS = 4
RESOLUTION = 800
class Tile:
    def __init__(self, r, c):
        self.r = r
        self.c = c
        self.v = r * NUM_ROWS + c
        self.img = loadImage(path + "/images/" + str(self.v) + ".png")

    def show(self):
        image(self.img, self.c * RESOLUTION/NUM_COLS, self.r * RESOLUTION/NUM_ROWS)
    
class Puzzle(list):
    def __init__(self):
        for r in range(NUM_ROWS):
            for c in range(NUM_COLS):
                self.append(Tile(r, c))

puzzle = Puzzle()

def setup():
    size(RESOLUTION, RESOLUTION)
    background(0,0,0)
    
def draw():
    for tile in puzzle:
        tile.show()
