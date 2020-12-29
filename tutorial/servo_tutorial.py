import Adafruit_PCA9685 # Import the library used to communicate with PCA9685
import time

pwm = Adafruit_PCA9685.PCA9685() # Instantiate the object used to control the PWM
pwm.set_pwm_freq(50) # Set the frequency of the PWM signal

while 1: # Make the servo connected to the No. 3 servo port on the Motor HAT drive board reciprocate
  pwm.set_pwm(3, 0, 300)
  time.sleep(1)
  pwm.set_pwm(3, 0, 400)
  time.sleep(1)
