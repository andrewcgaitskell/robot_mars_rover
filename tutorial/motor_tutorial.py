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

Motor_A_EN = 4
sc.stopWiggle()
sc.singleServo(3, 1, 2)
time.sleep(1)
sc.stopWiggle()
Motor_A_Pin1 = 14
Motor_A_Pin2 = 15

def motorStop():
  GPIO.output(Motor_A_Pin1, GPIO.LOW)
  GPIO.output(Motor_A_Pin2, GPIO.LOW)
  GPIO.output(Motor_A_EN, GPIO.LOW)

def setup(): # GPIO initialization, GPIO motor cannot be controlled without initialization
  global pwm_A, pwm_B
  GPIO.setwarnings(False)
  GPIO.setmode(GPIO.BCM)
  GPIO.setup(Motor_A_EN, GPIO.OUT)
  GPIO.setup(Motor_A_Pin1, GPIO.OUT)
  GPIO.setup(Motor_A_Pin2, GPIO.OUT)
  
  motorStop() # Avoid motor starting to rotate automatically after initialization
  try: # Try is used here to avoid errors due to repeated PWM settings
    pwm_A = GPIO.PWM(Motor_A_EN, 1000)
  except:
    pass

def motor_A(direction, speed): # The function used to control the motor of port A
  if direction == 1:
    GPIO.output(Motor_A_Pin1, GPIO.HIGH)
    GPIO.output(Motor_A_Pin2, GPIO.LOW)
    pwm_A.start(100)
    pwm_A.ChangeDutyCycle(speed)

  if direction == -1:
    GPIO.output(Motor_A_Pin1, GPIO.LOW)
    GPIO.output(Motor_A_Pin2, GPIO.HIGH)
    pwm_A.start(100)
    pwm_A.ChangeDutyCycle(speed)
    
# Control A and B motors to rotate at full speed for 3 seconds
motor_A(1, 100)
time.sleep(3)

# Control A and B motors to rotate in opposite directions at full speed for 3 seconds

motor_A(-1, 100)
time.sleep(3)

# Stop the motor rotation of A port

motorStop()
