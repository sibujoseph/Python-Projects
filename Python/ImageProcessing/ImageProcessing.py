import numpy
import cv2
from matplotlib import pyplot as plt

# Load an color image in grayscale
img = cv2.imread('messi5.jpg',0)

# Load an color image in color
img = cv2.imread('messi5.jpg',1)


cv2.imshow('image',img)
cv2.waitKey(0)
cv2.destroyAllWindows()

img = cv2.imread('messi5.jpg',0)
plt.imshow(img, cmap = 'gray', interpolation = 'bicubic')
plt.xticks([]), plt.yticks([])  # to hide tick values on X and Y axis
plt.show()
