from sg90servo import MySG90Servo

pin_id = 15
angular_speed = 720
steps = angular_speed * 2

servo = MySG90Servo(pin_id)


servo.sweep(0, 90, angular_speed, steps)
servo.sweep(90, 0, angular_speed, steps)
