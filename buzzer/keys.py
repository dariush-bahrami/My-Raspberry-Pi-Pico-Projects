from machine import Pin

from .core import Buzzer
from .notes import OCTAVE_0


class BuzzerSwitch:
    """
    HOW TO USE

    1. Connect input pin of the switch to 3V3(OUT) and output pin of the switch to one
        of the pico's GP pins.

    2. Connect buzzer's positive pin (longer one) to the specified picos's GP pin.

    3. Connect buzzer's other pin to the GND.

    4. Specify musical note name and octave.

    4. Specify the loudness of the song as a float between 0 and 1.
    """

    def __init__(
        self, switch_pin_id, buzzer_pin_id, note_name="D#", octave=4, loudness=0.9
    ):
        self.switch = Pin(switch_pin_id, Pin.IN, Pin.PULL_DOWN)
        self.buzzer = Buzzer(buzzer_pin_id)
        self.buzzer.set_frequency(OCTAVE_0[note_name] * 2**octave)
        self.loudness = loudness

    def update(self):
        self.buzzer.set_loudness(self.switch.value() * self.loudness)
