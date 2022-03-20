
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
int wai = -1; //I forgot what WAI stood for, but basically counts what index the counter is at, if the string was a list or smth
//-1 = at start
//0 to t1.length()-1 = data
//t1.length = at end
String t0 = "1.00 0.00 0.00 0.00";
String t1 = "1.00 0.00 0.00 0.00"; //will be changed to actual data in code.
String t2 = "180.00 180.00 180.00 0.00";
String t3 = "100.00 0.00 -4.00 0.07";
String t4 = "thisisbaddatalmaothisshouldnotwork";


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
          //accepting a new string of data
          t1.toCharArray(Buf,t1.length());
          
        }
        //regular code -> bytewise.
        if(t1.length()>18 && t1.length()<33){
        
        
        
        
       
   
        //detecting which byte the data reading is on the string.
        Serial.print(wai);
        if(wai==t1.length()){x = 'e'; wai = -2; }/*t1 = "wqieuroqwueyroqwueyroiweuqyrioqwueyrioqweuryoiqweuryoiqweurywq";}*/ //end data byte, -2 + 1 = -1, which accepts data.
        else{
          if(wai == -1){x = 's';} //start byte
          
          else{
            x = t1[wai];} //actual data byte
        }}
        
        Slavesend=x;        
        if(x==laste && x == (int) 'e'){
          laste = x;
          //"bad" data byte
          x = 'b'; //"if there was an end byte show that there is no data" 
        }
        if(onset==1){
          //"onset" byte (to avoid data offsets with actual bytes.
          x = 'o';
          wai--;
          onset = 0;
        }
        laste = x; //"when was the last e" 
           
        SPDR = Slavesend;  
        SPDR = x;//Sends the x value to master via SPDR 
        wai++;
        
        }
        delay(250);
        
        
 
}
}
