import cv2 as cv

# here we can split and merge the color scale of img

img = cv.imread('pandas2.webp')

# splitting the color channel
b,g,r = cv.split(img)
cv.imshow('Blue', b)
cv.imshow('Green', g)
cv.imshow('Red', r)

print(img.shape)
print(b.shape)
print(g.shape)
print(r.shape)

# merging
merged = cv.merge([b,g,r])
cv.imshow('merge img', merged)

cv.waitKey(0)