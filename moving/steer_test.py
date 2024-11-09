import time
import RPi.GPIO as GPIO

# Servo configuration
SERVO_PIN = 23  # GPIO pin connected to the servo (BCM numbering)
FREQUENCY = 50  # Servo control frequency (50 Hz)

# Setup GPIO
GPIO.setmode(GPIO.BCM)
GPIO.setup(SERVO_PIN, GPIO.OUT)

# Initialize PWM on the servo pin
pwm = GPIO.PWM(SERVO_PIN, FREQUENCY)
pwm.start(7.5)  # Start at the neutral position (7.5% duty cycle for 90°)

# Helper function to set the servo position using duty cycle
def set_servo_position(duty_cycle):
    pwm.ChangeDutyCycle(duty_cycle)

try:
    while True:
        # Slowly move the servo from 300 to 400 (approximated with duty cycle)
        for i in range(0, 100):
            duty_cycle = 5.0 + (i / 20)  # Scale i (0-100) to duty cycle (5.0-10.0)
            set_servo_position(duty_cycle)
            time.sleep(0.05)

        # Slowly move the servo from 400 to 300
        for i in range(0, 100):
            duty_cycle = 10.0 - (i / 20)  # Scale i (0-100) to duty cycle (10.0-5.0)
            set_servo_position(duty_cycle)
            time.sleep(0.05)

except KeyboardInterrupt:
    print("Stopping...")

finally:
    # Reset the servo to the neutral position and clean up
    set_servo_position(7.5)  # Neutral position (90°)
    time.sleep(1)
    pwm.stop()
    GPIO.cleanup()
