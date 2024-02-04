//exercise state initialization on lcd screen
void exercise(){
  byte customCharhead[] = {
  B00000,
  B01110,
  B01110,
  B01110,
  B01110,
  B00100,
  B00100,
  B00100
};

byte customCharrhrl[] = {
  B11111,
  B00000,
  B00000,
  B00000,
  B10000,
  B11000,
  B01100,
  B00110
};
byte customCharlhll[] = {
  B11111,
  B00000,
  B00000,
  B00000,
  B00001,
  B00011,
  B00110,
  B01100
};
byte customCharmid[] = {
  B11111,
  B00100,
  B00100,
  B01110,
  B11011,
  B10001,
  B00000,
  B00000
};
byte customCharjumphead[] = {
  B01110,
  B01110,
  B01110,
  B01110,
  B00100,
  B00100,
  B00100,
  B11111
};
byte customCharjumpmid[] = {
  B11111,
  B11111,
  B00100,
  B01010,
  B11011,
  B11011,
  B11011,
  B11011
};
byte customCharjumplefthand[] = {
  B00001,
  B00011,
  B00110,
  B01100,
  B00000,
  B00000,
  B00000,
  B00000
};
byte customCharjumprighthand[] = {
  B10000,
  B11000,
  B01100,
  B00110,
  B00000,
  B00000,
  B00000,
  B00000
};

  //normal state 1
  lcd.begin(16,2);
  lcd.createChar(1, customCharhead);
  lcd.setCursor(7,0);
  lcd.write(1);
  lcd.createChar(2, customCharmid);
  lcd.setCursor(7,1);
  lcd.write(2);
  lcd.createChar(3, customCharlhll);
  lcd.setCursor(6,1);
  lcd.write(3);
  lcd.createChar(4, customCharrhrl);
  lcd.setCursor(8,1);
  lcd.write(4);
  delay(1000);
  lcd.begin(16, 2);
  //state 2
  lcd.createChar(5, customCharjumphead);
  lcd.setCursor(7,0);
  lcd.write(5);
  lcd.createChar(6, customCharjumpmid);
  lcd.setCursor(7,1);
  lcd.write(6);
  lcd.createChar(7, customCharjumplefthand);
  lcd.setCursor(6,1);
  lcd.write(7);
  lcd.createChar(8, customCharjumprighthand);
  lcd.setCursor(8,1);
  lcd.write(8);
  delay(1000);
  
  

  }
  
