char mystr[40] = "-180.00 -180.00 -180.00 -180.00"; //String data
int x = 0;
void setup() {
  // Begin the Serial at 9600 Baud
  Serial3.begin(9600);
}

void loop() {
  //char buf[5];
  //String(x).toCharArray(buf,5);
  Serial3.write(mystr,40); //Write the serial data
  delay(100);
}
