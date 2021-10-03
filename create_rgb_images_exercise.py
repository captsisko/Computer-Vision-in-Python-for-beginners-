import cv2
import numpy as np
import matplotlib.pyplot as plt

rgb = np.zeros((100, 150, 3), dtype='uint8') # 10 rows, 150 columns, 3 values in each cell
print(rgb)
rgb[:,0:50,0] = 255
rgb[:,50:100,1] = 255
rgb[:,100:150,2] = 255

plt.imshow(rgb, cmap='gray')
plt.waitforbuttonpress()

# rgb = rgb[:,:,::-1] # reverses the order

cv2.imshow("Image", rgb)
cv2.waitKey(0)