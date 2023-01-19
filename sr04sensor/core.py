import utime
from machine import Pin


class SR04DistanceSensor:
    SOUND_SPEED = 0.0343  # cm per microsecond

    def __init__(self, trigger_pin_id: int, echo_pin_id: int):
        self.trigger = Pin(trigger_pin_id, Pin.OUT)
        self.echo = Pin(echo_pin_id, Pin.IN)

    def sense(self):
        self.trigger.low()
        utime.sleep_us(2)
        self.trigger.high()
        utime.sleep_us(5)
        self.trigger.low()

        while self.echo.value() == 0:
            signal_off = utime.ticks_us()
        while self.echo.value() == 1:
            signal_on = utime.ticks_us()

        time_passed = signal_on - signal_off
        distance = (time_passed * self.SOUND_SPEED) / 2
        return distance / 100  # distance in meter
