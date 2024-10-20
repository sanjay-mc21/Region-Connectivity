import numpy as np
import cv2

img = cv2.imread(r'F:\New folder\img\02. Mask_Img\Input IMG.png')
upperbound = np.array([123, 255,255])
lowerbound = np.array([40, 40,40])
mask = cv2.inRange(img, lowerbound, upperbound)
imask = mask>0
white = np.full_like(img, [255,255,255], np.uint8)

result = np.zeros_like(img, np.uint8)
result[imask] = white[imask]

cv2.imshow(winname = 'satellite image', mat = img)
cv2.imshow('vegetation detection', result)

cv2.waitKey(0) 
cv2.destroyAllWindows() 