
int count = 120;
PImage dead, won;
Game game;
Creature creature;
Cats[] cats;
Borders[] horizentalBorders;
Borders[] verticalBorders;
Locations[] locations;
SoundFile backgroundSound, baraha, knock, theatre, library, palms, dining, alarm;

void setup(){
    size(1024, 768);
    background(255, 255, 255);
    SoundFile[] sounds = new SoundFile[7]; 
    creature = new Creature (50, 50, 10);
    game = new Game (1024, 786, 585);
    cats = new Cats[3];
    for ( int g = 0; g< 3; g++){
      cats[g] = new Cats (int(random(200,900)), int(random(200,600)), 15, 70, 70, 200, 800);
    }
    locations = new Locations[7];
    locations[0] = new Locations (250, 270, 100); // library
    locations[1] = new Locations ( 250, 470, 100); // Palms
    locations[2] = new Locations (400, 310, 50); //baraha
    locations[3] = new Locations (790, 250, 100); //theatre
    locations[4] = new Locations (950, 400, 100); //dining
    locations[5] = new Locations (800, 620, 200); // knock
    locations[6] = new Locations (570, 570, 200); // alarm
    horizentalBorders = new Borders[14];
    verticalBorders = new Borders[13];
    horizentalBorders[1] = new Borders (444, 286, 575, 286); //h
    horizentalBorders[2] = new Borders (442, 346, 520, 346); //h 
    horizentalBorders[3] = new Borders (402, 470, 502, 470); //h
    horizentalBorders[4] = new Borders (590, 472, 712, 472); //h
    horizentalBorders[5] = new Borders (754, 493, 812, 493); //h
    horizentalBorders[6] = new Borders (70, 175, 440, 175); // h
    horizentalBorders[7] = new Borders (70, 375, 422, 375); //h
    horizentalBorders[8] = new Borders (310, 725, 970, 725); //h
    horizentalBorders[9] = new Borders (530, 527, 586, 527); //h 
    horizentalBorders[10] = new Borders (536, 595, 586, 595); // h
    horizentalBorders[11] = new Borders (350, 614, 396, 614); //h
    horizentalBorders[12] = new Borders (754, 602, 808, 602); // h
    horizentalBorders[0] = new Borders (756, 640, 808, 640); // h
    verticalBorders[12] = new Borders (440, 175, 440, 270); //h
    verticalBorders[1] = new Borders (540, 346, 540, 455); //v
    verticalBorders[2] = new Borders (582, 286, 582, 456);// v
    verticalBorders[3] = new Borders (70, 175, 70, 375); //v
    verticalBorders[4] = new Borders (310, 572, 310, 725); //v
    verticalBorders[5] = new Borders (970, 525, 970, 725);  // v
    verticalBorders[6] = new Borders (775, 675, 775, 720); // v
    verticalBorders[7] = new Borders (800, 675, 800, 720); //v 
    verticalBorders[8] = new Borders (586, 527, 586, 595); // v
    verticalBorders[9] = new Borders (536, 529, 536, 595); //v
    verticalBorders[10] = new Borders (396, 614, 396, 664); //v
    verticalBorders[11] = new Borders (808, 602, 808, 640); // v
    verticalBorders[0] = new Borders (756, 602, 756, 640); // v
    
    dead = loadImage("sorry.png");
    won = loadImage("finalpage.png");
    //borders8 = new Borders (874, 541, 874, 509); // v
    //borders15 = new Borders (948, 620, 948, 533); // v
    //borders16 = new Borders (158, 370, 158, 1823); //v
    
    backgroundSound = new SoundFile(this, "OriginalBacktrack.mp3");
    sounds[0] = new SoundFile(this, "CardSwipe.mp3");
    sounds[1]= new SoundFile(this, "Knock_RA.mp3");
    sounds[2]= new SoundFile(this, "SneezeCough.mp3");
    sounds[3] = new SoundFile(this, "Typing_clicking.mp3"); 
    sounds[4] = new SoundFile(this, "Birds.mp3");
    sounds[5]= new SoundFile(this, "Didyoudothereading.mp3");   
    sounds[6] = new SoundFile(this, "iPhoneAlarm.mp3"); 
   
}

void draw (){
  game.display();
  creature.display();
  for ( int g = 0; g< 3; g++){
    cats[g].display();
  }
  for ( int n = 0; n < 12; n ++) {
    horizentalBorders[n].displayBorders();
  }
  for ( int m = 0; m < 13; m ++) {
    verticalBorders[m].displayBorders();
  }
   for ( int l = 0; l <7; l ++) {
    locations[l].display();
  }
  if (count == 0){
    creature.alive = false;
    // close the sounds
  }
  if (creature. alive == false && creature.win == false){
     image (dead, 187, 59);
  //   // add close sounds 
   }
  if (creature. alive == false && creature.win == true){
     image (won, 187, 59);
  //   // add close sounds 
   }
}
   
void mouseClicked(){
  if ( creature.alive == true){
    game = new Game (1024, 786, 585);
  }
  if (creature.alive == false){
    game = new Game (1024, 786, 585);
    println("restart");
  }
    



}
