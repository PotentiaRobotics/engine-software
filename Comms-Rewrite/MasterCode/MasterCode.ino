/*
Program: Receive Strings From Raspberry Pi
File: receive_string_from_raspberrypi.ino
Description: Receive strings from a Raspberry Pi
Author: Addison Sears-Collins
Website: https://automaticaddison.com
Date: July 5, 2020
*/
int i=0;
void setup(){
   
  // Set the baud rate  
  Serial.begin(9600);
  Serial1.begin(9600);
   
}
 
void loop(){
  //Serial1.println("hi");
  if(Serial.available() > 0) {
    String data = Serial.readStringUntil('\n');
    //Serial.println("got req");
    if(data=="Data"){
      Serial1.println("Data");
      //Serial.println("req data from slave");
      delay(10);
      if(Serial1.available() > 0){
        Serial.println("AAAAgot data");
        String data2 = Serial1.readStringUntil('\n');
      
        Serial.print("Hi Raspberry Pi! You sent me: ");
        Serial.println(String(data2));}
      
    }
  }
}
