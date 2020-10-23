class Locations{
  float x, y, r;
  boolean win = false;
  
  Locations ( int _x, int _y, int _r){
  x = _x;
  y = _y;
  r = _r;
  }
  
  void display() {
  //fill(255, 255, 255);
  noStroke();
  noFill();
  circle( x, y, r );
  }
  
  float distance(int tarX, int tarY){
    return (pow( (pow(( x - tarX), 2) + pow((y - tarY),2)), 0.5));
  }
  
}
