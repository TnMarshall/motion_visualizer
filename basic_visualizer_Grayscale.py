import cv2 
import numpy as np
  
  
# define a video capture object 
vid = cv2.VideoCapture(0) 

ret, oldFrame = vid.read() 

oldFrame = cv2.cvtColor(oldFrame, cv2.COLOR_BGR2GRAY) 

cv2.namedWindow("frame", cv2.WINDOW_NORMAL) 
cv2.resizeWindow("frame", 1400, 1400) 

# print(oldFrame.dtype)
  
while(type(oldFrame) != None): 
      
    # Capture the video frame 
    # by frame 
    ret, newFrame = vid.read() 

    newFrame = cv2.cvtColor(newFrame, cv2.COLOR_BGR2GRAY) 

    mathNew = np.zeros(shape=newFrame.shape, dtype=np.int32)
    mathOld = np.zeros(shape=oldFrame.shape, dtype=np.int32)

    mathNew = mathNew + newFrame
    mathOld = mathOld + oldFrame

    frameOut = (mathNew - mathOld)
    frameOut = np.abs(frameOut)
    frameOut = frameOut.astype('uint8')
    oldFrame = newFrame
  
    # Display the resulting frame 
    cv2.imshow('frame', frameOut) 
    
    
      
    # the 'q' button is set as the 
    # quitting button you may use any 
    # desired button of your choice 
    if cv2.waitKey(1) & 0xFF == ord('q'): 
        break
  
# After the loop release the cap object 
vid.release() 
# Destroy all the windows 
cv2.destroyAllWindows() 
