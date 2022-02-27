
//Slave Arduino Code:
//SPI SLAVE (ARDUINO)
//SPI COMMUNICATION BETWEEN TWO ARDUINO 
//CIRCUIT DIGEST
//Pramoth.T
int laste = 0;
#include<SPI.h>
#define LEDpin 7
#define buttonpin 2
volatile boolean received;
volatile byte Slavereceived,Slavesend;
int buttonvalue;
int x = 65;
int wai = -1;
String t1 = "1.00 0.00 0.00 0.00";
char Buf[32]; 
int onset = 1;
void setup()

{
  Serial.begin(115200);
  
  pinMode(buttonpin,INPUT);               // Setting pin 2 as INPUT
  pinMode(LEDpin,OUTPUT);                 // Setting pin 7 as OUTPUT
  pinMode(MISO,OUTPUT);                   //Sets MISO as OUTPUT (Have to Send data to Master IN 

  SPCR |= _BV(SPE);                       //Turn on SPI in Slave Mode
  received = false;

  SPI.attachInterrupt();                  //Interuupt ON is set for SPI commnucation
  
}

ISR (SPI_STC_vect)                        //Inerrrput routine function 
{
  Slavereceived = SPDR;         // Value received from master if store in variable slavereceived
  received = true;                        //Sets received as True 
}

void loop()
{ 
  if(received)                            //Logic to SET LED ON OR OFF depending upon the value recerived from master
   {
      if (Slavereceived==8) 
      {
        if(wai==-1 && t1.length()>18 && t1.length()<33){
          t1.toCharArray(Buf,t1.length());
        }
        if(t1.length()>18 && t1.length()<33){
        
        
        
        
       
   
      
        Serial.print(wai);
        if(wai==t1.length()){x = 'e'; wai = -2; t1 = "wqieuroqwueyroqwueyroiweuqyrioqwueyrioqweuryoiqweuryoiqweurywq";}
        else{
          if(wai == -1){x = 's';}
          
          else{
            x = t1[wai];}
        }}
        
        Slavesend=x;        
        if(x==laste && x == (int) 'e'){
          laste = x;

          x = 'b';
        }
        if(onset==1){
          x = 'o';
          wai--;
          onset = 0;
        }
        laste = x;
           
        SPDR = Slavesend;  
        SPDR = x;//Sends the x value to master via SPDR 
        wai++;
        
        }
        delay(250);
        
        
 
}
}
