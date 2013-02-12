int ledPin = 11;  // choose the pin for the LED  
int val = 0;      // variable for reading the pin status  
char msg = '  ';   // variable to hold data from serial 


void setup() {  
  Serial.begin(9600);  
}  

void loop(){  
  // While data is sent over serial assign it to the msg  
  while (Serial.available()>0){  
    msg=Serial.read();  
    analogWrite(ledPin, msg); 
}  
}

