import cv2
import numpy as np
import os

def gstreamer_pipeline (capture_width=2592, capture_height=1458, display_width=680, display_height=480, framerate=30, flip_method=0) :   
    return ('nvarguscamerasrc ! ' 
    'video/x-raw(memory:NVMM), '
    'width=(int)%d, height=(int)%d, '
    'format=(string)NV12, framerate=(fraction)%d/1 ! '
    'nvvidconv flip-method=%d ! '
    'video/x-raw, width=(int)%d, height=(int)%d, format=(string)BGRx ! '
    'videoconvert ! '
    'video/x-raw, format=(string)BGR ! appsink'  % (capture_width,capture_height,framerate,flip_method,display_width,display_height))

def capture_camera():
    FILE_OUTPUT = './Image_Buffer/output.avi'
    FRAME_OUTPUT = './Image_Buffer/frame_'
    # Checks and deletes the output file
    # You cant have a existing file or it will through an error
    if os.path.isfile(FILE_OUTPUT):
        os.remove(FILE_OUTPUT)
    # To flip the image, modify the flip_method parameter (0 and 2 are the most common)
    print(gstreamer_pipeline(flip_method=0))
    cap = cv2.VideoCapture(gstreamer_pipeline(flip_method=0), cv2.CAP_GSTREAMER)
    currentFrame = 0
    currentFlag = 0
    # Get current width of frame
    width = cap.get(3)   # float
    # Get current height of frame
    height = cap.get(4) # float
    # Define the codec and create VideoWriter object
    out = cv2.VideoWriter(FILE_OUTPUT,cv2.VideoWriter_fourcc(*'XVID'), 20.0, (int(width),int(height)))
    if cap.isOpened():
        while True:
            ret_val, img = cap.read()
            if(ret_val == True):
                cv2.imshow('CSI Camera',img)
                print("[INFO] Frame Number:",currentFrame)
                #out.write(img)
                if(currentFrame%4==0):
                    print("Image Saving:",FRAME_OUTPUT+str(currentFlag)+'.jpg')
                    cv2.imwrite(FRAME_OUTPUT+str(currentFlag)+'.jpg',img)
                    currentFlag+=1
                currentFrame+=1
                if cv2.waitKey(1)&0xFF == ord('q'):
                    break
            else:
                break
        cap.release()
        out.release()
        cv2.destroyAllWindows()
    else:
        print('Unable to open camera')


if __name__ == '__main__':
    capture_camera()
