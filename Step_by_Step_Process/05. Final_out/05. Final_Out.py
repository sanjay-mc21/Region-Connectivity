import cv2
import numpy as np

img = cv2.imread(r'F:\New folder\img\05. Final_out\Input IMG.png')

# Specify the point where you want to mark an 'X'
x = 200
y = 260

# Draw the 'X' on the image
cv2.line(img, (x-40, y-40), (x+40, y+40), (0, 0, 255), 2)
cv2.line(img, (x+40, y-40), (x-40, y+40), (0, 0, 255), 2)

hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)

lower_blue = np.array([80, 10, 50])
upper_blue = np.array([140, 255, 255])
upperbound = np.array([123, 255,255])
lowerbound = np.array([40, 40,40])

mask = cv2.inRange(hsv, lower_blue, upper_blue)
mask1 = cv2.inRange(img, lowerbound, upperbound)
imask = mask1>0
white = np.full_like(img, [255,255,255], np.uint8)

kernel = np.ones((5, 5), np.uint8)
mask = cv2.morphologyEx(mask, cv2.MORPH_OPEN, kernel)
mask = cv2.morphologyEx(mask, cv2.MORPH_CLOSE, kernel)

result = cv2.bitwise_and(img, img, mask=mask)
result1 = np.zeros_like(img, np.uint8)
result1[imask] = white[imask]



result = cv2.bitwise_and(img, img, mask=mask)
result1 = np.zeros_like(img, np.uint8)
result1[imask] = white[imask]


cv2.imshow('Image with X mark', img)
#cv2.imshow("Satellite Image", img)
cv2.imshow("Mask", mask)
#cv2.imshow("Segmented River", result)
#cv2.imshow('vegetation detection', result1)
cv2.waitKey(0)
cv2.destroyAllWindows()

# Display the image

cv2.waitKey(0)
cv2.destroyAllWindows()