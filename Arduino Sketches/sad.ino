//sad initialization on lcd screen
void sad(){
byte sadcustomChar1[] = {
  B00001,
  B00011,
  B00111,
  B01110,
  B11100,
  B11111,
  B11111,
  B11111
};
byte sadcustomChar2[] = {
  B11111,
  B11111,
  B11111,
  B01110,
  B00100,
  B11111,
  B11111,
  B11111
};
byte sadcustomChar3[] = {
  B10000,
  B11000,
  B11100,
  B01110,
  B00111,
  B11111,
  B11111,
  B11111
};
byte sadcustomChar1b[] = {
  B00001,
  B00011,
  B00111,
  B01111,
  B11111,
  B11111,
  B11111,
  B11111
};
byte sadcustomChar2b[] = {
  B11111,
  B11111,
  B11111,
  B11111,
  B11111,
  B11111,
  B11111,
  B11111
};
byte sadcustomChar3b[] = {
  B10000,
  B11000,
  B11100,
  B11110,
  B11111,
  B11111,
  B11111,
  B11111
};

byte sadcustomChar4[] = {
  B11111,
  B11111,
  B11110,
  B11100,
  B01101,
  B00111,
  B00011,
  B00001
};
byte sadcustomChar5[] = {
  B11111,
  B00000,
  B00000,
  B11111,
  B11111,
  B11111,
  B11111,
  B11111
};
byte sadcustomChar6[] = {
  B11111,
  B11111,
  B01111,
  B00111,
  B10110,
  B11100,
  B11000,
  B10000
};
    //sad
  lcd.begin(16, 2);
  lcd.createChar(11, sadcustomChar1);
  lcd.setCursor(6,0);
  lcd.write(11);
  lcd.createChar(12, sadcustomChar2);
  lcd.setCursor(7,0);
  lcd.write(12);
  lcd.createChar(13, sadcustomChar3);
  lcd.setCursor(8,0);
  lcd.write(13);
  lcd.createChar(14, sadcustomChar4);
  lcd.setCursor(6,1);
  lcd.write(14);
  lcd.createChar(15, sadcustomChar5);
  lcd.setCursor(7,1);
  lcd.write(15);
  lcd.createChar(1, sadcustomChar6);
  lcd.setCursor(8,1);
  lcd.write(1);
  delay(1000);
//sad wink  
  lcd.begin(16, 2);
  lcd.createChar(2, sadcustomChar1b);
  lcd.setCursor(6,0);
  lcd.write(2);
  lcd.createChar(3, sadcustomChar2b);
  lcd.setCursor(7,0);
  lcd.write(3);
  lcd.createChar(4, sadcustomChar3b);
  lcd.setCursor(8,0);
  lcd.write(4);
  lcd.createChar(14, sadcustomChar4);
  lcd.setCursor(6,1);
  lcd.write(14);
  lcd.createChar(15, sadcustomChar5);
  lcd.setCursor(7,1);
  lcd.write(15);
  lcd.createChar(1, sadcustomChar6);
  lcd.setCursor(8,1);
  lcd.write(1);
  delay(500);  
    }
