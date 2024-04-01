import cv2

# img = cv2.imread('img/dog.webp')

# print(img)

# cv2.imshow('dog',img)

# cv2.waitKey(0)

capture = cv2.VideoCapture('vid/recvid.mp4')

while True:

    isTrue, frames = capture.read()
    cv2.imshow('Video', frames)

    if cv2.waitKey(20) & 0xFF==ord('b'):
        break

capture.release
cv2.destroyAllWindows()
