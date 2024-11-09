import time
import RPi.GPIO as GPIO

# Servo configuration
SERVO_PIN = 23  # GPIO pin connected to the servo (BCM numbering)
FREQUENCY = 50  # Servo control frequency (50 Hz)

# Define the straight-ahead angle (adjust this as needed)
STRAIGHT_AHEAD_ANGLE = 90  # Adjust based on your specific servo calibration

# Setup GPIO
GPIO.setmode(GPIO.BCM)
GPIO.setup(SERVO_PIN, GPIO.OUT)

# Initialize PWM on the servo pin
pwm = GPIO.PWM(SERVO_PIN, FREQUENCY)
pwm.start(7.5)  # Set to the neutral position (90°)

# Helper function to set the servo angle
def set_servo_angle(angle):
    # Convert angle (0-180) to duty cycle (5-10%)
    duty_cycle = 5 + (angle / 18)
    print(f"Setting angle {angle} -> Duty Cycle {duty_cycle:.2f}%")
    pwm.ChangeDutyCycle(duty_cycle)
    time.sleep(0.5)  # Wait for the servo to move

try:
    print("Moving servo from 0° to 180° and back to 0°.")
    while True:
        # Move the servo from 0° to 180°
        for angle in range(0, 181, 10):
            set_servo_angle(angle)

        # Move the servo from 180° back to 0°
        for angle in range(180, -1, -10):
            set_servo_angle(angle)

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
