#include <SR04.h>
//PID constants
double kp = 2;
double ki = 5;
double kd = 1;

unsigned long currentTime, previousTime;
double elapsedTime;
double error;
double lastError;
double input, output, setPoint;
double cumError, rateError;
double Setpoint = 100;
long dist;
SR04 sr04 = SR04(2,3);

void setup(){
        setPoint = 0;
        Serial.begin(115200);//set point at zero degrees
}    

void loop(){
        dist = sr04.Distance();                //read from rotary encoder connected to A0
        output = computePID(input);
        delay(100);
        Serial.println("Read: "+String(dist)+", Move: "+String(output));

}

double computePID(double inp){     
        currentTime = millis();                //get current time
        elapsedTime = (double)(currentTime - previousTime);        //compute time elapsed from previous computation
        
        error = Setpoint - inp;                                // determine error
        cumError += error * elapsedTime;                // compute integral
        rateError = (error - lastError)/elapsedTime;   // compute derivative

        double out = kp*error + ki*cumError + kd*rateError;                //PID output               

        lastError = error;                                //remember current error
        previousTime = currentTime;                        //remember current time

        return out;                                        //have function return the PID output
}
