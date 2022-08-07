String myStr = "sc1.00!0.01@0.02#-0.10e";
String myStr2 = "sd1.00!0.03@0.10#-0.05e";
void setup() {
  // put your setup code here, to run once:
  Serial3.begin(115200);
}

void loop() {
  // put your main code here, to run repeatedly:
  Serial3.print(myStr);
  Serial3.print(myStr2);
  delay(25);
}
