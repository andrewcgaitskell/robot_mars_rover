import RPi.GPIO as GPIO
from IPython.display import display, clear_output
import IPython
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
import time

# Sensor pins
line_pin_right = 19
line_pin_middle = 16
line_pin_left = 20

# Initialize GPIO
def setup():
    GPIO.setwarnings(False)
    GPIO.setmode(GPIO.BCM)
    GPIO.setup(line_pin_right, GPIO.IN)
    GPIO.setup(line_pin_middle, GPIO.IN)
    GPIO.setup(line_pin_left, GPIO.IN)

# Define state values based on sensor readings
def get_sensor_value():
    status_right = GPIO.input(line_pin_right)
    status_middle = GPIO.input(line_pin_middle)
    status_left = GPIO.input(line_pin_left)

    # Determine the state value based on sensor readings
    if status_left == 1 and status_middle == 1 and status_right == 1:
        return 0  # All On
    elif status_left == 0 and status_middle == 1 and status_right == 1:
        return 1  # Left Off, Middle On, Right On
    elif status_left == 0 and status_middle == 0 and status_right == 1:
        return 2  # Left Off, Middle Off, Right On
    elif status_left == 1 and status_middle == 1 and status_right == 0:
        return -1  # Left On, Middle On, Right Off
    elif status_left == 1 and status_middle == 0 and status_right == 0:
        return -2  # Left On, Middle Off, Right Off
    elif status_left == 0 and status_middle == 0 and status_right == 0:
        return -3  # All Off
    else:
        return -3  # Undefined state

# Setup GPIO
setup()



      
