
#include <Wire.h>

void setup() {
  Wire.begin();        // join i2c bus (address optional for master)
  Serial.begin(115200);  // start serial for output
}

void loop() {
  Wire.requestFrom(8, 27);    // request 27 bytes from slave device #8
  String data = "";
  while (Wire.available()) { // slave may send less than requested
    char c = Wire.read(); // receive a byte as character
    //Serial.print(c);
    data += c;
  }
  if(data.charAt(0) == 'a')
  {
  Serial.println("Acceleration Data: " + data.substring(1) + " m/s^2");
  }
  else
  {
  Serial.println("Gyroscope Data:    " + data.substring(1) + " rad/s");
  }

  delay(10);
}
