import Adafruit_PCA9685 #Import the library used to communicate with PCA9685
import time
import zero_servos as z

pwm = Adafruit_PCA9685.PCA9685() # Instantiate the object used to control the PWM
pwm.set_pwm_freq(50) # Set the frequency of the PWM signal

z0,z1,z2 = z.zero_all()

while 1:
  for i in range(0,5):
    print(z1+(i*20))
    pwm.set_pwm(1, 0, (z1+(i*20)))
    time.sleep(0.1)
  for i in range(0,5):
    print((z1+120)-(i*20))
    pwm.set_pwm(1, 0, ((z1+100)-(i*20)))
    time.sleep(0.1)
  for i in range(0,-5):
    print(z1+(i*20))
    pwm.set_pwm(1, 0, (z1+(i*20)))
    time.sleep(0.1)
  for i in range(0,-5):
    print((z1+120)-(i*20))
    pwm.set_pwm(1, 0, ((z1+100)-(i*20)))
    time.sleep(0.1)
