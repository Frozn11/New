# Import packages
import cv2
import numpy as np
 
img = cv2.imread('images2.png')
print(img.shape) 
# cv2.imshow("original", img)
 
cropped_image = img[80:280, 150:330]
 
cv2.imshow("cropped", cropped_image)
cv2.imwrite("Cropped Image.jpg", cropped_image)
 
cv2.waitKey(0)
cv2.destroyAllWindows()