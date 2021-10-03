import cv2
import matplotlib.pyplot

im = cv2.imread("Resources/albert-einstein-gray.jpeg", cv2.IMREAD_GRAYSCALE)
print( type(im) )
print( im.dtype )
print( im.shape )

im[530:630, 560:670] = 0
im[530:630, 730:830] = 0

cv2.imshow('Einstein', im)

cv2.imwrite("Resources/albert-einstein-gray-opencv-modified.jpeg", im)

cv2.waitKey(0)
cv2.destroyAllWindows()