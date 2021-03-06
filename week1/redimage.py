import matplotlib.pyplot as plt
import numpy as nump

img = plt.imread("bestwangle.jpeg")
imgrows, imgcols = img.shape[0], img.shape[1]
rgb = img.shape[2]
red = nump.zeros((imgrows, imgcols, rgb), dtype=int)

for x in range(imgrows):
    for y in range(imgcols):
        tint = img[x, y, 0] * 0.5
        red[x,y,0] = tint

plt.imshow(red), plt.show()
plt.imsave("C:/Users/Phoenix-Ptah/Desktop/Nanohackers/ml-spring-2019/week1/bestwanglerouge.jpeg", red)
