#include <LiquidCrystal.h>  //Include LCD Library
#include<Servo.h>           //Include Servo Library
#include <dht.h>            // Include Temperature and Humidity Sensor library
#define outPin 10           // Defines pin number to which the sensor is connected
LiquidCrystal lcd(2,3,4,5,6,7); //defining workings for LCD
dht DHT;                      //initialization for Temperature and Humidity Sensor
Servo Servo1;                 //initialization for Servo Motor



//list of variables



String angle_input;           //angle input as string from serial monitor

int flag_game=0;
int count=0;
int X = 0;
int Y = 0;
int px = 0;
int py = 0;
 
 
int a = 0;
String angle;             //String input to the function (angle_servo) as angle taken from serial monitor as string
String emotion;
String emot="";
String status_on;
String txt="";           //String input taken from serial monitor to type text
int func_to_use=-1;
int flag=0;
int servoPin=9;
int y;
int value;
int ledPin = 11;          // the pin that the LED is attached to
int x;
int status = false; 
char text[]="MANDRED TECH";
unsigned int i=0;
int blink_flag=0;



 
//list of variables  

 



void setup() 
   {  
   Servo1.attach(servoPin); //servo attachment to pin 9  
   Serial.begin(9600);     //serial data begin
   lcd.begin(16,2);       //lcd screen begin 
   Servo1.write(120);    //initial servo placement 120 degrees
   }



  

void intro()
  { 
  //prints MANDRED TECH text at initial start up 
  lcd.begin(16,2);
  lcd.setCursor(2, 0);  
  while(text[i]!='\0'){
  lcd.print(text[i]);   
   if(i>=14)
  {
   lcd.command(0x18);
  }
   delay(500);
   i++;
   }   
  }










  void led_control(int onoff)
  {
  //cyclops eye led control
  pinMode(11, OUTPUT);
  if(onoff==1){
    digitalWrite(11,HIGH);
  }
  else
  {
  digitalWrite(11,LOW);
  }  
  }


  
  void led_blink()
  {
  //cyclops eye led blink control
  pinMode(11, OUTPUT);
  digitalWrite(11, LOW);
  delay(200);
  digitalWrite(11, HIGH);
  delay(100);
  digitalWrite(11, LOW);
  delay(200);
  digitalWrite(11, HIGH);
  delay(10);
  buzz();  
  }




  
  


  
void angle_servo(String angle)
  {
  //random angle string input, converts into integer and rotates servo accordingly 
  Servo1.write(angle.toInt());
  delay(1000);  
  }

  


  

void print_text(String rx_str)
  {
  //prints any text on lcd screen 
  String a1=rx_str.substring(0,16);
  String a2=rx_str.substring(16,32);
  lcd.begin(16,2);
  lcd.setCursor(0,0);
  lcd.setCursor(0,0);
  lcd.print(a1);
  lcd.setCursor(0,1);
  lcd.print(a2);
  delay(500);
  lcd.clear();  
  }

  




  




void rotate1()
  {  
  //rotates the servo (head movement)
  Servo1.attach(servoPin);  
  for(int measure=120;measure>=60;measure--)
  {
    Servo1.write(measure);
    delay(10);    
  }
  for(int measure=60;measure<=120;measure++){
  Servo1.write(measure);
  delay(10);     
  }
  for(int measure=120;measure<=180;measure++){
  Servo1.write(measure);
  delay(10);     
  }
  for(int measure=180;measure>=120;measure--){
  Servo1.write(measure);
  delay(10);     
   }
   }



void rotate2()
  {  
  //rotates the servo (head movement)
  Servo1.attach(servoPin);  
  for(int measure=120;measure>=60;measure--)
  {
    Servo1.write(measure);
    delay(20);    
  }
  for(int measure=60;measure<=120;measure++){
  Servo1.write(measure);
  delay(20);     
  }
  for(int measure=120;measure<=180;measure++){
  Servo1.write(measure);
  delay(20);     
  }
  for(int measure=180;measure>=120;measure--){
  Servo1.write(measure);
  delay(20);     
   }
   }











  

void get_dht()
  {
  //Humidity and Temperature Function
  delay(1000);
  lcd.clear();
  int readData = DHT.read11(outPin);
  float t = DHT.temperature;        // Read temperature
  float h = DHT.humidity;           // Read humidity
  lcd.setCursor(0,0);
  lcd.print("Temp(C):");
  lcd.setCursor(9,0);
  lcd.print(t);
  lcd.setCursor(0,1);
  lcd.print("Humidity(%):");
  lcd.setCursor(12,1);
  lcd.print(h);
  delay(100); // wait two seconds
  }


  
