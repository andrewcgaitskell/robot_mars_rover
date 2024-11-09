import time
import RPi.GPIO as GPIO

# Servo configuration
SERVO_PIN = 23  # GPIO pin connected to the servo (BCM numbering)
FREQUENCY = 50  # Servo control frequency (50 Hz)

# Define the straight-ahead angle (adjust this as needed)
STRAIGHT_AHEAD_ANGLE = 85  # Adjust based on your specific servo calibration

# Setup GPIO
GPIO.setmode(GPIO.BCM)
GPIO.setup(SERVO_PIN, GPIO.OUT)

# Initialize PWM on the servo pin
pwm = GPIO.PWM(SERVO_PIN, FREQUENCY)
pwm.start(0)

# Helper function to set the servo angle
def set_servo_angle(angle):
    # Convert angle (0-180) to duty cycle (2-12%)
    duty_cycle = 2 + (angle / 18)
    pwm.ChangeDutyCycle(duty_cycle)

try:
    while True:
        # Slowly move the servo from 0° to 180°
        for angle in range(0, 181, 1):
            set_servo_angle(angle)
            time.sleep(0.05)

        # Slowly move the servo from 180° back to 0°
        for angle in range(180, -1, -1):
            set_servo_angle(angle)
            time.sleep(0.05)

except KeyboardInterrupt:
    print("Stopping...")

finally:
    # Set the servo to the straight-ahead position
    print(f"Setting servo to straight-ahead position ({STRAIGHT_AHEAD_ANGLE}°)")
    set_servo_angle(STRAIGHT_AHEAD_ANGLE)
    time.sleep(1)  # Give time for the servo to move

    # Clean up
    pwm.ChangeDutyCycle(0)
    pwm.stop()
    GPIO.cleanup()
