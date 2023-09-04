import cv2 as cv
import matplotlib.pyplot as plt


#importing img
img = cv.imread('pandas2.webp')

# BGR TO GRAYSCALE
gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
cv.imshow("GRay", gray)

# BGR TO HSV
hsv = cv.cvtColor(img, cv.COLOR_BGR2HSV)
cv.imshow("HSV", hsv)

# BGR TO L*A*B
lab = cv.cvtColor(img, cv.COLOR_BGR2LAB)
cv.imshow("LAB", lab)

# BGR TO RGB
rgb = cv.cvtColor(img, cv.COLOR_BGR2RGB)
cv.imshow("RGB", rgb)


# making plot of an image using matplotlib lib
plt.imshow(img)
plt.show()


cv.waitKey(0)