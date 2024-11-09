import time
import RPi.GPIO as GPIO

# Define GPIO pins
Motor_EN = 17
Motor_Pin1 = 27
Motor_Pin2 = 18
Servo1_Pin = 22  # Camera tilt
Servo2_Pin = 23  # Camera rotate
Servo3_Pin = 24  # Steering

# Servo zero positions (trimmed for straight/level positioning)
SERVO1_ZERO = 7.5  # Neutral position (1.5 ms pulse width)
SERVO2_ZERO = 7.0  # Neutral position (trimmed)
SERVO3_ZERO = 7.3  # Neutral position (trimmed)

# Setup GPIO
def setup():
    GPIO.setwarnings(False)
    GPIO.setmode(GPIO.BCM)
    GPIO.setup(Motor_EN, GPIO.OUT)
    GPIO.setup(Motor_Pin1, GPIO.OUT)
    GPIO.setup(Motor_Pin2, GPIO.OUT)
    GPIO.setup(Servo1_Pin, GPIO.OUT)
    GPIO.setup(Servo2_Pin, GPIO.OUT)
    GPIO.setup(Servo3_Pin, GPIO.OUT)

    global pwm_motor, pwm_servo1, pwm_servo2, pwm_servo3
    pwm_motor = GPIO.PWM(Motor_EN, 1000)  # Motor PWM at 1000 Hz
    pwm_servo1 = GPIO.PWM(Servo1_Pin, 50)  # Servo PWM at 50 Hz
    pwm_servo2 = GPIO.PWM(Servo2_Pin, 50)  # Servo PWM at 50 Hz
    pwm_servo3 = GPIO.PWM(Servo3_Pin, 50)  # Servo PWM at 50 Hz

    pwm_motor.start(0)
    pwm_servo1.start(0)
    pwm_servo2.start(0)
    pwm_servo3.start(0)

    motorStop()
    zero_all()

# Stop the motor
def motorStop():
    GPIO.output(Motor_Pin1, GPIO.LOW)
    GPIO.output(Motor_Pin2, GPIO.LOW)
    pwm_motor.ChangeDutyCycle(0)

# Control the motor direction and speed
def motor(direction, speed):
    # Speed should be between 0 and 100
    speed = max(0, min(speed, 100))

    if direction == -1:  # Reverse
        GPIO.output(Motor_Pin1, GPIO.HIGH)
        GPIO.output(Motor_Pin2, GPIO.LOW)
        pwm_motor.ChangeDutyCycle(speed)

    elif direction == 1:  # Forward
        GPIO.output(Motor_Pin1, GPIO.LOW)
        GPIO.output(Motor_Pin2, GPIO.HIGH)
        pwm_motor.ChangeDutyCycle(speed)

# Zero all servos
def zero_all():
    pwm_servo1.ChangeDutyCycle(SERVO1_ZERO)
    pwm_servo2.ChangeDutyCycle(SERVO2_ZERO)
    pwm_servo3.ChangeDutyCycle(SERVO3_ZERO)
    print(f"Servos zeroed to: {SERVO1_ZERO}, {SERVO2_ZERO}, {SERVO3_ZERO}")
    time.sleep(0.5)  # Give time for servos to move

# Move the car forward by approximately 10 cm
def move10cm_fwd():
    motor(1, 100)
    time.sleep(0.2)
    motor(-1, 50)
    time.sleep(0.1)
    motorStop()

# Move the car forward by approximately 5 cm
def move5cm_fwd():
    motor(1, 100)
    time.sleep(0.1)
    motor(-1, 50)
    time.sleep(0.075)
    motorStop()

# Move the car backward by approximately 5 cm
def move5cm_back():
    motor(-1, 100)
    time.sleep(0.125)
    motor(1, 50)
    time.sleep(0.075)
    motorStop()

# Main setup and loop
setup()

try:
    for x in range(1, 10):
        move5cm_fwd()
        time.sleep(1)
        move5cm_back()
        time.sleep(1)
finally:
    # Clean up GPIO and stop all servos
    motorStop()
    zero_all()
    pwm_servo1.stop()
    pwm_servo2.stop()
    pwm_servo3.stop()
    GPIO.cleanup()
