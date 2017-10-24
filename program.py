import cv2
import sys
import numpy as np
import cv2.cv as cv

img = cv2.imread("face2.jpg",cv2.CV_LOAD_IMAGE_COLOR) ## Read image file

if (img == None): ## Check for invalid input
    print "Could not open or find the image"
else:
    print "size of image: ",img.shape ## print size of image
    cv2.namedWindow('a') ## create window for display
    cv2.imshow('a', img)
    gray = cv2.cvtColor(img, cv.CV_BGR2GRAY)
    gray = cv2.equalizeHist(gray)
    #cv2.imshow ('Display Window',gray) ## Show image in the window
    cascade_fn = "haarcascade_frontalface_alt.xml"
    cascade = cv2.CascadeClassifier(cascade_fn)
    
    rects = cascade.detectMultiScale(img, scaleFactor = 1.3, 
                                    minNeighbors=4, minSize=(20, 20),
                                    flags=cv.CV_HAAR_SCALE_IMAGE)
    if len(rects) == 0:
        print "no face"
    else:
        rects[:,2:] += rects[:,:2]
        vis = img.copy()
        for x1, y1, x2, y2 in rects:
            cv2.rectangle(vis, (x1, y1), (x2, y2), (255,0,123), 2)
        cv2.namedWindow('s') ## create window for display
        cv2.imshow('s', vis)
    cv2.waitKey (0) ## Wait for keystroke
    cv2.destroyAllWindows ()