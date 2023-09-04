import cv2 as cv
import numpy as np


img = cv.imread('matplotlib.webp')
cv.imshow('image', img)

# translation of an immage
# makng function to perform this
def translate(img, x, y):
    transformMatrix = np.float32([[1,0,x],[0,1,y]])
    dimensions = (img.shape[1], img.shape[0])
    return cv.warpAffine(img, transformMatrix, dimensions)

# -x --> left
# # -y --> up
# x --> right
# y --> down

translated = translate( img, 100, 100)
cv.imshow('translated', translated)

# rotation of an image
# making a function that can perform the rotation of an image
def rotate(img, angle, rotPoint=None):
    (height, width)= img.shape[:2]
    if rotPoint is None:
        rotPoint = (width//2, height//2)
    
    rotMat = cv.getRotationMatrix2D(rotPoint, angle, 1.0)
    dimensions = (width, height)
    
    return cv.warpAffine(img, rotMat, dimensions)

rotated = rotate(img, 45)  # 45 is the value of angle
# if angle is positive then img rotate anticlockwiose
# if angle is negative then img rotate clo0ckwise

cv.imshow('Rotated Img', rotated)

# Resizing of an image
resized = cv.resize(img, (500,500), interpolation=cv.INTER_CUBIC)
cv.imshow('resized image', resized)

# Flipping the Image
# {1,0,-1} they indicates that 1 is for horizental flip, 0 for vertical and -1 for both at a same time

flip = cv.flip(img, 0)
cv.imshow('Flip img', flip)

# Cropping of image

cropped = img[200:300, 250:400]
cv.imshow('crop img', cropped)


cv.waitKey(0)