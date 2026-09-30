#include <AFMotor.h>

AF_DCMotor motor1(1);  // Claw
AF_DCMotor motor2(2);  // Arm

void setup() {
  Serial.begin(9600);

  motor1.setSpeed(200);
  motor2.setSpeed(200);

  motor1.run(RELEASE);
  motor2.run(RELEASE);
}

void loop() {
  if (Serial.available() > 0) {
    char command = Serial.read();

    if (command == 'U') {
      motor2.run(FORWARD);
      delay(5000);
      motor2.run(RELEASE);
    }

    if (command == 'D') {
      motor2.run(BACKWARD);
      delay(5000);
      motor2.run(RELEASE);
    }

    if (command == 'O') {
      motor1.run(BACKWARD);
      delay(3000);
      motor1.run(RELEASE);
    }

    if (command == 'C') {
      motor1.run(FORWARD);
      delay(3000);
      motor1.run(RELEASE);
    }
  }
}
