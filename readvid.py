import numpy as np
import cv2
cap = cv2.VideoCapture("img/vid.mp4")
# cap = cv2.VideoCapture(0)

while(cap.isOpened()):
  # ret, frame = cap.read()
#   gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
  # cv2.imshow('frame',frame)
  
# Returns a posterior frame
  cap.set(cv2.CAP_PROP_POS_FRAMES, 10)
  _, frame = cap.read()
  cv2.imwrite('0_set.jpg', frame)
  if cv2.waitKey(1) & 0xFF == ord('q'):
    break

cap.release()
cv2.destroyAllWindows()