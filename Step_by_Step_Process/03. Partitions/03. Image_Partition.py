import cv2

# Load image
img = cv2.imread(r'F:\New folder\img\03. Partitions\Input IMG.png')

# Get image dimensions
height, width, _ = img.shape

# Define the partition boundaries
num_partitions = 4
partition_width = width // num_partitions
boundaries = [i * partition_width for i in range(num_partitions)] + [width]

# Split image into multiple parts
partitions = []
for i in range(len(boundaries)-1):
    partition = img[:, boundaries[i]: boundaries[i+1]]
    partitions.append(partition)

# Display the partitions
for i, partition in enumerate(partitions):
    cv2.imshow(f'Partition {i+1}', partition)

cv2.waitKey(0)
cv2.destroyAllWindows()
