//game parameters initialization on lcd screen
void init_game(){
  
byte pac1Def[8] = {
B00000,
B01110,
B11011,
B11111,
B11111,
B01110,
B00000,
B00000
};
byte pac2Def[8] = {
B00000,
B01110,
B10100,
B11000,
B11100,
B01110,
B00000,
B00000
};
byte pillDef[8] = {
B00000,
B00000,
B00000,
B01100,
B01100,
B00000,
B00000,
B00000
};

const byte pac1 = 0x0;
const byte pac2 = 0x1;
const byte pill = 0x2;


lcd.createChar(1, pac1Def);
lcd.createChar(2, pac2Def);
lcd.createChar(3, pillDef);
lcd.clear();



 
  
 



  
  

  
}
