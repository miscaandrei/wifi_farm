/*
Este fitxer fa que el arduino escolti el serial 9600 (USB natiu) per veure les commandes que l'hi arriba i que ha d'executar.
Aquet fitxer conte la funcio que mostra l'inicialitzacio del servidor, l'execucio de la commanda en curs i que hi ha connexio entre servidor i Arduino.

*/
//Definicio de leds
int ledPinA1 = 12;  // led bicolor A (vermell), en la placa representat per un fill verd
int ledPinA2 = 11;  // led bicolor A (groc), en la placa representat per un fill verd

int ledPinB1 = 8;  // led bicolor B (groc), en la placa representat per un fill blau
int ledPinB2 = 7;  // led bicolor B (verd), en la placa representat per un fill blau

int ledPinC1 = 5;  // led RGB (RED), en la placa representat per un fill groc
int ledPinC2 = 3;  // led RGB (BLUE), en la placa representat per un fill blanc
int ledPinC3 = 4;  // led RGB (GREEN), en la placa representat per un fill taronja
  

int val = 0;      // variable for reading the pin status  
char msg = '  ';   // variable to hold data from serial 


void setup() {  
  pinMode(ledPinA1, OUTPUT);      // declare LED as output  
  pinMode(ledPinA2, OUTPUT);
  pinMode(ledPinB1, OUTPUT);
  pinMode(ledPinB2, OUTPUT);
  pinMode(ledPinC1, OUTPUT);
  pinMode(ledPinC2, OUTPUT);
  pinMode(ledPinC3, OUTPUT);
            
  Serial.begin(9600);  
  //Serial.print("Program Initiated\n");  
}  


void error(int x){
  if (x==1){
    for (int i=0; i <= 255; i++){
          digitalWrite(ledPinA1, HIGH);
          delay(500);
          digitalWrite(ledPinA1, LOW);
      }
  }
  else if (x==0){
    digitalWrite(ledPinA1, LOW);
  }
}


void warningOn(){
  digitalWrite(ledPinA2, HIGH);
}

void warningOff(){
  digitalWrite(ledPinA2, LOW);
}

void conectat(){
  digitalWrite(ledPinB1, LOW);
  digitalWrite(ledPinB2, HIGH);
}

void desconectat(){
  digitalWrite(ledPinB1, HIGH);
  digitalWrite(ledPinB2, LOW);
}


void RGB(int r, int g, int b){
  if (r==1){
    digitalWrite(ledPinC1, HIGH);
  }
  
  else if(r==0){
    digitalWrite(ledPinC1, LOW);
  }
  
  if (b==1){
    digitalWrite(ledPinC2, HIGH);
  }
  
  else if (b==0){
    digitalWrite(ledPinC2, LOW);
  }
  
  if (g==1){
    digitalWrite(ledPinC3, HIGH);
  }
  
  else if (g==0){
    digitalWrite(ledPinC3, LOW);
  }
  
  else{
   error(1);
  }
}


void loop(){  

  //Desconectat
  desconectat();
  delay(3000);
  
  //Conectat
  conectat();
  delay(3000);
 

  //RGB Vermell
  RGB(1,0,0);
  delay(3000);

  //RGB Verd
  RGB(0,1,0);
  delay(3000);

    //RGB Blau
  RGB(0,0,1);
  delay(3000);
  
  
  // RGB Blau + Verd
  RGB(0,1,1);
  delay(3000);
  
  // RGB Blau + Vermell
  RGB(1,0,1);
  delay(3000);
  
  // RGB Verd + Vermell
  RGB(1,1,0);
  delay(3000);
  


  // RGB BlANC
  RGB(1,1,1);
  delay(3000);

  //RGB apagat i error on
  RGB(0,0,0);
  RGB(2,2,2);
  delay(50000);
  
  //Error OFF & Warning on
  warningOn();
  delay(10000);
  warningOff();

  delay(100);
  
  
  
  
  // While data is sent over serial assign it to the msg  
  /*while (Serial.available()>0){  
    msg=Serial.read();  
  }  

  // Turn LED on/off if we recieve 'Y'/'N' over serial  
  if (msg=='I') {
    digitalWrite(ledPin, HIGH);  // turn LED ON  
    Serial.print("LED --ON--\n");  
    msg=' ';  
  } 
  else if (msg=='O') {  
    digitalWrite(ledPin, LOW); // turn LED OFF  
    Serial.print("LED --OFF--\n");  
    msg=' ';
  } 
  else {

  } */
  
  
}

