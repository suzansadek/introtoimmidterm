// creature cats

class Cats{
  float x, y, r, w , h, x1, x2;
  float vy = 0;
  float vx = 0;
  boolean alive = true;
  PImage img; 

  Cats (float _x, float _y, int _r, int _w, int _h, int _x1,int  _x2){
   x = _x;
   y = _y;
   r = _r;
   vy = 0;
   vx = random(1,3);
   w = _w;
   h = _h;
   x1 = _x1;
   x2 = _x2;   
   img = loadImage("cat" + str(int(random(1,3))) + ".png");
   
  }
  
  void display(){
    update();
    noFill();
    noStroke();
    image( img, x-r, y-r, 50, 50);
    circle(x,y, r*2);
  }
  
  void update(){
    
    y += vy;
    x += vx; 
    
    if (x < x1){
      vx *= -1;
    }
    else if ( x > x2){
    vx *= -1;
    }
  }
  
  float distance(int tarX, int tarY){
    return (pow( (pow(( x - tarX), 2) + pow((y - tarY),2)), 0.5));
  }

}
