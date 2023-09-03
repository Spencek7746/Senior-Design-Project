import cv2
import numpy as np
import matplotlib.pylab as plt

parking_lot_files = "parking_lot_empty.jpg"
image = plt.imread(parking_lot_files)

fig, ax = plt.subplots(figsize=(10, 10))
ax.imshow(image)
ax.axis('off')
plt.show()

#image = np.zeros((512, 512, 3), np.uint8)

#cv2.line(image, (0, 0), (511, 511), (0, 255, 0), 5)

#cv2.imshow('Image', image)

#cv2.waitKey(0)
#cv2.destroyAllWindows()