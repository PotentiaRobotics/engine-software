String myStr = "-179.00 90.00 0.00";
String myStr2 = "45.00 30.00 -30.00";
int i=0;
void setup() {
  // put your setup code here, to run once:
  Serial1.begin(9600);
  Serial.begin(9600);
}

void loop() {
  
  // put your main code here, to run repeatedly:
  if(Serial1.available() > 0) {
    i+=1;
    String data = Serial1.readStringUntil('\n');
    Serial.print(data.charAt(0));
    
    if(data.charAt(0)=='D'){ //this took forever to resolve, just do first char comparisions for now
      Serial.println("true");
      Serial1.print(myStr+"_");
      Serial1.println(myStr2+i);
        
    }
  }
    
}
