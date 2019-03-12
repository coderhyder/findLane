import cv2
import numpy as np

img = cv2.imread('test_image.jpg',0)
cv2.imshow('image',img)
k = cv2.waitKey(0) & 0xFF
if k == 27:
    cv2.destroyAllWindows()
elif k == ord('s'):
    cv2.imwrite('moregrey.jpg',img)
    cv2.destroyAllWindows()
# Color loaded IMAGES notes
# openCV loads in BGR, Blue Green Red
# Matplotlib loads RGB Red  Green Blue



