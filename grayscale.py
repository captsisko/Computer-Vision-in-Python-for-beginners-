import numpy as np
import matplotlib.pyplot as plt

im = np.arange(256)
print(im)
print(im.shape)

im = im[np.newaxis,:]
print(im)
print(im.shape)

im = np.repeat(im, 10, axis=0)
print(im)
print(im.shape)

plt.imshow(im, cmap='gray')
plt.waitforbuttonpress()

