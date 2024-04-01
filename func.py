import cv2

img = cv2.imread('img/dog.webp')
cv2.imshow('img', img)

new_img  = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
# cv2.imshow('new_img', new_img)

blur_img = cv2.GaussianBlur(img, (9,9), 0)
# cv2.imshow('blurred_img', blur_img)

canny = cv2.Canny(img, 100,200)
cv2.imshow('edges', canny)

cv2.waitKey(0)