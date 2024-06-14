#include <SoftwareSerial.h>

SoftwareSerial mySerial(10, 11); // RX, TX

void setup() {
  Serial.begin(9600);
  mySerial.begin(9600);

}

void loop() {

  String data = mySerial.readStringUntil('\n');
  Serial.println(data);

}