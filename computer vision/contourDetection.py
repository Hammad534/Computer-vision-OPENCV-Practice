import cv2 as cv
import numpy as np

img = cv.imread('pandas2.webp')
# cv.imshow('img', img)

# converting img to grayscale img
gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
cv.imshow('Gray scale', gray)

# making canny
canny = cv.Canny(img, 125, 275)
cv.imshow('Canny edges', canny)

# making threshold function
ret, thresh = cv.threshold(gray, 125,255, cv.THRESH_BINARY)
cv.imshow('thresh', thresh)

# finding contours
contours, herarchies = cv.findContours(thresh, cv.RETR_LIST, cv.CHAIN_APPROX_SIMPLE)
print(f'{len(contours)} contours found!')


# making blank image
blank = np.zeros((500,500,3), dtype='uint8')
cv.imshow('blank', blank)

# drawing contours on blank image
draw = cv.drawContours(blank, contours, -1, (0,0,255), 1)
cv.imshow('Draw Contours', draw)


cv.waitKey(0)
