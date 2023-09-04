import cv2
import numpy as np
import matplotlib.pylab as plt

tags = ["Taken", "Empty"]
parking_lot_files = "parking_lot_empty.jpg"
image = cv2.imread(parking_lot_files)

cv2.imshow('Image', image)

cv2.waitKey(0)
cv2.destroyAllWindows()