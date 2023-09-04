import cv2 as cv
import numpy as np

# making blank image
blank = np.zeros((500,500,3), dtype='uint8') #uint8 is the data type of image
# cv.imshow('image', blank)

# color changing of the blank image
# blank[:] = 0,255,0

# color the specific area of image
# blank[200:300, 400:500] = 0,0,255
# cv.imshow('image', blank)

# making rectangle on image
# cv.rectangle(blank, (0,0), (250,350), (139,220,0), thickness=3)
# cv.imshow('image', blank)

# cv.circle(blank, (blank.shape[1]//3, blank.shape[0]//2) , 40, (0,110,0), thickness=3) # (blank.shape[1]//3, blank.shape[0]//2) another method to put the dimension of object
# cv.imshow('circle', blank)

# draw a line
# cv.line(blank, (100,200), (300,500), (255,255,255), thickness=3)
# cv.imshow('line', blank)

# write text on image
cv.putText(blank, ('Hammad Afzal'), (50,300), cv.FONT_HERSHEY_SIMPLEX, 1.5, (255,255,255), 3)
cv.imshow('text', blank)

cv.waitKey(0)