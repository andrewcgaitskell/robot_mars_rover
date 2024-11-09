import time
import board
import busio
import adafruit_pca9685
from adafruit_motor import motor
import zero_servos as z

# Initialize I2C bus and PCA9685 PWM controller
i2c = busio.I2C(board.SCL, board.SDA)
pca = adafruit_pca9685.PCA9685(i2c)
pca.frequency = 1000

# Define motor channels (adjust based on your wiring)
Motor_EN = pca.channels[0]  # Enable channel
Motor_Pin1 = pca.channels[1]  # Motor input 1
Motor_Pin2 = pca.channels[2]  # Motor input 2

# Initialize motor object
motor_driver = motor.DCMotor(Motor_Pin1, Motor_Pin2)

def motorStop():
    motor_driver.throttle = 0

def setup():
    motorStop()  # Ensure the motor is stopped on startup

def motor(direction, speed):
    # Speed should be between 0 (stop) and 1 (full speed)
    speed = max(0, min(speed / 100, 1))
    if direction == -1:
        motor_driver.throttle = -speed  # Reverse direction
    elif direction == 1:
        motor_driver.throttle = speed   # Forward direction

def move10cm_fwd():
    motor(1, 100)
    time.sleep(0.2)
    motor(-1, 50)
    time.sleep(0.1)
    motorStop()

def move5cm_fwd():
    motor(1, 100)
    time.sleep(0.1)
    motor(-1, 50)
    time.sleep(0.075)
    motorStop()

def move5cm_back():
    motor(-1, 100)
    time.sleep(0.125)
    motor(1, 50)
    time.sleep(0.075)
    motorStop()

setup()

# Move forward and backward repeatedly
for x in range(1, 10):
    move5cm_fwd()
    time.sleep(1)
    move5cm_back()
    time.sleep(1)

# Zero all servos at the end
z.zero_all()
