//logo initialization on lcd screen
void logo(){
  byte acustomChar[] = {
  B00000,
  B00000,
  B00000,
  B00001,
  B00011,
  B00110,
  B01100,
  B11000
};
  byte bcustomChar[] = {
  B00100,
  B01110,
  B11111,
  B11111,
  B00000,
  B00000,
  B01111,
  B01111
};

byte ccustomChar[] = {
  B00000,
  B00000,
  B00000,
  B10000,
  B11000,
  B01100,
  B00110,
  B00011
};


byte dcustomChar[] = {
  B00001,
  B00011,
  B00111,
  B01111,
  B11111,
  B00000,
  B00000,
  B00000
};
byte ecustomChar[] = {
  B11000,
  B11100,
  B11110,
  B11111,
  B11111,
  B00000,
  B00000,
  B00000
};
byte fcustomChar[] = {
  B00000,
  B00000,
  B00000,
  B11111,
  B11111,
  B00000,
  B00000,
  B00000
};
byte gcustomChar[] = {
  B00011,
  B00111,
  B01111,
  B11111,
  B11111,
  B00000,
  B00000,
  B00000
};
byte hcustomChar[] = {
  B10000,
  B11000,
  B11100,
  B11110,
  B11111,
  B00000,
  B00000,
  B00000
};




//normal
  lcd.begin(16,2);
  lcd.createChar(1, acustomChar);
  lcd.setCursor(6,0);
  lcd.write(1);
  lcd.createChar(2, bcustomChar);
  lcd.setCursor(7,0);
  lcd.write(2);
  lcd.createChar(3, ccustomChar);
  lcd.setCursor(8,0);
  lcd.write(3);
  lcd.createChar(4, dcustomChar);
  lcd.setCursor(5,1);
  lcd.write(4);
  lcd.createChar(5, ecustomChar);
  lcd.setCursor(6,1);
  lcd.write(5);
  lcd.createChar(6, fcustomChar);
  lcd.setCursor(7,1);
  lcd.write(6);
  lcd.createChar(7, gcustomChar);
  lcd.setCursor(8,1);
  lcd.write(7);
  lcd.createChar(8, hcustomChar);
  lcd.setCursor(9,1);
  lcd.write(8);
  
  
  delay(100);
  
  }
