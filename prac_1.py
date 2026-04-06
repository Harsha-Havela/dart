//raindrop sensor
#define analogpin = A0
#define buzzer 9

void setup() {
	pinMode(analogpin,  INPUT);
	pinMode(buzzer, OUTPUT);
	serial.begin(9600);
}

void loop() {
	int sensorRead= analogRead(analogpin);
	Serial.println(sensorRead);
	
	if (sensorRead < 102){
		digitalwrite(buzzer,HIGH);
	}else{
		digitalwrite(buzzer,LOW);
	}

	delay(1000);
}

//soil moisture sensor
#define ledPin 6
#define sensorPin A0

void setup() {
  Serial.begin(9600);
  pinMode(ledPin, OUTPUT);
  digitalWrite(ledPin, LOW);
}

void loop() {
  Serial.print("Analog output: ");
  Serial.println(readSensor());
  delay(500);

}

int readSensor() {
  int sensorValue = analogRead(sensorPin);  
  int outputValue = map(sensorValue, 0, 1023, 255, 0); 
  analogWrite(ledPin, outputValue); 
  return outputValue;          
}

//PIR sensor
const int PIR_SENSOR_OUTPUT_PIN = 4;	
int warm_up;

void setup() {
  pinMode(PIR_SENSOR_OUTPUT_PIN, INPUT);
  Serial.begin(9600);	
  delay(20000);	
}

void loop() {
  int sensor_output;
  sensor_output = digitalRead(PIR_SENSOR_OUTPUT_PIN);
  if( sensor_output == LOW )
  {
    if( warm_up == 1 )
     {
      Serial.print("Warming Up\n\n");
      warm_up = 0;
      delay(2000);
    }
    Serial.print("No object in sight\n\n");
    delay(1000);
  }
  else
  {
    Serial.print("Object detected\n\n");    
    warm_up = 1;
    delay(1000);
  }  
}

//ultrasonic sensor
const int buzzer = 8;
const int trig_pin = 9;
const int echo_pin = 10;
float timing = 0.0;
float distance = 0.0;

void setup()
{
  pinMode(echo_pin, INPUT);
  pinMode(trig_pin, OUTPUT);
  pinMode(buzzer, OUTPUT);
  
  digitalWrite(trig_pin, LOW);
  digitalWrite(buzzer, LOW);
    
  Serial.begin(9600);
}

void loop()
{
  digitalWrite(trig_pin, LOW);
  delay(2);
  
  digitalWrite(trig_pin, HIGH);
  delay(10);
  digitalWrite(trig_pin, LOW);
  
  timing = pulseIn(echo_pin, HIGH);
  distance = (timing * 0.034) / 2;
  
  Serial.print("Distance: ");
  Serial.print(distance);
  Serial.print("cm | ");
  Serial.print(distance / 2.54);
  Serial.println("in");
  
    
  if (distance <= 50) {
  	tone(buzzer, 500);
  } else {
  	noTone(buzzer);
  }
  
  delay(100);
}

//temperature sensor
float temp;
int temppin = 2;
int ledpin=7;
void setup(){
	serial.begin(9600);
	pinMode(ledpin, OUTPUT);
}
void loop(){
	int sensorValue = analogRead(temppin);
	temp = sensorValue*0.48828125;

	serial.print("Temperature:");
	serial.print(temp);
	serial.print("'C");

	if (temp >= 250.0){
		digitalwrite(ledpin,HIGH);
	}else{
		digitalwrite(ledpin,LOW);
	}

	delay(1000);
}#!/usr/bin/python3
import time

from gpiozero import LED

led01 = LED(16)
led02 = LED(20)

while True:
    led01.on()
    print ("01")
    time.sleep(1)
    led01.off()
    led02.on()
    print ("02")
    time.sleep(1)
    led02.off()

import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)

GPIO_TRIG = 23   # Yellow wire
GPIO_ECHO = 24   # Pink wire

GPIO.setup(GPIO_TRIG, GPIO.OUT)
GPIO.setup(GPIO_ECHO, GPIO.IN)

GPIO.output(GPIO_TRIG, False)
print("Waiting for sensor to settle...")
time.sleep(2)

# Trigger pulse
GPIO.output(GPIO_TRIG, True)
time.sleep(0.00001)
GPIO.output(GPIO_TRIG, False)

# Wait for echo start
while GPIO.input(GPIO_ECHO) == 0:
    start_time = time.time()

# Wait for echo end
while GPIO.input(GPIO_ECHO) == 1:
    stop_time = time.time()

# Calculate distance
pulse_duration = stop_time - start_time
distance = round(pulse_duration * 17150, 2)

print("Distance:", distance, "cm")

GPIO.cleanup()

import RPi.GPIO as GPIO
import time

RAIN_PIN = 17   # DO pin of rain sensor

GPIO.setmode(GPIO.BCM)
GPIO.setup(RAIN_PIN, GPIO.IN, pull_up_down=GPIO.PUD_UP)

print("Rain Sensor Monitoring... Press CTRL+C to stop")

try:
    while True:
        if GPIO.input(RAIN_PIN) == GPIO.LOW:
            print("🌧️ Rain Detected!")
        else:
            print("☀️ No Rain")
        time.sleep(1)

except KeyboardInterrupt:
    print("\nExiting...")
    GPIO.cleanup()

import RPi.GPIO as GPIO
import time

SOIL_PIN = 24  # DO pin of soil moisture sensor

GPIO.setmode(GPIO.BCM)
GPIO.setup(SOIL_PIN, GPIO.IN, pull_up_down=GPIO.PUD_UP)

print("Soil Moisture Sensor Monitoring... Press CTRL+C to exit")

try:
    while True:
        if GPIO.input(SOIL_PIN) == GPIO.LOW:
            print("🌧️ Soil is Wet / Moisture Detected")
        else:
            print("🔥 Soil is Dry")
        time.sleep(1)

except KeyboardInterrupt:
    print("\nExiting...")
    GPIO.cleanup()

import RPi.GPIO as GPIO
import time

BUZZER_PIN = 4   # GPIO connected to buzzer

GPIO.setmode(GPIO.BCM)
GPIO.setup(BUZZER_PIN, GPIO.OUT)
GPIO.setwarnings(False)

print("Buzzer Test... Press CTRL+C to exit")

try:
    while True:
        print("Beep ON")
        GPIO.output(BUZZER_PIN, GPIO.HIGH)
        time.sleep(0.5)

        print("Beep OFF")
        GPIO.output(BUZZER_PIN, GPIO.LOW)
        time.sleep(0.5)

except KeyboardInterrupt:
    print("\nExiting...")
    GPIO.cleanup()

import Adafruit_DHT
import time

DHT_SENSOR = Adafruit_DHT.DHT11
DHT_PIN = 17   # Data pin of DHT11

print("Temperature Sensor Monitoring... Press CTRL+C to exit")

try:
    while True:
        humidity, temperature = Adafruit_DHT.read(DHT_SENSOR, DHT_PIN)

        if humidity is not None and temperature is not None:
            print("🌡️ Temp:", temperature, "°C   💧 Humidity:", humidity, "%")
        else:
            print("Sensor error, trying again...")

        time.sleep(1)

except KeyboardInterrupt:
    print("\nExiting...")

from gpiozero import MotionSensor
Fform signal import pause
import time

pir=MotionSensor(18)
print(“Sensor Warming up…..”)
time.sleep(0.5)
print (“ready”)

def motion_function():
print(“Motion detected”)
pir.when_motion=motion_function
pause()
