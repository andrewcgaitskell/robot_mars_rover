import time
import zero_servos as z
import RPi.GPIO as GPIO # Import the library used to control GPIO
GPIO.cleanup() # Reset the high and low levels of the GPIO port
GPIO.setwarnings(False) # Ignore some insignificant errors
GPIO.setmode(GPIO.BCM)

import Adafruit_PCA9685 #Import the library used to communicate with PCA9685
import time
import zero_servos as z

pwm_steering = Adafruit_PCA9685.PCA9685() # Instantiate the object used to control the PWM
pwm_steering.set_pwm_freq(50) # Set the frequency of the PWM signal

z1,z2,z3 = z.zero_all()

# There are three encoding methods for the GPIO port of the Raspberry Pi,
# we choose BCM encoding to define the GPIO port

'''
The following code defines the GPIO used to control the L298N chip.
This definition is different for different Raspberry Pi driver boards.
'''

Motor_EN = 17
Motor_Pin1 = 27
Motor_Pin2 = 18

def motorStop():
  GPIO.output(Motor_Pin1, GPIO.LOW)
  GPIO.output(Motor_Pin2, GPIO.LOW)
  GPIO.output(Motor_EN, GPIO.LOW)

def setup(): # GPIO initialization, GPIO motor cannot be controlled without initialization
  global pwm_motor
  GPIO.setwarnings(False)
  GPIO.setmode(GPIO.BCM)
  GPIO.setup(Motor_EN, GPIO.OUT)
  GPIO.setup(Motor_Pin1, GPIO.OUT)
  GPIO.setup(Motor_Pin2, GPIO.OUT)
  
  motorStop() # Avoid motor starting to rotate automatically after initialization
  try: # Try is used here to avoid errors due to repeated PWM settings
    pwm_motor = GPIO.PWM(Motor_EN, 1000)
  except:
    pass

def motor(direction, speed): # The function used to control the motor
  if direction == -1:
    GPIO.output(Motor_Pin1, GPIO.HIGH)
    GPIO.output(Motor_Pin2, GPIO.LOW)
    pwm_motor.start(100)
    pwm_motor.ChangeDutyCycle(speed)

  if direction == 1:
    GPIO.output(Motor_Pin1, GPIO.LOW)
    GPIO.output(Motor_Pin2, GPIO.HIGH)
    pwm_motor.start(100)
    pwm_motor.ChangeDutyCycle(speed)

setup()

def circle_fwd(time_in,speed_in,angle_in):
  # Control motor to rotate at full speed for 0.5 seconds
  pwm_steering.set_pwm(2, 0, angle_in)
  motor(1, speed_in)
  time.sleep(time_in)

  # Control motor to rotate in opposite directions at full speed for 0.5 seconds

  motor(-1, 50)
  time.sleep(0.075)

  # Stop the motor
  motorStop()

while 1:
  circle_fwd(10,90,390)
  
