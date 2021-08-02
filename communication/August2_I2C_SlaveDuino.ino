#include <Wire.h>
#include <Adafruit_MPU6050.h>
#include <Adafruit_Sensor.h>

Adafruit_MPU6050 mpu;

String x = "";
String y = "";

volatile int Val; // variable used by the master to sent data to the slave

void setup() {
  Wire.begin(8);                // Slave id #8
  Wire.onRequest(requestEvent); // function to run when asking for data
  //Wire.onReceive(receiveEvent); // what to do when receiving data
  Serial.begin(115200);  // serial for displaying data on your screen

    while (!Serial)
    delay(10); // will pause Zero, Leonardo, etc until serial console opens

  Serial.println("Adafruit MPU6050 test!");

  // Try to initialize!
  if (!mpu.begin()) {
    Serial.println("Failed to find MPU6050 chip");
    while (1) {
      delay(10);
    }
  }
 Serial.println("MPU6050 Found!");

  mpu.setAccelerometerRange(MPU6050_RANGE_8_G);
  Serial.print("Accelerometer range set to: ");
  switch (mpu.getAccelerometerRange()) {
  case MPU6050_RANGE_2_G:
    Serial.println("+-2G");
    break;
  case MPU6050_RANGE_4_G:
    Serial.println("+-4G");
    break;
  case MPU6050_RANGE_8_G:
    Serial.println("+-8G");
    break;
  case MPU6050_RANGE_16_G:
    Serial.println("+-16G");
    break;
  }
  mpu.setGyroRange(MPU6050_RANGE_500_DEG);
  Serial.print("Gyro range set to: ");
  switch (mpu.getGyroRange()) {
  case MPU6050_RANGE_250_DEG:
    Serial.println("+- 250 deg/s");
    break;
  case MPU6050_RANGE_500_DEG:
    Serial.println("+- 500 deg/s");
    break;
  case MPU6050_RANGE_1000_DEG:
    Serial.println("+- 1000 deg/s");
    break;
  case MPU6050_RANGE_2000_DEG:
    Serial.println("+- 2000 deg/s");
    break;
  }

  mpu.setFilterBandwidth(MPU6050_BAND_21_HZ);
  Serial.print("Filter bandwidth set to: ");
  switch (mpu.getFilterBandwidth()) {
  case MPU6050_BAND_260_HZ:
    Serial.println("260 Hz");
    break;
  case MPU6050_BAND_184_HZ:
    Serial.println("184 Hz");
    break;
  case MPU6050_BAND_94_HZ:
    Serial.println("94 Hz");
    break;
  case MPU6050_BAND_44_HZ:
    Serial.println("44 Hz");
    break;
  case MPU6050_BAND_21_HZ:
    Serial.println("21 Hz");
    break;
  case MPU6050_BAND_10_HZ:
    Serial.println("10 Hz");
    break;
  case MPU6050_BAND_5_HZ:
    Serial.println("5 Hz");
    break;
  }

  Serial.println("");
}

void loop() {
      /* Get new sensor events with the readings */
  sensors_event_t a, g, temp;
  mpu.getEvent(&a, &g, &temp);
  x = "";
  y = "";

  /* Print out the values */
  y += "a ";
  y += String(a.acceleration.x, 3);
  y += " ";
  y += String(a.acceleration.y, 3);
  y += " ";
  y += String(a.acceleration.z, 3);
  
  while(y.length() < 27)
  {
  y += " ";
  }
  Serial.println(y.length());
  Serial.println(y);

  x += "g ";
  x += String(g.gyro.x, 3);
  x += " ";
  x += String(g.gyro.y, 3);
  x += " ";
  x += String(g.gyro.z, 3);
  
  while(x.length() < 27)
  {
  x += " ";
  }
  Serial.println(x.length());
  Serial.println(x);
  delay(10);
}
int oscillator = 0;
// function: what to do when asked for data
void requestEvent() {
  
      if(oscillator == 0)
      {
      byte data[27];
      for (byte i=0; i<27; i++) 
      {
        data[i] = (byte) y.charAt(i);
      }
      Wire.write(data, sizeof(data));
      
      oscillator = 1;
      }
      else if(oscillator == 1)
      {
      byte data[27];
      for (byte i=0; i<27; i++) 
      {
        data[i] = (byte) x.charAt(i);
      }
      Wire.write(data, sizeof(data));
      
      oscillator = 0;
      }
      else
      {
      Wire.write("ERROR");
      }
      
      
      
      
}
