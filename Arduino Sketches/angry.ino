//angry initialization on lcd screen
void angry(){
byte angrycustomChar1[] = {
  B00001,
  B00011,
  B00111,
  B01110,
  B11110,
  B11111,
  B11111,
  B11111
};
byte angrycustomChar2[] = {
  B11111,
  B11111,
  B11111,
  B11111,
  B01110,
  B00100,
  B11111,
  B11111
  
};
byte angrycustomChar3[] = {
  B10000,
  B11000,
  B11100,
  B01110,
  B01111,
  B11111,
  B11111,
  B11111
};
byte angrycustomChar1b[] = {
  B00001,
  B00011,
  B00111,
  B01111,
  B11111,
  B11111,
  B11111,
  B11111
};
byte angrycustomChar2b[] = {
  B11111,
  B11111,
  B11111,
  B11111,
  B11111,
  B11111,
  B11111,
  B11111
};
byte angrycustomChar3b[] = {
  B10000,
  B11000,
  B11100,
  B11110,
  B11111,
  B11111,
  B11111,
  B11111
};

byte angrycustomChar4[] = {
  B11111,
  B11111,
  B11111,
  B11110,
  B01111,
  B00111,
  B00011,
  B00000
};
byte angrycustomChar5[] = {
  B11111,
  B11111,
  B00000,
  B11111,
  B11111,
  B11111,
  B11111,
  B00000
};
byte angrycustomChar6[] = {
  B11111,
  B11111,
  B11111,
  B01111,
  B11110,
  B11100,
  B11000,
  B00000
};
//angry
  lcd.begin(16, 2);
  lcd.createChar(5, angrycustomChar1);
  lcd.setCursor(6,0);
  lcd.write(5);
  lcd.createChar(6, angrycustomChar2);
  lcd.setCursor(7,0);
  lcd.write(6);
  lcd.createChar(7, angrycustomChar3);
  lcd.setCursor(8,0);
  lcd.write(7);
  lcd.createChar(8, angrycustomChar4);
  lcd.setCursor(6,1);
  lcd.write(8);
  lcd.createChar(9, angrycustomChar5);
  lcd.setCursor(7,1);
  lcd.write(9);
  lcd.createChar(10, angrycustomChar6);
  lcd.setCursor(8,1);
  lcd.write(10);
  delay(1000);
//angry wink  
  lcd.begin(16, 2);
  lcd.createChar(11, angrycustomChar1b);
  lcd.setCursor(6,0);
  lcd.write(11);
  lcd.createChar(12, angrycustomChar2b);
  lcd.setCursor(7,0);
  lcd.write(12);
  lcd.createChar(13, angrycustomChar3b);
  lcd.setCursor(8,0);
  lcd.write(13);
  lcd.createChar(8, angrycustomChar4);
  lcd.setCursor(6,1);
  lcd.write(8);
  lcd.createChar(9, angrycustomChar5);
  lcd.setCursor(7,1);
  lcd.write(9);
  lcd.createChar(10, angrycustomChar6);
  lcd.setCursor(8,1);
  lcd.write(10);
  delay(500);      
      }
