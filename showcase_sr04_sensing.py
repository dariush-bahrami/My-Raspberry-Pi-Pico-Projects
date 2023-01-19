from machine import Pin
import utime
from sr04sensor import SR04DistanceSensor

trig_pin_id = 3
echo_pin_id = 2
sr04 = SR04DistanceSensor(trig_pin_id, echo_pin_id)

while True:
   print(round(sr04.sense()*100, 2), "cm")
   utime.sleep(0.5)