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
   
}
 
void loop(){
 
  if(Serial.available() > 0) {
    String data = Serial.readStringUntil('\n');
    if(data=="Data"){
    Serial.print("Hi Raspberry Pi! You sent me: ");
    Serial.println(String(i));
    i+=1;}
  }
  
}
