import matplotlib.pyplot as plt
import numpy as nump

img = plt.imread("bestwangle.jpeg")
scale = 0.5
imgrows, imgcols = int(img.shape[0]*scale), int(img.shape[1]*scale)
timgrows, timgcols = img.shape[0], img.shape[1]
rgb = img.shape[2]
imgc = nump.zeros((imgrows, imgcols, rgb), dtype=int)

scale = 1/scale
# countx = 0
# county = 0
# trix = 0
# triy = 0
for x in range(imgrows):
    # county = 0
    # if trix == scale and countx < imgrows:
    #     countx = countx + 1
    #     trix = 0
    # else:
    #     trix = trix + 1
    for y in range(imgcols):
        # if triy == scale and county < imgcols:
        #     county = county + 1
        #     triy = 0
        # else:
        #     triy = triy + 1
        imgc[x, y,:] = img[x*2, y*2,:]


plt.imshow(imgc), plt.show()
plt.imsave("C:/Users/Phoenix-Ptah/Desktop/Nanohackers/ml-spring-2019/week1/bestwanglebig.jpeg", imgc)
