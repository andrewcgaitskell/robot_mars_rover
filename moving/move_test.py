import time
from rpi_ws281x import PixelStrip, Color

# LED strip configuration:
LED_COUNT = 12          # Number of LED pixels.
LED_PIN = 12            # GPIO pin connected to the pixels (18 uses PWM!).
LED_FREQ_HZ = 800000    # LED signal frequency in hertz (usually 800kHz)
LED_DMA = 10            # DMA channel to use for generating signal (try 10)
LED_BRIGHTNESS = 255    # Set to 0 for darkest and 255 for brightest
LED_INVERT = False      # True to invert the signal (when using NPN transistor level shift)
LED_CHANNEL = 0         # Set to '1' for GPIOs 13, 19, 41, 45 or 53

# Create PixelStrip object with the specified configuration
strip = PixelStrip(LED_COUNT, LED_PIN, LED_FREQ_HZ, LED_DMA, LED_INVERT, LED_BRIGHTNESS, LED_CHANNEL)
strip.begin()

# Function to turn off all LEDs
def turn_off_all_leds():
    for i in range(LED_COUNT):
        strip.setPixelColor(i, Color(0, 0, 0))  # Set each pixel to black (off)
    strip.show()  # Update the LED strip


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

def motor(direction, speed):
    # Speed should be between 0 and 100
    speed = max(0, min(speed, 100))

    # Quick start parameters
    kick_start_duration = 0.05  # Duration of the kick-start (in seconds)
    kick_start_speed = 100      # Speed for the quick start (maximum power)

    if direction == -1:  # Reverse
        GPIO.output(Motor_Pin1, GPIO.HIGH)
        GPIO.output(Motor_Pin2, GPIO.LOW)
        
        # Apply a quick burst of full speed
        pwm_motor.ChangeDutyCycle(kick_start_speed)
        time.sleep(kick_start_duration)

        # Set to desired speed
        pwm_motor.ChangeDutyCycle(speed)

    elif direction == 1:  # Forward
        GPIO.output(Motor_Pin1, GPIO.LOW)
        GPIO.output(Motor_Pin2, GPIO.HIGH)

        # Apply a quick burst of full speed
        pwm_motor.ChangeDutyCycle(kick_start_speed)
        time.sleep(kick_start_duration)

        # Set to desired speed
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
print("Turning off all LEDs...")
turn_off_all_leds()

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
