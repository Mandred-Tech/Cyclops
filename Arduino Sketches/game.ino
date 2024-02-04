//game initialization on lcd screen
void game(){

//anim
  lcd.setCursor(px,py);
lcd.print(" ");
lcd.setCursor(X,Y);
lcd.write(2);  //pac2
delay(250);
lcd.setCursor(X,Y);
lcd.write(1);  //pac1
delay(250);
px = X;
py = Y;
X++;
if(X>15 && Y == 0)
{
X = 0;
Y = 1;
}
else if(X>15 && Y == 1)
{
X = 0;
Y = 0;

//fill
lcd.setCursor(0,0);
lcd.write(1); //pac1
for(int j=0;j<7;j++)
{
lcd.print(" ");
lcd.write(3); //pill
}
lcd.setCursor(0,1);
lcd.write(3); //pill
for(int j=0;j<7;j++)
{
lcd.print(" ");
lcd.write(3); //pill
}
}

 
  
  

  
  }
