import cv2

img = cv2.imread('images2.png')

cv2.rectangle(img, (100, 100), (300, 200), (255, 0, 0), 2)
cv2.imshow('image', img)
cv2.waitKey(0)
cv2.destroyAllWindows()