import cv2
import numpy as np

# Load the image
img = cv2.imread(r'F:\New folder\img\04. Distance\Distance Input.png')

# Convert the image to grayscale
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# Threshold the image to create a binary mask of the black squares
ret, thresh = cv2.threshold(gray, 10, 255, cv2.THRESH_BINARY)

# Apply morphological operations to remove noise and fill gaps in the black squares
kernel = cv2.getStructuringElement(cv2.MORPH_ELLIPSE, (5, 5))
mask = cv2.morphologyEx(thresh, cv2.MORPH_OPEN, kernel)
mask = cv2.morphologyEx(mask, cv2.MORPH_CLOSE, kernel)

# Find the contours of the black squares
contours, hierarchy = cv2.findContours(mask, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

# Draw contours around the black squares
cv2.drawContours(img, contours, -1, (0, 0, 255), 2)

# Calculate the distance between the centroids of the two largest black squares
if len(contours) >= 2:
    # Get the centroids of the two largest black squares
    centroids = []
    for contour in contours:
        M = cv2.moments(contour)
        if M["m00"] != 0:
            cx = int(M["m10"] / M["m00"])
            cy = int(M["m01"] / M["m00"])
            centroids.append((cx, cy))
    centroids = sorted(centroids, key=lambda c: c[0])
    centroid1, centroid2 = centroids[:2]

    # Calculate the distance between the centroids of the two largest black squares
    distance = np.sqrt((centroid2[0] - centroid1[0])**2 + (centroid2[1] - centroid1[1])**2)

    #print(f"Distance between the two largest black squares: {distance:.2f} pixels")
#else:
    #print("Could not find two black squares in the image")


# Set the pixel width value in pixels
pixel_width = distance

# Set the scale of the image in the real world
# In this example, we assume a scale of 1:500 meters
scale = 7.5  # 1 pixel represents 0.003 meters

# Calculate the width of the image in the real world
width_km = (pixel_width * scale) / 1000

# Print the width of the image in kilometers
print("The width of the image is {:.2f} km".format(width_km))

# Display the image with contours around the black squares
cv2.putText(img, f"Distance: {width_km:.2f} kilometers", (10, 30), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 255), 2)
cv2.imshow('image', img)
cv2.waitKey(0)
cv2.destroyAllWindows()
