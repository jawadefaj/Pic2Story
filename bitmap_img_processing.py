import cv2
import numpy as np
import math


f_target=open("temp.txt", "r")
img_string = f_target.read()
img_string = img_string.split(",")
dim = int(math.sqrt(len(img_string)/4))

temp = np.array(img_string)
temp = temp[0: dim*dim*4]
_temp = np.zeros(dim*dim*4)
for i in range(temp.size):
    _temp[i] = int(temp[i])/255.0
arr = np.reshape(_temp, (dim, dim, 4))
img = arr
trans_mask = img[:,:,3] == 0
img[trans_mask] = [1, 1, 1, 1]
bmp_img = cv2.resize(img, ( 28, 28))
temp = ''
for pixelX in range( 0, bmp_img.shape[0], 1):
    for pixelY in range( 0, bmp_img.shape[1], 1):
        temp += str(bmp_img[pixelX, pixelY, 0]) +  " "
print(temp)
print("\n")
cv2.imshow("image", bmp_img)
cv2.waitKey(0)
cv2.destroyAllWindows()
