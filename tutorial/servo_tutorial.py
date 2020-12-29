import Adafruit_PCA9685 # Import the library used to communicate with PCA9685
import time

pwm = Adafruit_PCA9685.PCA9685() # Instantiate the object used to control the PWM
pwm.set_pwm_freq(50) # Set the frequency of the PWM signal

# Tutorial has Servo Port 3 - there are three servos and the ports start at 0? Changed to Port 1

while 1: # Make the servo connected to the No. 1 servo port on the Motor HAT drive board reciprocate
  pwm.set_pwm(1, 0, 300)
  time.sleep(1)
  pwm.set_pwm(1, 0, 400)
  time.sleep(1)
