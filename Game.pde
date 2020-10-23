import processing.sound.*;
PImage img;
StringList tally;

class Game {
  float w, h, g;
  int count = 120;
  float scorecount = 0;
  boolean totalwin = false;
  
  String str1 = "I I I I I I";
  char data[] = {'I', 'I', 'I', 'I', 'I', 'I', 'I'};
  
  
  Game(int _w, int _h, int _g){
   w = _w;
   h = _h;
   g = _g;
   img = loadImage("map.jpg");
   tally = new StringList("I","I","I", "I", "I","I" );
   
}

void display (){
  
  image (img, 0,0);
  fill (0,0,0);
  textSize(25);
  text("Time Remaining: " + count , 365, 50);
  fill(255,255,255);
  //textSize(25);
  text("Time Remaining: " + count , 363, 48 );
  fill(255, 0, 0);
  text (str1, 50, 50);
  if (creature.alive == true){
    if (frameCount % 60 == 0){
      //println (frameCount);
      count   -=1;
    }
  }
}
}
  
