import cv2 
import numpy as np
import sys
  
minChange = 20
highVal = 70

# define a video capture object 
ipAddr = sys.argv[1]
openArg = "http://" + ipAddr
print(openArg)

vid = cv2.VideoCapture() 
vid.open(openArg)
# vid = cv2.VideoCapture(0) 

ret, oldFrame = vid.read() 

# oldFrameGray = cv2.cvtColor(oldFrame, cv2.COLOR_BGR2GRAY)
# oldFrameGray = vid.read() 

print(oldFrame.shape)

cv2.namedWindow("frame", cv2.WINDOW_NORMAL) 
cv2.resizeWindow("frame", 1400, 1400) 
# cv2.namedWindow("dif_nofilter_frame", cv2.WINDOW_NORMAL) 
# cv2.resizeWindow("dif_nofilter_frame", 1400, 1400) 
cv2.namedWindow("dif_filtered_frame", cv2.WINDOW_NORMAL) 
cv2.resizeWindow("dif_filtered_frame", 1400, 1400) 
# cv2.namedWindow("highlighted_movement_frame", cv2.WINDOW_NORMAL) 
# cv2.resizeWindow("highlighted_movement_frame", 1400, 1400) 

# print(oldFrame.dtype)
  
while(type(oldFrame) != None): 
      
    # Capture the video frame 
    # by frame 
    ret, newFrame = vid.read() 

    # newFrameGray = cv2.cvtColor(newFrame, cv2.COLOR_BGR2GRAY)

    mathNew = np.zeros(shape=newFrame.shape, dtype=np.int32)
    mathOld = np.zeros(shape=oldFrame.shape, dtype=np.int32)

    mathNew = mathNew + newFrame
    mathOld = mathOld + oldFrame

    mathOut = (mathNew - mathOld)
    frameOut = (mathNew - mathOld)
    frameOut = np.abs(frameOut)
    frameOut = frameOut.astype('uint8')
    oldFrame = newFrame
  
    # b,g,r = cv2.split(newFrame)
    # rOrig = r.copy()
    # r = r + frameOutGray # TODO Figure out why this keeps resulting in blue regions as well as red. There should only be red
    # r+=frameOutGray; r[(r+frameOutGray)<rOrig]=254 # prevent overflow

    # frameOut = cv2.merge((b,g,r))

    ### Run filtering on each color field for change ###

    b,g,r = cv2.split(frameOut)

    b[b<minChange] = 0
    g[g<minChange] = 0
    r[r<minChange] = 0

    outHighlightB = np.zeros(shape=b.shape, dtype=b.dtype)
    outHighlightG = np.zeros(shape=g.shape, dtype=g.dtype)
    outHighlightR = np.copy(r)
    outHighlightR[b>highVal] = 254
    outHighlightR[g>highVal] = 254
    outHighlightR[r>highVal] = 254

    frameOutHighlighted = cv2.merge((outHighlightB, outHighlightG, outHighlightR))
    frameOutFiltered = cv2.merge((b,g,r))
    
    ### Run filtering on each color field for change ###


    ### Calculate sum of all camera pixels unfiltered ###

    totalChange = np.sum(np.sum(np.sum(mathOut)))
    
    filteredChange = np.sum(np.sum(np.sum(frameOutFiltered)))

    print("Filtered: " + str(filteredChange) + " | Unfiltered: " + str(totalChange))

    ### Calculate sum of all camera pixels unfiltered ###



    # frameOutGray[frameOutGray<minChange]=0
    # totalChange = np.sum(np.sum(frameOutGray)) #TODO find running average and subtract to bring no-movement value closer to zero
    # print(totalChange)

    # frameOutGray[frameOutGray>majChange]=254


    # Display the resulting frame 
    # cv2.imshow('dif_nofilter_frame', frameOut) 
    cv2.imshow('dif_filtered_frame', frameOutFiltered) 
    cv2.imshow('frame', newFrame) 
    # cv2.imshow('highlighted_movement_frame', frameOutHighlighted) 
      
    # the 'q' button is set as the 
    # quitting button you may use any 
    # desired button of your choice 
    if cv2.waitKey(1) & 0xFF == ord('q'): 
        break
  
# After the loop release the cap object 
vid.release() 
# Destroy all the windows 
cv2.destroyAllWindows() 
