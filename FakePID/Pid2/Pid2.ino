/*
sketch belongs to this video: https://youtu.be/crw0Hcc67RY
write by Moz for YouTube changel logMaker360
4-12-2017
*/

#include <PID_v1.h>
#include <SR04.h>
double Setpoint ; // will be the desired value
double Input; // photo sensor
double Output ; //LED
//PID parameters
double Kp=0, Ki=10, Kd=0; 
long dist;
SR04 sr04 = SR04(2,3);
 
//create PID instance 
PID myPID(&Input, &Output, &Setpoint, Kp, Ki, Kd, DIRECT);
 
void setup()
{
  
  Serial.begin(9600);   
  //Hardcode the brigdness value
  Setpoint = 100;
  //Turn the PID on
  myPID.SetMode(AUTOMATIC);
  //Adjust PID values
  myPID.SetTunings(Kp, Ki, Kd);
}
 
void loop()
{
  //Read the value from the light sensor. Analog input : 0 to 1024. We map is to a value from 0 to 255 as it's used for our PWM function.
  Input = sr04.Distance();  // photo senor is set on analog pin 5
  //PID calculation
  myPID.Compute();
  //Write the output as calculated by the PID function
  analogWrite(3,Output); //LED is set to digital 3 this is a pwm pin. 
  //Send data by serial for plotting 
  //Serial.print(Input);
  //Serial.print(" ");
  Serial.println(Output);
  //Serial.print(" ");  
  //Serial.println(Setpoint);
//  delay(100); 
}
