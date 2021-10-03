import numpy as np
import matplotlib.pyplot as plt

im = plt.imread(r'Resources/albert-einstein-gray.jpeg')
print("Type: ", type(im))
print("Shape: ", im.shape)
print("Data Type: ", im.dtype)
print(im[23][70])
# print(im)

print(im[50,300])
im[50,300] = 255
print(im[50,300])
# im[50:100,0:100] = 255
# im[400:500] = 255
im[550:650, 530:650] = 255
# im[595:650] = 255
im[700:800, 670:830] = 255

plt.imshow(im, cmap='gray')

plt.imsave(r'Resources/albert-einstein-gray-modified.jpeg', im)

plt.waitforbuttonpress()