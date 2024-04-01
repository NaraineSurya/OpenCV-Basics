import cv2

# img = cv2.imread('img/dog.webp')

# cv2.imshow('Image',img)

# cv2.waitKey(0)

# resized_img = rescaleFrame(img)

# cv2.imshow('Resized', resized_img)

def rescaleFrame(frame, scale=0.75):
    width = int(frame.shape[1] * scale)
    height = int(frame.shape[0] * scale)

    return cv2.resize(frame, (width,height), interpolation=cv2.INTER_AREA)

capture = cv2.VideoCapture('vid/recvid.mp4')

while True:

    isTrue, frames = capture.read()

    rescale_Frame = rescaleFrame(frames, 0.4)
    cv2.imshow('Video', frames)
    cv2.imshow('rescale_video', rescale_Frame)

    if cv2.waitKey(20) & 0xFF==ord('b'):
        break

capture.release
cv2.destroyAllWindows()

cv2.waitKey(0)