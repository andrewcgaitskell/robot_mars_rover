import Adafruit_PCA9685 #Import the library used to communicate with PCA9685
import time

pwm = Adafruit_PCA9685.PCA9685() # Instantiate the object used to control the PWM

pwm.set_pwm_freq(50) # Set the frequency of the PWM signal

#servo1 - port 0 - camera tilt
#servo2 - port 1 - camera rotate
#servo3 - port 2 - steering

'''
According to the different servos, this value represents different servo angles.
The PWM duty cycle range of the servos we use is approximately 100 to 560, which corresponds to a rotation range of approximately 0 ° to 180 °.
'''

# following trimmed each servo so they are straight or level
servo1_zero = 330-50 #100 + (460/2)
servo2_zero = 330-20 #100 + (460/2) trimmed
servo3_zero = 330-10 #100 + (460/2) trimmed

pwm.set_pwm(0, 0, servo1_zero)
pwm.set_pwm(1, 0, servo2_zero)
pwm.set_pwm(2, 0, servo3_zero)


'''
while 1:
  for i in range(0,100): # Slowly move the servo from 300 to 400
    pwm.set_pwm(2, 0, (300+i))
    time.sleep(0.05)
  for i in range(0,100): # Slowly move the servo from 400 to 300
    pwm.set_pwm(2, 0, (400-i))
    time.sleep(0.05)
'''