void listening()
{
    lcd.write("Listening");
    delay(200);
    lcd.clear();
    lcd.write("Listening.");
    delay(200); 
    lcd.clear();
    lcd.write("Listening..");
    delay(200);
    lcd.clear();      
    lcd.write("Listening...");
    delay(200);
    lcd.clear();
    lcd.write("Listening....");
    delay(200);
    lcd.clear();      
    lcd.write("Listening.....");  
    lcd.clear();    
}



void loop() 
{     

    
    //looks for the serial function input 
    if (Serial.available()>0)
    {
      emotion=Serial.readStringUntil('\r');
    } 

    //declaration of different function parameters
    if(emotion=="on")
    {
      lcd.begin(16,2);
      intro();
      intro_tune(); 
      led_control(1);
             
    }     
    else if(emotion=="sine")
    {
      func_to_use=1;
    }
    else if(emotion=="happy")
    {
      func_to_use=2;
    }
    else if(emotion=="sad")
    {
      func_to_use=3;
    }
    else if(emotion=="angry")
    {
      func_to_use=4;
    }
    else if(emotion=="rotate1")
    {
      led_control(1);
      lcd.clear();
      rotate1();
      logo();      
    }
    else if(emotion=="rotate2")
    {
      led_control(1);
      lcd.clear();
      rotate2();
      logo();
    }
    else if(emotion=="temph")
    {
      func_to_use=5;
    }
    else if(emotion.indexOf("#")>=0)
    {
      txt=emotion.substring(1,emotion.length());
      func_to_use=6;
    }      
    else if(emotion=="camera")
    {
      func_to_use=7;
      
    }
    else if(emotion=="clock")
    {
        func_to_use=8;
        
    }
    else if(emotion=="game")
    {
           X = 0;
           Y = 0;
           px = 0;
           py = 0;
          func_to_use=9;          
    }
    else if(emotion.indexOf("@")>=0)
    {
      angle_input=emotion.substring(1,emotion.length());
      func_to_use=10;
      
    } 
    else if(emotion=="exercise")
    {
        func_to_use=11;
    }
    else if(emotion=="logo")
    {
          func_to_use=12;
          
    } 
    else if(emotion=="led_blink")
    {
       
      
        lcd.clear();
        led_blink();      
        listening();
        func_to_use=13;
          
      } 
      else if(emotion=="off")
    {
      func_to_use=-1;
      led_control(0);
      lcd.clear();
    }
    




    //loopings for the functions   
       
    if (func_to_use==1)
    {
      led_control(1);
      sinewave2();
    }
    else if (func_to_use==2)
    {
      led_control(1);
      happy();
    }
    else if (func_to_use==3)
    {
      led_control(1);
      sad();
    }
    else if (func_to_use==4)
    {
      led_control(1);
      angry();
    }
    else if (func_to_use==5)
    {
      led_control(1);
      get_dht();
    }
    else if (func_to_use==6)
    {
      led_control(1);
      print_text(txt);        
    }
    else if (func_to_use==7)
    {
      led_control(1);
      camera();      
    }
    else if (func_to_use==8)
    {
      led_control(1);
      clock1();
      clock2();
      clock3();
      clock4();
      clock5();
      clock6();
      clock7();        
    }
    else if (func_to_use==9)
    {  
      led_control(1);  
      init_game(); 
      if(flag_game==0)
      {
      //pac1
      lcd.setCursor(0,0);
      lcd.write(1); 
      }
        game();
        count++;
        if(count!=32)
        {           
           flag_game=1;   
        }
        else
        {
          flag_game=0;
          count=0;
        }            
        Serial.println(func_to_use);                     
        Serial.println(count);
        Serial.println(flag_game);                
     }          
    else if(func_to_use==10)
    {
      led_control(1); 
      angle_servo(angle_input);
      logo();    
    }
    else if(func_to_use==11)
    {
      led_control(1);
      exercise();            
    }
    else if(func_to_use==12)
    {
      led_control(1);
      logo();
    }
    else if(func_to_use==13)
    {
      led_control(1);
      listening();
      
      
    }



    


  
}
