import random
import time
import RPi.GPIO as GPIO
from quart import Blueprint, jsonify, render_template

line_following_bp = Blueprint('line_following_bp', __name__, template_folder='templates')

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

# Initialize GPIO
setup()

# API endpoint to provide sensor data
@line_following_bp.route('/line_data')
async def fn_line_data():
    sensor_value = get_sensor_value()
    return jsonify({"value": sensor_value})

# Route to render the Jinja2 template with the chart
@sensor_bp.route('/show_line_data')
async def fn_show_line_data():
    return await render_template('sensor_data.html')
