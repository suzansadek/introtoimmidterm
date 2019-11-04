img = ''

def setup():
    global img
    img = loadImage('nyu.jpg')
    size(800, 600)
    background(0)

def draw():
    #syntax: image(img, x, y, width, height, x1, y1, x2, y2):
    image(img, 0, 0)
    image(img, 200, 0, 200, 200)
    image(img, 0, 250, 50, 50)
    image(img, 100, 250, 50, 50, 100, 100, 200, 200)
    image(img, 200, 250, 50, 50, 200, 200, 0, 0)
    image(img, 300, 250, 50, 50, 200, 0, 0, 200)
