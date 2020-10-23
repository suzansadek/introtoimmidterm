
//This is creature thomas
class Creature{
  int x, y, r;
  float vy = 0;
  float vx = 0;
  int directionH = 0; 
  //int directionL = 1;
  boolean alive = true;
  boolean win = false;
  boolean borderCheckY = true;
  boolean borderCheckX = true;
  PImage img;
  boolean leftKey = false;
  boolean rightKey = false;
  boolean upKey = false;
  boolean downKey = false;
  
  Creature (int _x, int _y, int _r){
   x = _x;
   y = _y;
   r = _r;
   vy = 0;
   vx = 0;
   img = loadImage("thomas.png");
   
  }
  
  void display(){
   update();
   noFill();
   noStroke();
   image( img, x-r, y-r, 50, 50);
   circle(x,y, r*2);

  }
   
  void update(){
   keyPressed();
   
    y += vy;
    x += vx;
    
    if ( leftKey == true){
      directionH = 1;
      vx = -1;
    }
    else if ( rightKey == true){
      vx = 1;
      directionH = 0;
    }
    else if ( downKey == true){
      vy = 1;
    }
    else if ( upKey == true){
      vy = -1;
    }    
    else { 
      vx = 0;
      vy = 0;
    }
    
    collisionY();
    collisionX();
    
    for ( int g = 0; g< 3; g++){
      if (cats[g].distance(x,y) <= r +cats[g].r){
        alive = false;
        win = false;
      }
    }
    for ( int o = 0; o< 7; o++){
      if (locations[o].distance(x,y) <= 20){
        //game.d.remove(0);
        //win = true;
        //alive = false;
      }
    }
    
  }
  void collisionY(){
   for (int i = 0; i <13 ; i++ ){
     if ( vy + y + r >= horizentalBorders[i].y && 
       vx + x + r >= horizentalBorders[i].x &&
       x + vx +r <= horizentalBorders[i].x2 && 
       vy + y + r <= horizentalBorders[i].y2){
      println("stop1");
      //leftKey = false;
      vy = 0;
     }
    }
  }
  
  void collisionX(){
    for (int j = 0; j < 11; j++){
      if ( vx + x + (r*2) <= verticalBorders[j].x && 
           vx + x + (r*2) >= verticalBorders[j].x2 &&
           y + vy + r >= verticalBorders[j].y && 
           vy + y + r <= verticalBorders[j].y2){
        println("stop3");
         vx = 0;
      }
    }
  }
  
  void keyPressed(){
    if (keyPressed && keyCode == LEFT ) {
      leftKey = true;
    }
    else{
      leftKey = false;
    }
    if (keyPressed && keyCode == RIGHT) { //&& x+r <= game.w
      rightKey = true;
    }
    else{
      rightKey = false;
    }
    if (keyPressed && keyCode == UP) {
      upKey = true;
    }
    else{
      upKey = false;
    }
     if (keyPressed && keyCode == DOWN) { // && y+r <= game.h
      downKey = true;
    }
    else{
      downKey = false;
    }
  }
  
  
  
  float distanceCreature(int tarX, int tarY){
    return (pow( (pow(( x - tarX), 2) + pow((y - tarY),2)), 0.5));
  }
  
}
