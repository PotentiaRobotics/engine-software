char mystr[40]; //Initialized variable to store recieved data

void setup() {
  // Begin the Serial at 9600 Baud
  Serial3.begin(115200);
  Serial.begin(115200);
}

void loop() {
  Serial3.readBytes(mystr,40); //Read the serial data and store in var
  if(mystr!=""){
  Serial.println(mystr); //Print data on Serial Monitor
  }
  int x = mystr[0];
  Serial.println(x);
 //   Serial.println("LOLYES");
}
