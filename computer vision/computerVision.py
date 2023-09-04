import cv2 as cv
# # how to read the image using open cv
# # img = cv.imread('pandas2.webp')

# # cv.imshow('Panda', img)
# # cv.waitKey(0)


# # video capturing and local video in open cv
capture = cv.VideoCapture(0)

# #resize the window
# def window_resize(frame, scale=0.75):
#     width = int(frame.shape[0] * scale)
#     height = int(frame.shape[1] * scale)
    
#     dimensions = (width,height)
    
#     return cv.resize(frame, dimensions, interpolation=cv.INTER_AREA)


# def change_resolution(width, height):
#     capture.set(3,width)
#     capture.set(4,height)

# adding picture and text on image and videos

while True:
    isTrue, frame = capture.read()
    # frame_rescale = window_resize(frame)
    
    cv.imshow('video', frame)
    # cv.imshow('videoresize', frame_rescale)
    
    if cv.waitKey(20) & 0xFF==ord('d'):
        break
capture.release()
cv.destroyAllWindows()