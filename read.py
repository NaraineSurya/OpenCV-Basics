import cv2

img = cv2.imread('img/dog.webp')

print(img)

cv2.imshow('dog',img)

cv2.waitKey(0)