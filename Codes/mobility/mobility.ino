int in_2 =11;
int in_1=10;
int pwm =A2;
int in_3=9;
int in_4=6;
int sec=A3;

#define joyX A0
#define joyY A1

int r = 10;

void setup() {
Serial.begin(9600);
pinMode(pwm,OUTPUT) ;   
pinMode(in_1,OUTPUT) ;  
pinMode(in_2,OUTPUT) ;
pinMode(in_3,OUTPUT) ;
pinMode(in_4,OUTPUT) ;
pinMode(sec,OUTPUT) ;
}

void loop() {

  if(Serial.available()){      
    r = Serial.read();  
    Serial.println(r);
    int xv = analogRead(joyX);
 int yv = analogRead(joyY);


   Serial.print("X Value :  ");
    Serial.print(xv);
   Serial.print("Y Value :  ");
    Serial.println(yv);
    
 
 analogWrite(pwm,225); 
 analogWrite(sec,225); 
if (xv > 950 && yv < 600 || r==3){
if(r==3)
{
digitalWrite(in_1,LOW) ;
digitalWrite(in_2,HIGH) ;
digitalWrite(in_3,LOW) ;
digitalWrite(in_4,HIGH) ;
delay(2000);
}
digitalWrite(in_1,LOW) ;
digitalWrite(in_2,HIGH) ;     
digitalWrite(in_3,LOW) ;
digitalWrite(in_4,HIGH) ;
}

else if( xv <= 20 && yv < 600|| r==4)
{ 
  if(r==4)
  { 
digitalWrite(in_1,HIGH) ;
digitalWrite(in_2,LOW) ;
digitalWrite(in_3,HIGH) ;
digitalWrite(in_4,LOW) ;
delay(2000);
  }
  digitalWrite(in_1,HIGH) ;
digitalWrite(in_2,LOW) ;
digitalWrite(in_3,HIGH) ;
digitalWrite(in_4,LOW) ;
}


else if (xv <= 600 && yv >= 950 || r==1){
if(r==1)
{
digitalWrite(in_1,HIGH) ;
digitalWrite(in_2,LOW) ;
digitalWrite(in_3,LOW) ;
digitalWrite(in_4,HIGH) ;
delay(2000);
}

digitalWrite(in_1,HIGH) ;
digitalWrite(in_2,LOW)  ;
digitalWrite(in_3,LOW) ;
digitalWrite(in_4,HIGH) ;
}
else if(xv <= 600 && yv <=200 || r==2){
if(r==2)
{
digitalWrite(in_1,LOW) ;
digitalWrite(in_2,HIGH) ;
digitalWrite(in_3,HIGH) ;
digitalWrite(in_4,LOW) ;
delay(2000);
}

digitalWrite(in_1,LOW) ;
digitalWrite(in_2,HIGH) ;
digitalWrite(in_3,HIGH) ;
digitalWrite(in_4,LOW) ;
}
else{
if(r==5)
{
      digitalWrite(in_1,LOW) ;
digitalWrite(in_2,LOW) ;
digitalWrite(in_3,LOW) ;
digitalWrite(in_4,LOW) ;
    }
digitalWrite(in_1,LOW) ;
digitalWrite(in_2,LOW) ;
digitalWrite(in_3,LOW) ;
digitalWrite(in_4,LOW) ;
  }
}
int xv = analogRead(joyX);
 int yv = analogRead(joyY);


   Serial.print("X Value :  ");
    Serial.print(xv);
   Serial.print("Y Value :  ");
    Serial.println(yv);
    
 
 analogWrite(pwm,225); 
 analogWrite(sec,225); 
if (xv > 950 && yv < 600 || r==3){
if(r==3)
{
digitalWrite(in_1,LOW) ;
digitalWrite(in_2,HIGH) ;
digitalWrite(in_3,LOW) ;
digitalWrite(in_4,HIGH) ;
delay(2000);
}
digitalWrite(in_1,LOW) ;
digitalWrite(in_2,HIGH) ;     
digitalWrite(in_3,LOW) ;
digitalWrite(in_4,HIGH) ;
}

else if( xv <= 20 && yv < 600|| r==4)
{ 
  if(r==4)
  { 
digitalWrite(in_1,HIGH) ;
digitalWrite(in_2,LOW) ;
digitalWrite(in_3,HIGH) ;
digitalWrite(in_4,LOW) ;
delay(2000);
  }
  digitalWrite(in_1,HIGH) ;
digitalWrite(in_2,LOW) ;
digitalWrite(in_3,HIGH) ;
digitalWrite(in_4,LOW) ;
}


else if (xv <= 600 && yv >= 950 || r==1){
if(r==1)
{
digitalWrite(in_1,HIGH) ;
digitalWrite(in_2,LOW) ;
digitalWrite(in_3,LOW) ;
digitalWrite(in_4,HIGH) ;
delay(2000);
}

digitalWrite(in_1,HIGH) ;
digitalWrite(in_2,LOW)  ;
digitalWrite(in_3,LOW) ;
digitalWrite(in_4,HIGH) ;
}
else if(xv <= 600 && yv <=200 || r==2){
if(r==2)
{
digitalWrite(in_1,LOW) ;
digitalWrite(in_2,HIGH) ;
digitalWrite(in_3,HIGH) ;
digitalWrite(in_4,LOW) ;
delay(2000);
}

digitalWrite(in_1,LOW) ;
digitalWrite(in_2,HIGH) ;
digitalWrite(in_3,HIGH) ;
digitalWrite(in_4,LOW) ;
}
else{
if(r==5)
{
      digitalWrite(in_1,LOW) ;
digitalWrite(in_2,LOW) ;
digitalWrite(in_3,LOW) ;
digitalWrite(in_4,LOW) ;
    }
digitalWrite(in_1,LOW) ;
digitalWrite(in_2,LOW) ;
digitalWrite(in_3,LOW) ;
digitalWrite(in_4,LOW) ;
  }
  }
