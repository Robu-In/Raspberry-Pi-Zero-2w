#include <SoftwareSerial.h>
SoftwareSerial mySerial(10, 11); // RX, TX

void setup() {
  mySerial.begin(9600);
}

void loop() {

  serial_send(1, 2, 3);
  delay(1000);
  
}

void serial_send(uint8_t x, uint8_t y, uint8_t z){
  Serial.print("A = ");
  Serial.print(x);
  Serial.print(" B = ");
  Serial.print(y);
  Serial.print(" C = ");
  Serial.println(z);
}