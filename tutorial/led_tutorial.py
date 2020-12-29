import time
from rpi_ws281x import *

class LED:
  def __init__(self):
    self.LED_COUNT = 16 # Set to the total number of LED lights on the robot product.There are more LED lights on the Pi
    self.LED_PIN = 12 # Set to the input pin number of the LED group 
    self.LED_FREQ_HZ = 800000
    self.LED_DMA = 10
    self.LED_BRIGHTNESS = 255
    self.LED_INVERT = False
    self.LED_CHANNEL = 0

    # Use the configuration item above to create a strip
    self.strip = Adafruit_NeoPixel(
    self.LED_COUNT, self.LED_PIN, self.LED_FREQ_HZ, self.LED_DMA, self.LED_INVERT, self.LED_BRIGHTNESS, self.LED_CHANNEL
    )

    self.strip.begin()

  def colorWipe(self, R, G, B): # This function is used to change the color of the LED light
    color = Color(R, G, B)
    for i in range(self.strip.numPixels()): # Only one LED light color can be set at a time, so we need to do a loop
      self.strip.setPixelColor(i, color)
      self.strip.show() # The color will only change after calling the show method

if __name__ == '__main__':
  LED = LED()
  try:
    while 1:
      LED.colorWipe(255, 0, 0) # All the lights turn red
      time.sleep(1)
      LED.colorWipe(0, 255, 0) # All lights turn green 
      time.sleep(1)
      LED.colorWipe(0, 0, 255) # All lights turn blue
      time.sleep(1)
  except:
    LED.colorWipe(Color(0,0,0)) # Turn off all lights
