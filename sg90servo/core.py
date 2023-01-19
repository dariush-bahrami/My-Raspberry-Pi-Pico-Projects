from time import sleep

from machine import PWM, Pin


class SG90Servo:
    def __init__(self, pin_id: int, min_value: int, max_value: int):
        self.pwm = PWM(Pin(pin_id))
        self.pwm.freq(50)
        self.min_value = min_value
        self.delta = max_value - min_value

    def convert_angle_to_duty_16(self, angle):
        angle = min(max(angle, 0), 180)  # cap between -90° and +90°
        return int((angle / 180) * self.delta + self.min_value)

    def set_angle(self, angle: float):
        self.pwm.duty_u16(self.convert_angle_to_duty_16(angle))

    def sweep(self, start_angle, stop_angle, angular_speed, steps):
        delta_theta = stop_angle - start_angle
        total_time = abs(delta_theta) / angular_speed
        sleep_time = total_time / steps
        angular_step = delta_theta / steps
        self.set_angle(start_angle)
        for i in range(1, steps + 1):
            self.set_angle(start_angle + i * angular_step)
            sleep(sleep_time)
        self.set_angle(stop_angle)


class MySG90Servo(SG90Servo):
    def __init__(self, pin_id: int):
        super().__init__(pin_id, 1638, 8192)
