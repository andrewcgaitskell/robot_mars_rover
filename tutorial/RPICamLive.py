

'''
First import the required libraries, the above has a specific introduction to these libraries
'''
import cv2
import zmq
import base64
import picamera
from picamera.array import PiRGBArray
'''
Here we need to fill in the IP address of the video receiver (the IP address of the PC) '''

IP = '192.168.1.47'

'''
Then initialize the camera, you can change these parameters according to your needs
'''

camera = picamera.PiCamera()
camera.resolution = (640, 480)
camera.framerate = 20
rawCapture = PiRGBArray(camera, size=(640, 480))

'''
Here we instantiate the zmq object used to send the frame, using the tcp communication protocol, where 5555 is the port number
The port number can be customized, as long as the port number of the sending end and the receiving end are the same
'''

context = zmq.Context()

footage_socket = context.socket(zmq.PAIR)

footage_socket.connect('tcp://%s:5555'%IP)

print(IP)

'''
Next, loop to collect images from the camera, because we are using a Raspberry Pi camera, so use_video_port is True
'''

for frame in camera.capture_continuous(rawCapture, format="bgr", use_video_port=True):
    '''
    Since imencode () function needs to pass in numpy array or scalar to encode the image Here we convert the collected frame to numpy array
    '''
    
    frame_image = frame.array

    '''
    We encode the frame into stream data and save it in the memory buffer
    '''

    encoded, buffer = cv2.imencode('.jpg', frame_image)
    jpg_as_text = base64.b64encode(buffer)

    '''
    Here we send the stream data in the buffer through base64 encoding to the video receiving end
    '''

    footage_socket.send(jpg_as_text)

    '''
    Clear the stream in preparation for the next frame
    '''

    rawCapture.truncate(0)
