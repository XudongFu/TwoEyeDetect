import matplotlib.pyplot as plt
import numpy as np
from PIL import Image
import math

def getMatchPic(Left,right):
    row=Left.shape[0]
    empty = np.array(Image.new("RGB", (row, row)))
    half=int(row/2)
    empty[:,:] = [255, 255, 255]
    for y in range(row)[half:]:
        for x in range(y):
            color=Left[y]-right[x]
            if(color<0):
                color=color*-1
            empty[y,x]=[color,color,color]
    for x in range(half):
        for y in range(half):
            color=Left[x]-right[y]
            if(color<0):
                color=color*-1
            if (x <= y):
                empty[x,y] =[color,color,color]
    plt.imshow(empty)
    pass


path="F:/code/TwoEyeDetect/twoEyePic"
pic="/home/free/roscode/TwoEyeDetect/twoEyePic/left1.png"
picRight="/home/free/roscode/TwoEyeDetect/twoEyePic/right1.png"
left=np.array(Image.open(pic))
right=np.array(Image.open(picRight))
rows,cols,dims=left.shape
half=int(rows/2)
# dataX=range(rows)
# dataY=left[half,:,0]
# dataZ=left[half,:,1]
# dataW=left[half,:,2]

# plt.plot(dataX,dataY)
# plt.plot(dataX,dataZ)
# plt.plot(dataX,dataW)

dataY=left[half,:,1]
dataZ=right[half,:,1]

getMatchPic(dataY,dataZ)

# plt.plot(dataX,dataY,'.')
# plt.plot(dataX,dataZ,'.')
# empty = np.array(Image.new("RGB",(rows,rows)))
# empty[half:rows,0:half]=[255,255,255]
#
#
# for x in range(half):
#     for y in range(half):
#         if(x<=y):
#             empty[x,y] = [255, 255, 255]
#
# for x in range(rows)[half:]:
#     for y in range(rows)[half:]:
#         if(x>=y):
#             empty[x,y] = [255, 255, 255]
#
# plt.imshow(empty)

# plt.plot(dataX,dataY,"g-s")
# plt.plot(dataX,dataZ,"g-s")
plt.show()