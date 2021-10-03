import matplotlib.pyplot as plt

cim = plt.imread(r"Resources/tulips.jpeg")
print( cim.shape )
# print( cim )
print( type(cim) )
print( cim.dtype)

R = cim[:,:,0]
G = cim[:,:,1]
B = cim[:,:,2]

plt.figure(1)

plt.subplot(231)
plt.imshow(cim)
plt.xticks([])
plt.yticks([])

plt.subplot(232)
plt.imshow(cim)
plt.xticks([])
plt.yticks([])

plt.subplot(233)
plt.imshow(cim)
plt.xticks([])
plt.yticks([])

plt.subplot(234)
plt.imshow(R, cmap='gray')
plt.xticks([])
plt.yticks([])
plt.title('Red')

plt.subplot(235)
plt.imshow(G, cmap='gray')
plt.xticks([])
plt.yticks([])
plt.title('Green')

plt.subplot(236)
plt.imshow(B, cmap='gray')
plt.xticks([])
plt.yticks([])
plt.title('Blue')

R[100:400,100:400] = 255
G[100:400,100:400] = 0
B[100:400,100:400] = 0
cim[:,:,0] = R
cim[:,:,1] = G
cim[:,:,2] = B

plt.subplot(231)
plt.imshow(cim)
plt.xticks([])
plt.yticks([])

plt.subplot(232)
plt.imshow(cim)
plt.xticks([])
plt.yticks([])

plt.subplot(233)
plt.imshow(cim)
plt.xticks([])
plt.yticks([])

plt.subplot(234)
plt.imshow(R, cmap='gray')
plt.xticks([])
plt.yticks([])
plt.title('Red')

plt.subplot(235)
plt.imshow(G, cmap='gray')
plt.xticks([])
plt.yticks([])
plt.title('Green')

plt.subplot(236)
plt.imshow(B, cmap='gray')
plt.xticks([])
plt.yticks([])
plt.title('Blue')

plt.show()
# plt.imshow(cim)

plt.waitforbuttonpress()