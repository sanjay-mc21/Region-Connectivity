import cv2
import numpy as np

# Load the satellite image
img = cv2.imread(r'F:\New folder\img\01. Vegetation\Input IMG.png')
img1 = cv2.imread(r'F:\New folder\img\01. Vegetation\Input IMG.png')
# Convert the image from BGR to HSV
hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)

# Define the lower and upper bounds of the river color in HSV
lower_blue = np.array([80, 10, 50])
upper_blue = np.array([140, 255, 255])
upperbound = np.array([123, 255,255])
lowerbound = np.array([40, 40,40])

# Threshold the image to get only the pixels within the range
mask = cv2.inRange(hsv, lower_blue, upper_blue)
mask1 = cv2.inRange(img1, lowerbound, upperbound)
imask = mask1>0
white = np.full_like(img1, [255,255,255], np.uint8)
# Perform morphological operations to remove noise and improve the segmentation
kernel = np.ones((5, 5), np.uint8)
mask = cv2.morphologyEx(mask, cv2.MORPH_OPEN, kernel)
mask = cv2.morphologyEx(mask, cv2.MORPH_CLOSE, kernel)

# Bitwise-AND the mask with the original image to get the segmented river
result = cv2.bitwise_and(img, img, mask=mask)
result1 = np.zeros_like(img1, np.uint8)
result1[imask] = white[imask]
# Show the results
cv2.imshow("Satellite Image", img)
cv2.imshow(winname = 'satellite image', mat = img1)

cv2.imshow("Mask", mask)
cv2.imshow("Segmented River", result)
cv2.imshow('vegetation detection', result1)
cv2.waitKey(0)
cv2.destroyAllWindows()