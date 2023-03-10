import random

from machine import Pin
from utime import sleep

from .core import Buzzer
from .notes import Tone


class Exorcist:
    """
    HOW TO USE

    1. Connect buzzer's positive pin (longer one) to the specified picos's GP pin

        Note: you can connect more than 1 buzzer to generate a louder sound! Just pass
            the GP numbers as a tuple.

    2. Connect buzzer's other pin to the GND.

    3. If you want you can connect a LED too. Connect LED's longest pin (positive one)
        to one of the GP pins of the pico and pass the the GP number as second argument.
        If you dont want to use led pass None as the second argument.

    4. Specify the loudness of the song as a float between 0 and 1.
    """

    def __init__(self, buzzer_pins, led_pin=None, loudness=0.9):
        self.buzzers = [Buzzer(p) for p in buzzer_pins]
        if led_pin is not None:
            self.led = Pin(led_pin, Pin.OUT)
        else:
            self.led = None
        self.notes = "EAEBEGAECEDEBCEAEBEGAECEDEBCEB"
        tempo = 294
        self.unit_duration = 1 / (tempo / 60)
        self.loudness = loudness

    def mute(self):
        for buzzer in self.buzzers:
            buzzer.set_loudness(0)

    def play(self):
        for note in self.notes:
            if self.led is not None:
                self.led.high() if random.random() > 0.5 else self.led.low()
            for buzzer in self.buzzers:
                octave = random.choice((3, 4))
                octave = octave if note not in "CD" else octave + 1
                tone = Tone(note, octave, 1, self.loudness)
                buzzer.set_frequency(tone.pitch)
                buzzer.set_loudness(self.loudness)
            note_time = tone.duration * self.unit_duration
            mute_ratio = random.uniform(0.01, 0.1)
            sleep(note_time * (1 - mute_ratio))
            self.mute()
            sleep(note_time * mute_ratio)
        self.mute()
        if self.led is not None:
            self.led.low()
