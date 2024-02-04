//sinewave initialization on lcd screen
void sinewave2(){

int i=0;
int j=0;
int randomnum;
byte customChar1[] = {
  B11111,
  B11111,
  B11111,
  B11111,
  B11111,
  B11111,
  B11111,
  B11111
};

byte customChar2[] = {
  B00000,
  B00000,
  B11111,
  B11111,
  B11111,
  B11111,
  B11111,
  B11111
};
byte customChar3[] = {
  B00000,
  B00000,
  B00000,
  B00000,
  B11111,
  B11111,
  B11111,
  B11111
};
byte customChar4[] = {
  B00000,
  B00000,
  B00000,
  B00000,
  B00000,
  B00000,
  B11111,
  B11111
};
byte customChar5[] = {
  B00000,
  B00000,
  B00000,
  B00000,
  B00000,
  B00000,
  B00000,
  B00000
};
lcd.begin(16,2);
  lcd.createChar(1, customChar1);
  lcd.createChar(2, customChar2);
  lcd.createChar(3, customChar3);
  lcd.createChar(4, customChar4);
  lcd.createChar(5, customChar5);
  i= random(0,15);
  lcd.setCursor(4,0);
  
  lcd.setCursor(0,1);
  
  
  lcd.clear();
  
  lcd.setCursor(i,0);
    lcd.write(1);
    lcd.setCursor(i,1);
    lcd.write(1);
    
    lcd.setCursor(i+1,0);
    lcd.write(2);
    lcd.setCursor(i+1,1);
    lcd.write(1);

    lcd.setCursor(i-1,0);
    lcd.write(2);
    lcd.setCursor(i-1,1);
    lcd.write(1);

    lcd.setCursor(i+2,0);
    lcd.write(3);
    lcd.setCursor(i+2,1);
    lcd.write(1);

    lcd.setCursor(i-2,0);
    lcd.write(3);
    lcd.setCursor(i-2,1);
    lcd.write(1);


    lcd.setCursor(i+3,0);
    lcd.write(4);
    lcd.setCursor(i+3,1);
    lcd.write(1);

    lcd.setCursor(i-3,0);
    lcd.write(4);
    lcd.setCursor(i-3,1);
    lcd.write(1);

    lcd.setCursor(i+4,0);
    lcd.write(5);
    lcd.setCursor(i+4,1);
    lcd.write(1);

    lcd.setCursor(i-4,0);
    lcd.write(5);
    lcd.setCursor(i-4,1);
    lcd.write(1);


   
    lcd.setCursor(i+5,1);
    lcd.write(1);

    lcd.setCursor(i-5,1);
    lcd.write(1);


    lcd.setCursor(i+6,1);
    lcd.write(2);

    lcd.setCursor(i-6,1);
    lcd.write(2);

    lcd.setCursor(i+7,1);
    lcd.write(3);

   lcd.setCursor(i-7,1);
   lcd.write(3);
   delay(50);
   lcd.clear();
   i++;
   if(i==21)
   i=-7;
   
  }
