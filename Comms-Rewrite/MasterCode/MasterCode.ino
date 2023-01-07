
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
      delay(3);
      if(Serial1.available() > 0){
        //Serial.println("AAAAgot data");
        String data2 = Serial1.readStringUntil('\n');
      
        Serial.println(String(data2));}
      
    }
  }
}
