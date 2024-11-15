import Adafruit_PCA9685 #Import the library used to communicate with PCA9685
import time
pwm = Adafruit_PCA9685.PCA9685() # Instantiate the object used to control the PWM
pwm.set_pwm_freq(50) # Set the frequency of the PWM signal

while 1:
  for i in range(0,100): # Slowly move the servo from 300 to 400
    pwm.set_pwm(1, 0, (300+i))
    time.sleep(0.025)
  for i in range(0,100): # Slowly move the servo from 400 to 300
    pwm.set_pwm(1, 0, (400-i))
    time.sleep(0.025)
