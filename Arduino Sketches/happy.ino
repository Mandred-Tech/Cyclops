//happy initialization on lcd screen
void happy(){
byte happycustomChar1[] = {
  B00001,
  B00011,
  B00111,
  B01110,
  B11110,
  B11111,
  B11111,
  B11111
};
byte happycustomChar2[] = {
  B11111,
  B11111,
  B11111,
  B01110,
  B01110,
  B11111,
  B11111,
  B11111
};
byte happycustomChar3[] = {
  B10000,
  B11000,
  B11100,
  B01110,
  B01111,
  B11111,
  B11111,
  B11111
};
byte happycustomChar4[] = {
  B11011,
  B11000,
  B11100,
  B11110,
  B01111,
  B00111,
  B00011,
  B00001
};
byte happycustomChar5[] = {
  B11111,
  B00000,
  B00000,
  B00000,
  B00000,
  B11111,
  B11111,
  B11111
};
byte happycustomChar6[] = {
  B11011,
  B00011,
  B00111,
  B01111,
  B11110,
  B11100,
  B11000,
  B10000
};
byte happycustomChar1b[] = {
  B00001,
  B00011,
  B00111,
  B01111,
  B11111,
  B11111,
  B11111,
  B11111
};
byte happycustomChar2b[] = {
  B11111,
  B11111,
  B11111,
  B11111,
  B11111,
  B11111,
  B11111,
  B11111
};
byte happycustomChar3b[] = {
  B10000,
  B11000,
  B11100,
  B11110,
  B11111,
  B11111,
  B11111,
  B11111
};
  //happy   
  lcd.begin(16, 2);
  lcd.createChar(1, happycustomChar1);
  lcd.setCursor(6,0);
  lcd.write(1);
  lcd.createChar(2, happycustomChar2);
  lcd.setCursor(7,0);
  lcd.write(2);
  lcd.createChar(3, happycustomChar3);
  lcd.setCursor(8,0);
  lcd.write(3);
  lcd.createChar(4, happycustomChar4);
  lcd.setCursor(6,1);
  lcd.write(4);
  lcd.createChar(5, happycustomChar5);
  lcd.setCursor(7,1);
  lcd.write(5);
  lcd.createChar(6, happycustomChar6);
  lcd.setCursor(8,1);
  lcd.write(6);
  delay(1000);
//happy wink  
  lcd.begin(16, 2);
  lcd.createChar(7, happycustomChar1b);
  lcd.setCursor(6,0);
  lcd.write(7);
  lcd.createChar(8, happycustomChar2b);
  lcd.setCursor(7,0);
  lcd.write(8);
  lcd.createChar(9, happycustomChar3b);
  lcd.setCursor(8,0);
  lcd.write(9);
  lcd.createChar(4, happycustomChar4);
  lcd.setCursor(6,1);
  lcd.write(4);
  lcd.createChar(5, happycustomChar5);
  lcd.setCursor(7,1);
  lcd.write(5);
  lcd.createChar(6, happycustomChar6);
  lcd.setCursor(8,1);
  lcd.write(6);
  delay(500);  
  }
