#include <Servo.h> 

Servo myservo;

void setup() {
  // put your setup code here, to run once:
  myservo.attach(9);
  Serial.begin(9600);
}

void loop() {
  // put your main code here, to run repeatedly:
  for(int i=1500; i<2100; i+=100)
  {
    myservo.writeMicroseconds(i);
    delay(3000);
    Serial.println(i);
  }
}
