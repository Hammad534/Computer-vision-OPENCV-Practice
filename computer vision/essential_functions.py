import cv2 as cv
import numpy as np

# loading image from local machine

img = cv.imread('pandas2.webp')
cv.imshow('Pandas', img)

# converting rgb image to grayscale image

# gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
# cv.imshow('Gray', gray)

# bluring the image
# blur = cv.GaussianBlur(img, (7,3), cv.BORDER_DEFAULT)
# cv.imshow('blur', blur)

# # edge cascadding
# canny = cv.Canny(img, 125, 125) 
# cv.imshow('Canny Edge', canny)

# # dialating the image
# dialated = cv.dilate(canny, (3,3), iterations=3)
# cv.imshow("Dialated", dialated)

# # eroding
# erode = cv.erode(dialated, (3,3), iterations=3)
# cv.imshow('Erode', erode)


# resizing and cropping 

# resize = cv.resize(img, (400,400), interpolation=cv.INTER_CUBIC)
# cv.imshow('resized', resize)

# crop = img[200:300, 300:450]
# cv.imshow('crop', crop)
cv.waitKey(0)