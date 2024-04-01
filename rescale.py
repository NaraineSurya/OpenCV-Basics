import cv2

img = cv2.imread('img/dog.webp')

cv2.imshow('Image',img)

# cv2.waitKey(0)

def rescaleFrame(frame, scale=0.75):
    width = int(frame.shape[1] * scale)
    height = int(frame.shape[0] * scale)

    return cv2.resize(frame, (width,height), interpolation=cv2.INTER_AREA)

resized_img = rescaleFrame(img)

cv2.imshow('Resized', resized_img)

cv2.waitKey(0)