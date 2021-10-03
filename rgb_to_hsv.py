import cv2

im = cv2.imread("Resources/tulips.jpeg")
hsvImg = cv2.cvtColor(im, cv2.COLOR_BGR2HSV)
print( type(hsvImg))
print( hsvImg.shape )

cv2.imshow('Image', im)
cv2.imshow('HSV Image', hsvImg)

cv2.waitKey(0)