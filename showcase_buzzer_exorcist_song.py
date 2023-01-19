from buzzer.mysongs import Exorcist

player = Exorcist((15,), 14, 1.0)
try:
    player.play()
except KeyboardInterrupt:
    player.mute()
