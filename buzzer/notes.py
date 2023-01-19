OCTAVE_0 = {
    "C": 16.35,
    "C#": 17.32,
    "D": 18.35,
    "D#": 19.45,
    "E": 20.60,
    "F": 21.83,
    "F#": 23.12,
    "G": 24.50,
    "G#": 25.96,
    "A": 27.50,
    "A#": 29.14,
    "B": 30.87,
}


class Tone:
    def __init__(self, name, octave, duration, loudness):
        self.pitch = OCTAVE_0[name] * 2**octave
        self.duration = duration
        self.loudness = loudness


class Silence:
    def __init__(self, duration):
        self.pitch = OCTAVE_0["C"]
        self.duration = duration
        self.loudness = 0
