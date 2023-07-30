from gpiozero import Servo
from time import sleep

# Set the GPIO pin used to control the servo
servo_pin = 17

# Create a servo object
servo = Servo(servo_pin)

try:
    while True:
        # Move the servo to the minimum angle (usually -1, but may vary)
        servo.min()
        sleep(1)

        # Move the servo to the middle position (usually 0, but may vary)
        servo.mid()
        sleep(1)

        # Move the servo to the maximum angle (usually 1, but may vary)
        servo.max()
        sleep(1)

except KeyboardInterrupt:
    pass

# Cleanup
servo.detach()
