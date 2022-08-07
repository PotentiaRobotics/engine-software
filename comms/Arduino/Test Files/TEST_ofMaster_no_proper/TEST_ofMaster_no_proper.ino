char incomingByte = ""; // for incoming serial data
String incomingBytes = "";
int readPls = 0;
void setup() {
  Serial3.begin(115200);Serial.begin(115200); // opens serial port, sets data rate to 9600 bps
}

void loop() {
  
  // send data only when you receive data:
  if (Serial3.available() > 0) {
    // read the incoming bytxe:
    incomingByte = Serial3.read();
    
    // say what you got:
    Serial3.println(incomingByte);
   
      incomingBytes.concat(incomingByte);
      Serial.println(incomingByte);
      if(incomingByte == 13){
      incomingBytes = "";}
    
    //if(readPls == 1){
    //}
  }
}
