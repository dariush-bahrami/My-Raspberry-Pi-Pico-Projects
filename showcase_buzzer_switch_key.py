from buzzer.keys import BuzzerSwitch

switch_pin_id = 14
buzzer_pin_id = 15
note_name = "C#"
octave = 4
loudness = 1.0
buzzer_switch = BuzzerSwitch(switch_pin_id, buzzer_pin_id, note_name, octave, loudness)

while True:
    buzzer_switch.update()
