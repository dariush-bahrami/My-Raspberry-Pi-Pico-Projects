from utime import sleep

from .core import Buzzer


class Player:
    def __init__(self, pin, tempo, maximum_loudness):
        self.buzzer = Buzzer(pin)
        self.maximum_loudness = maximum_loudness
        self.unit_duration = 1 / (tempo / 60)

    def play(self, song):
        for note in song:
            self.buzzer.set_frequency(note.pitch)
            self.buzzer.set_loudness(note.loudness * self.maximum_loudness)
            sleep(note.duration * self.unit_duration)
            self.buzzer.set_loudness(0)
