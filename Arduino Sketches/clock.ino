//clock initialization on lcd screen
void clock1(){
  byte customChar1[] = {
  B00000,
  B00000,
  B00001,
  B00010,
  B00100,
  B01000,
  B10000,
  B10000
};
  byte customChar2[] = {
  B00000,
  B11111,
  B00000,
  B00000,
  B00000,
  B00100,
  B00100,
  B00100
};
byte customChar3[] = {
  B00000,
  B00000,
  B10000,
  B01000,
  B00100,
  B00010,
  B00001,
  B00001
};
byte customChar4[] = {
  B10000,
  B10000,
  B01000,
  B00100,
  B00010,
  B00001,
  B00000,
  B00000
};
byte customChar5[] = {
  B00000,
  B00000,
  B00000,
  B00000,
  B00000,
  B00000,
  B11111,
  B00000
};
byte customChar6[] = {
  B00001,
  B00001,
  B00010,
  B00100,
  B01000,
  B10000,
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
  delay(200);

  
  
  
  }
void clock2(){
  byte customChar1[] = {
  B00000,
  B00000,
  B00001,
  B00010,
  B00100,
  B01000,
  B10000,
  B10000
};
  byte customChar2[] = {
  B00000,
  B11111,
  B00000,
  B00000,
  B00000,
  B00001,
  B00010,
  B00100
};
byte customChar3[] = {
  B00000,
  B00000,
  B10000,
  B01000,
  B00100,
  B00010,
  B00001,
  B00001
};
byte customChar4[] = {
  B10000,
  B10000,
  B01000,
  B00100,
  B00010,
  B00001,
  B00000,
  B00000
};
byte customChar5[] = {
  B00000,
  B00000,
  B00000,
  B00000,
  B00000,
  B00000,
  B11111,
  B00000
};
byte customChar6[] = {
  B00001,
  B00001,
  B00010,
  B00100,
  B01000,
  B10000,
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
  delay(200);

  
  
  
  }
void clock3(){
  byte customChar1[] = {
  B00000,
  B00000,
  B00001,
  B00010,
  B00100,
  B01000,
  B10000,
  B10000
};
  byte customChar2[] = {
  B00000,
  B11111,
  B00000,
  B00000,
  B00000,
  B00000,
  B00000,
  B00111
};
byte customChar3[] = {
  B00000,
  B00000,
  B10000,
  B01000,
  B00100,
  B00010,
  B00001,
  B10001
};
byte customChar4[] = {
  B10000,
  B10000,
  B01000,
  B00100,
  B00010,
  B00001,
  B00000,
  B00000
};
byte customChar5[] = {
  B00000,
  B00000,
  B00000,
  B00000,
  B00000,
  B00000,
  B11111,
  B00000
};
byte customChar6[] = {
  B00001,
  B00001,
  B00010,
  B00100,
  B01000,
  B10000,
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
  delay(200);

  
  
  
  }
void clock4(){
  byte customChar1[] = {
  B00000,
  B00000,
  B00001,
  B00010,
  B00100,
  B01000,
  B10000,
  B10000
};
  byte customChar2[] = {
  B00000,
  B11111,
  B00000,
  B00000,
  B00000,
  B00000,
  B00000,
  B00100
};
byte customChar3[] = {
  B00000,
  B00000,
  B10000,
  B01000,
  B00100,
  B00010,
  B00001,
  B00001
};
byte customChar4[] = {
  B10000,
  B10000,
  B01000,
  B00100,
  B00010,
  B00001,
  B00000,
  B00000
};
byte customChar5[] = {
  B00010,
  B00001,
  B00000,
  B00000,
  B00000,
  B00000,
  B11111,
  B00000
};
byte customChar6[] = {
  B00001,
  B00001,
  B00010,
  B00100,
  B01000,
  B10000,
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
  delay(200);

  
  
  
  }
void clock5(){
  byte customChar1[] = {
  B00000,
  B00000,
  B00001,
  B00010,
  B00100,
  B01000,
  B10000,
  B10000
};
  byte customChar2[] = {
  B00000,
  B11111,
  B00000,
  B00000,
  B00000,
  B00000,
  B00000,
  B00100
};
byte customChar3[] = {
  B00000,
  B00000,
  B10000,
  B01000,
  B00100,
  B00010,
  B00001,
  B00001
};
byte customChar4[] = {
  B10000,
  B10000,
  B01000,
  B00100,
  B00010,
  B00001,
  B00000,
  B00000
};
byte customChar5[] = {
  B00100,
  B00100,
  B00100,
  B00000,
  B00000,
  B00000,
  B11111,
  B00000
};
byte customChar6[] = {
  B00001,
  B00001,
  B00010,
  B00100,
  B01000,
  B10000,
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
  delay(200);

  
  
  
  }
void clock6(){
  byte customChar1[] = {
  B00000,
  B00000,
  B00001,
  B00010,
  B00100,
  B01000,
  B10000,
  B10000
};
  byte customChar2[] = {
  B00000,
  B11111,
  B00000,
  B00000,
  B00000,
  B00000,
  B00000,
  B00100
};
byte customChar3[] = {
  B00000,
  B00000,
  B10000,
  B01000,
  B00100,
  B00010,
  B00001,
  B00001
};
byte customChar4[] = {
  B10000,
  B10000,
  B01000,
  B00100,
  B00010,
  B00001,
  B00000,
  B00000
};
byte customChar5[] = {
  B01000,
  B10000,
  B00000,
  B00000,
  B00000,
  B00000,
  B11111,
  B00000
};
byte customChar6[] = {
  B00001,
  B00001,
  B00010,
  B00100,
  B01000,
  B10000,
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
  delay(200);

  
  
  
  }
void clock7(){
  byte customChar1[] = {
  B00000,
  B00000,
  B00001,
  B00010,
  B00100,
  B01000,
  B10000,
  B10001
};
  byte customChar2[] = {
  B00000,
  B11111,
  B00000,
  B00000,
  B00000,
  B00000,
  B00000,
  B11100
};
byte customChar3[] = {
  B00000,
  B00000,
  B10000,
  B01000,
  B00100,
  B00010,
  B00001,
  B00001
};
byte customChar4[] = {
  B10000,
  B10000,
  B01000,
  B00100,
  B00010,
  B00001,
  B00000,
  B00000
};
byte customChar5[] = {
  B00000,
  B00000,
  B00000,
  B00000,
  B00000,
  B00000,
  B11111,
  B00000
};
byte customChar6[] = {
  B00001,
  B00001,
  B00010,
  B00100,
  B01000,
  B10000,
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
  delay(200);

  
  
  
  }

//  void clock_() {
//    clock1();
//    clock2();
//    clock3();
//    clock4();
//    clock5();
//    clock6();
//    clock7();
//    
//    
//    }
