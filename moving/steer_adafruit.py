import time
import board
import busio
from adafruit_pca9685 import PCA9685

# Initialize I2C bus
i2c = busio.I2C(board.SCL, board.SDA)

# Create PCA9685 object
pwm = PCA9685(i2c)
pwm.frequency = 50  # Set the frequency to 50 Hz

## servo_channel = 2 ### steering
## servo_channel = 1 ## camera side to side
servo_channel = 3

try:
    while True:
        # Slowly move the servo from 300 to 400
        for i in range(0, 100):
            pwm.channels[servo_channel].duty_cycle = (300 + i) * 16  # Scale to 16-bit value
            time.sleep(0.05)

        # Slowly move the servo from 400 to 300
        for i in range(0, 100):
            pwm.channels[servo_channel].duty_cycle = (400 - i) * 16  # Scale to 16-bit value
            time.sleep(0.05)

        # Slowly move the servo from 300 to 200
        for i in range(0, 100):
            pwm.channels[servo_channel].duty_cycle = (300 - i) * 16  # Scale to 16-bit value
            time.sleep(0.05)
        
        # Slowly move the servo from 200 to 300
        for i in range(0, 100):
            pwm.channels[servo_channel].duty_cycle = (200 + i) * 16  # Scale to 16-bit value
            time.sleep(0.05)

except KeyboardInterrupt:
    pwm.channels[servo_channel].duty_cycle = (300) * 16
    print("Stopping...")

finally:
    pwm.deinit()  # Clean up the PCA9685
    print("PCA9685 deinitialized.")
