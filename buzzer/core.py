from machine import PWM, Pin


class Buzzer:
    def __init__(self, pin_id):
        self.pin = PWM(Pin(pin_id))

    def set_loudness(self, value):
        self.pin.duty_u16(int(value * 1000))

    def set_frequency(self, value):
        self.pin.freq(int(value))
