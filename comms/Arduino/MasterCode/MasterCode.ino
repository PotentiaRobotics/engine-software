  /* data is read as:
 *  s + (id) + (read1) + ! + (read2) + @ + (read3) + # + (read4) + e
 *  ex. sa1.00!0.00@0.00#-0.10e
 */
char incomingByte = ""; // for incoming serial data
String incomingBytes = "";
char incomingByte2 = ""; // for incoming serial data
String incomingBytes2 = "";


int readPls = 0;
void setup() {
  Serial3.begin(115200);Serial2.begin(115200);Serial.begin(115200); // opens serial port, sets data rate to 9600 bps
  delay(8000); //8 second delay to wait for RPi to run, avoids port busy error on RPi. 
}

void loop() {
  
  // send data only when you receive data:
  if (Serial3.available() > 0) {
    // read the incoming byte:
    incomingByte = Serial3.read();
    
    // say what you got:
    Serial3.println(incomingByte);
    if(incomingByte == 's'){
      readPls = 1;
    }
    if(incomingByte == 'e'){
      readPls = 0;
      incomingBytes.concat(incomingByte);
      Serial.println(incomingBytes);
      incomingBytes = "";
    }
    if(readPls == 1){
      incomingBytes.concat(incomingByte);
    }
  }
    if (Serial2.available() > 0) {
    // read the incoming byte:
    incomingByte2 = Serial2.read();
    
    // say what you got:
    Serial2.println(incomingByte2);
    if(incomingByte2 == 's'){
      readPls = 1;
    }
    if(incomingByte2 == 'e'){
      readPls = 0;
      incomingBytes2.concat(incomingByte2);
      Serial.println(incomingBytes2);
      incomingBytes2 = "";
    }
    if(readPls == 1){
      incomingBytes2.concat(incomingByte2);
    }
  }
}
