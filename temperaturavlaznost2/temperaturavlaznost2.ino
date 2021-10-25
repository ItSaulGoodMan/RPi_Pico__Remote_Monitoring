//
//    FILE: dhtnew_endless_insideFunction.ino
// AUTHORS: Rob Tillaart, Vladislaw Kuzmin
// VERSION: 0.1.5
// PURPOSE: Demonstration example of endless DHT values' reporting in a function
//    DATE: 2021-02-19
//    (c) : MIT
//
// 0.1.0    2020-06-04 initial version
// 0.1.1    2020-06-15 match 0.3.0 error handling
// 0.1.2    2020-09-22 fix typo
// 0.1.3    2020-11-09 wait for read handling
// 0.1.5    2021-02-19 improved the sketch to read the DHT's value in a function
//
// DHT PINs' layout from left to right
// =================================
// FRONT : DESCRIPTION
// pin 1 : VCC
// pin 2 : DATA
// pin 3 : Not Connected
// pin 4 : GND


#include <dhtnew.h>

uint64_t previousMillis;
uint32_t count = 0;
uint32_t start, stop;

uint32_t errors[11] = { 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0 };
int zvuk = 0;
int zvuk2 = 0;
int gas = 0;
int gas2 = 0;
int vatra = 0;
void setup()
{
 
}

void DHTt(const uint8_t pin)
{
  if (millis() - previousMillis > 1) {
    previousMillis = millis();
    DHTNEW mySensor(pin);
    
    count++;
    // show counters for OK and errors.
    if (count % 50 == 0)
    {
      
      for (uint8_t i = 0; i < 10; i++)
      {
      
      }
      
    }
  
    if (count % 10 == 0)
    {
      
    }
    
  
    start = micros();
    int chk = mySensor.read();
    stop = micros();
  
    switch (chk)
    {
      case DHTLIB_OK:
        
        errors[0]++;
        break;
      case DHTLIB_ERROR_CHECKSUM:
       
        errors[1]++;
        break;
      case DHTLIB_ERROR_TIMEOUT_A:
        
        errors[2]++;
        break;
      case DHTLIB_ERROR_TIMEOUT_B:
        
        errors[3]++;
        break;
      case DHTLIB_ERROR_TIMEOUT_C:
        
        errors[4]++;
        break;
      case DHTLIB_ERROR_TIMEOUT_D:
        
        errors[5]++;
        break;
      case DHTLIB_ERROR_SENSOR_NOT_READY:
        
        errors[6]++;
        break;
      case DHTLIB_ERROR_BIT_SHIFT:
        
        errors[7]++;
        break;
      case DHTLIB_WAITING_FOR_READ:
        
        errors[8]++;
        break;
      default:
    
        errors[9]++;
        break;
    }
    // DISPLAY DATA
    Serial.println(mySensor.getHumidity(), 1);
    
    Serial.println(mySensor.getTemperature(), 1);
    zvuk = digitalRead(6);
        zvuk2 = analogRead(27);

   gas = digitalRead(7);
   gas2 = analogRead(28);
   vatra = digitalRead(8); 
    Serial.println(zvuk);
        Serial.println(zvuk2);

    Serial.println(gas);
        Serial.println(gas2);

    Serial.println(vatra);
    


    
    
  }
}

void loop() {
  DHTt(15);
  delay(5000);
}
