import cv2 
import numpy as np
import sys
  
  
# define a video capture object 
ipAddr = sys.argv[1]
openArg = "http://" + ipAddr
print(openArg)

vid = cv2.VideoCapture() 
vid.open(openArg)
# vid = cv2.VideoCapture(0) 

ret, oldFrame = vid.read() 

oldFrameGray = cv2.cvtColor(oldFrame, cv2.COLOR_BGR2GRAY)
# oldFrameGray = vid.read() 

print(oldFrame.shape)

cv2.namedWindow("frame", cv2.WINDOW_NORMAL) 
cv2.resizeWindow("frame", 1400, 1400) 

# print(oldFrame.dtype)
  
while(type(oldFrame) != None): 
      
    # Capture the video frame 
    # by frame 
    ret, newFrame = vid.read() 

    newFrameGray = cv2.cvtColor(newFrame, cv2.COLOR_BGR2GRAY)

    mathNew = np.zeros(shape=newFrameGray.shape, dtype=np.int32)
    mathOld = np.zeros(shape=oldFrameGray.shape, dtype=np.int32)

    mathNew = mathNew + newFrameGray
    mathOld = mathOld + oldFrameGray

    frameOutGray = (mathNew - mathOld)
    frameOutGray = np.abs(frameOutGray)
    frameOutGray = frameOutGray.astype('uint8')
    oldFrameGray = newFrameGray
  
    b,g,r = cv2.split(newFrame)
    rOrig = r.copy()
    r = r + frameOutGray # TODO Figure out why this keeps resulting in blue regions as well as red. There should only be red
    r+=frameOutGray; r[(r+frameOutGray)<rOrig]=254 # prevent overflow

    frameOut = cv2.merge((b,g,r))

    totalChange = np.sum(np.sum(frameOutGray)) - 250000 #TODO find running average and subtract to bring no-movement value closer to zero
    print(totalChange)


    # Display the resulting frame 
    cv2.imshow('frame', frameOutGray) 
      
    # the 'q' button is set as the 
    # quitting button you may use any 
    # desired button of your choice 
    if cv2.waitKey(1) & 0xFF == ord('q'): 
        break
  
# After the loop release the cap object 
vid.release() 
# Destroy all the windows 
cv2.destroyAllWindows() 
