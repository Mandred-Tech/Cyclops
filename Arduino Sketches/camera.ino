//camera initialization on lcd screen
void camera(){
  byte customChar1[] = {
  B00000,
  B00000,
  B01111,
  B11111,
  B11110,
  B11101,
  B11011,
  B11011
};
byte customChar2[] = {
  B00000,
  B00000,
  B11111,
  B11111,
  B00000,
  B11111,
  B11111,
  B10001
};
byte customChar3[] = {
  B00000,
  B00000,
  B11110,
  B11011,
  B01111,
  B10111,
  B11011,
  B11011
};
byte customChar4[] = {
  B11011,
  B11011,
  B11101,
  B11110,
  B11111,
  B01111,
  B00000,
  B00000
};
byte customChar5[] = {
  B10001,
  B11111,
  B11111,
  B00000,
  B11111,
  B11111,
  B00000,
  B00000
};
byte customChar6[] = {
  B11011,
  B11011,
  B10111,
  B01111,
  B11111,
  B11110,
  B00000,
  B00000
};
  byte customChar2b[] = {
  B00000,
  B00000,
  B11111,
  B11111,
  B00000,
  B11111,
  B11111,
  B11111
};
  byte customChar5b[] = {
  B11111,
  B11111,
  B11111,
  B00000,
  B11111,
  B11111,
  B00000,
  B00000
};

  lcd.begin(16,2);
  lcd.createChar(1, customChar1);
  lcd.setCursor(6,0);
  lcd.write(1);
  lcd.createChar(2, customChar2);
  lcd.setCursor(7,0);
  lcd.write(2);
  lcd.createChar(3, customChar3);
  lcd.setCursor(8,0);
  lcd.write(3);
  lcd.createChar(4, customChar4);
  lcd.setCursor(6,1);
  lcd.write(4);
  lcd.createChar(5, customChar5);
  lcd.setCursor(7,1);
  lcd.write(5);
  lcd.createChar(6, customChar6);
  lcd.setCursor(8,1);
  lcd.write(6);
  delay(500);
  //camera click
  lcd.begin(16,2);
  lcd.createChar(1, customChar1);
  lcd.setCursor(6,0);
  lcd.write(1);
  lcd.createChar(7, customChar2b);
  lcd.setCursor(7,0);
  lcd.write(7);
  lcd.createChar(3, customChar3);
  lcd.setCursor(8,0);
  lcd.write(3);
  lcd.createChar(4, customChar4);
  lcd.setCursor(6,1);
  lcd.write(4);
  lcd.createChar(8, customChar5b);
  lcd.setCursor(7,1);
  lcd.write(8);
  lcd.createChar(6, customChar6);
  lcd.setCursor(8,1);
  lcd.write(6);
  delay(500);
}
