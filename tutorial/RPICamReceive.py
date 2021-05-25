'''
First import the required libraries
'''

import cv2
import zmq
import base64 import numpy as np

'''
Here we instantiate the zmq object used to receive the frame
Note that the port number needs to be consistent with the sender's
'''

context = zmq.Context()

footage_socket = context.socket(zmq.PAIR) footage_socket.bind('tcp://*:5555')

while True:

    '''
    Received video frame data
    '''
    
    frame = footage_socket.recv_string()
    
    '''
    Decode and save it to the cache
    '''

    img = base64.b64decode(frame)

    '''
    Interpret a buffer as a 1-dimensional array
    '''

    npimg = np.frombuffer(img, dtype=np.uint8)

    '''
    Decode a one-dimensional array into an image
    '''

    source = cv2.imdecode(npimg, 1)

    '''
    Display image
    '''
    cv2.imshow("Stream", source)

    '''
    Generally, waitKey () should be used after imshow () to leave time for image drawing, otherwise the window will appear unresponsive and the image cannot be displayed
    '''
    cv2.waitKey(1)
