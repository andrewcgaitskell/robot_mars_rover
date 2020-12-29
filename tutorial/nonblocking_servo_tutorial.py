import RPIservo # Import a library that uses multiple threads to control the steering gear
import time

sc = RPIservo.ServoCtrl() # Instantiate the object that controls the steering gear

sc.start() # Start this thread, when the servo does not move, the thread is suspended

while 1:
  sc.singleServo(2, -1, 2)
  time.sleep(1)
  sc.stopWiggle()
  sc.singleServo(2, 1, 2)
  time.sleep(1)
  sc.stopWiggle()
