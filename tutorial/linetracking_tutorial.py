import RPi.GPIO as GPIO
import time
# Hunt module output pin
line_pin_right = 19
line_pin_middle = 16
line_pin_left = 20
'''
Initialize your GPIO port related to the line patrol module
'''
def setup():
  GPIO.setwarnings(False)
  GPIO.setmode(GPIO.BCM)
  GPIO.setup(line_pin_right,GPIO.IN)
  GPIO.setup(line_pin_middle,GPIO.IN)
  GPIO.setup(line_pin_left,GPIO.IN)

def run():
  '''
  Read the values of three infrared sensor phototransistors (0 is no line detected, 1 is line detected)
  This routine takes the black line on white as an example
  '''
  status_right = GPIO.input(line_pin_right)
  status_middle = GPIO.input(line_pin_middle)
  status_left = GPIO.input(line_pin_left)
  # Detect if the line hunting module senses the line
  if status_middle == 1:
    print('forward')
  elif status_left == 1:
    print('left')
  elif status_right == 1:
    print('right')
  else:
    print('stop')

if __name__ == '__main__':
  setup()
  while 1:
    run()
  
