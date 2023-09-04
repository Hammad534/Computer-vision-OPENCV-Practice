import cv2 as cv

img = cv.imread('pandas2.webp')

# Averaging bluring
average = cv.blur(img, (3,3))
cv.imshow('Average Blur', average)

# Gaussian Blur
gauss = cv.GaussianBlur(img, (3,3), 0)
cv.imshow('Gauusain Blur', gauss)

# Median Blur
median = cv.medianBlur(img, 3)
cv.imshow('median blur', median)

# Bilateral blur
bilateral = cv.bilateralFilter(img, 5, 15, 15)
cv.imshow('Bilateral', bilateral)

cv.waitKey(0)