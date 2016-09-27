#include <Servo.h>

Servo servo1;
Servo servo2;
// These constants won't change.  They're used to give names
// to the pins used:
const int analogInPin = A5;  // Analog input pin that the potentiometer is attached to
const int analogOutPin = 9; // Analog output pin that the LED is attached to
const int phi = 30;
const int ang1 = 90+phi;
const int ang2 = 25;

int serv1ang = 0;
int serv2ang = 0;
int sensorValue = 0;        // value read from the pot
int outputValue = 0;        // value output to the PWM (analog out)

int buttonstate;
int prevbuttonstate = 0;

void setup() {
  // Push Button
  pinMode(7,INPUT);
  // initialize serial communications at 9600 bps:
  Serial.begin(9600);
  servo1.attach(9);
  servo2.attach(10);
}

void startmeasurement() {
  Serial.println("0,0,0");
  for (serv1ang=90-phi; serv1ang<=ang1; serv1ang+=10){
    servo1.write(serv1ang);
    for (serv2ang=90; serv2ang>=ang2; serv2ang-=5){
      servo2.write(serv2ang);
      // read the analog in value:
      sensorValue = analogRead(analogInPin);
      // map it to the range of the analog out:
      outputValue = map(sensorValue, 0, 1023, 0, 255);
      Serial.print(serv1ang-90);
      Serial.print(",");
      Serial.print(90-serv2ang);
      Serial.print(",");
      Serial.println(outputValue);
      delay(100);
    }
    servo2.write(90);
    delay(1000);
  }
  Serial.println("-1,-1,-1");
}

void loop() {
  // change the analog out value:
  buttonstate = digitalRead(7);
  servo1.write(90);
  servo2.write(90);
//  Serial.print(buttonstate);
  if (prevbuttonstate ==1 && buttonstate ==0){
      startmeasurement();
  }
  prevbuttonstate = buttonstate;
}

