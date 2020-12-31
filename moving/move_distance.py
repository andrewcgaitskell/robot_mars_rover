import time
import RPi.GPIO as GPIO # Import the library used to control GPIO
GPIO.cleanup() # Reset the high and low levels of the GPIO port
GPIO.setwarnings(False) # Ignore some insignificant errors
GPIO.setmode(GPIO.BCM)

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
  global pwm
  GPIO.setwarnings(False)
  GPIO.setmode(GPIO.BCM)
  GPIO.setup(Motor_EN, GPIO.OUT)
  GPIO.setup(Motor_Pin1, GPIO.OUT)
  GPIO.setup(Motor_Pin2, GPIO.OUT)
  
  motorStop() # Avoid motor starting to rotate automatically after initialization
  try: # Try is used here to avoid errors due to repeated PWM settings
    pwm = GPIO.PWM(Motor_EN, 1000)
  except:
    pass

def motor(direction, speed): # The function used to control the motor
  if direction == -1:
    GPIO.output(Motor_Pin1, GPIO.HIGH)
    GPIO.output(Motor_Pin2, GPIO.LOW)
    pwm.start(100)
    pwm.ChangeDutyCycle(speed)

  if direction == 1:
    GPIO.output(Motor_Pin1, GPIO.LOW)
    GPIO.output(Motor_Pin2, GPIO.HIGH)
    pwm.start(100)
    pwm.ChangeDutyCycle(speed)

setup()

def move10cm_fwd():
  # Control motor to rotate at full speed for 0.5 seconds
  motor(1, 100)
  time.sleep(0.2)

  # Control motor to rotate in opposite directions at full speed for 0.5 seconds

  motor(-1, 50)
  time.sleep(0.1)

  # Stop the motor

  motorStop()

  
def move5cm_fwd():
  # Control motor to rotate at full speed for 0.5 seconds
  motor(1, 100)
  time.sleep(0.05)

  # Control motor to rotate in opposite directions at full speed for 0.5 seconds

  #motor(-1, 50)
  #time.sleep(0.1)

  # Stop the motor

  motorStop()

move5cm_fwd()
