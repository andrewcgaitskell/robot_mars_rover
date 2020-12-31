import Adafruit_PCA9685 #Import the library used to communicate with PCA9685
import time
import zero_servos as z

pwm = Adafruit_PCA9685.PCA9685() # Instantiate the object used to control the PWM
pwm.set_pwm_freq(50) # Set the frequency of the PWM signal

z1,z2,z3 = z.zero_all()

while 1:
  for i in range(0,15): # Slowly move the servo from 300 to 400
    print(z2+(i*10))
    pwm.set_pwm(2, 0, (z2+(i*10)))
    time.sleep(0.5)
  for i in range(0,15): # Slowly move the servo from 400 to 300
    print((z2+200)-(i*10))
    pwm.set_pwm(2, 0, ((z2+150)-(i*10)))
    time.sleep(0.5)
