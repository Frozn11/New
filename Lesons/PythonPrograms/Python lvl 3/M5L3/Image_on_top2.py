import cv2

image1 = cv2.imread('images2.png')
image2 = cv2.imread('2.png')

image2 = cv2.resize(image2, (image1.shape[1], image1.shape[0]))

result = cv2.bitwise_or(image1, image2)

cv2.imshow('Наложение изображений', result)
cv2.waitKey(0)
cv2.destroyAllWindows()
