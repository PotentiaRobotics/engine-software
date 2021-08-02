
#include <Wire.h>

void setup() {
  Wire.begin();        // join i2c bus (address optional for master)
  Serial.begin(115200);  // start serial for output
}

void loop() {
  Wire.requestFrom(8, 26);    // request 100 bytes from slave device #8
  byte index = 0;
  String data = "";
  while (Wire.available()) { // slave may send less than requested
    char c = Wire.read(); // receive a byte as character
    //Serial.print(c);
    data += c;
  }
  Serial.println("Rotation Data: " + data);
  Serial.println();

  delay(10);
}
