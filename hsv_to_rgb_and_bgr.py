import cv2

# img = cv2.imread("Resources/tulips.jpeg")
# hsvImg = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
# cv2.imwrite("Resources/tulips-hsv.jpeg", hsvImg)

hsvImg = cv2.imread("Resources/tulips-hsv.jpeg")
hsv_to_rgb = cv2.cvtColor(hsvImg, cv2.COLOR_HSV2RGB)
hsv_to_bgr = cv2.cvtColor(hsvImg, cv2.COLOR_HSV2BGR)

# cv2.imshow("Image", img)
cv2.imshow("HSV Image", hsvImg)
cv2.imshow("HSV-RGB", hsv_to_rgb)
cv2.imshow("HSV-BGR", hsv_to_bgr)
cv2.waitKey(0)