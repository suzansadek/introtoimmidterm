class Borders{
  float x, y, x2, y2;
  
  Borders (int _x, int _y, int _x2, int _y2 ){
    x = _x;
    y = _y;
    x2 = _x2;
    y2 = _y2;
    
  
  }
  
  void displayBorders(){
  //stroke(200);
  noStroke();
  line(x,y,x2,y2);
  }
}
