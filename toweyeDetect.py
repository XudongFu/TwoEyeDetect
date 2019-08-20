import matplotlib.pyplot as plt#约定俗成的写法plt
#首先定义两个函数（正弦&余弦）
import numpy as np
from PIL import Image


path="F:/code/TwoEyeDetect/twoEyePic"
pic="F:/code/TwoEyeDetect/twoEyePic/left2.png"
picRight="F:/code/TwoEyeDetect/twoEyePic/right2.png"
left=np.array(Image.open(pic))
right=np.array(Image.open(picRight))
rows,cols,dims=left.shape
half=int(rows/2)
dataX=range(rows)
# dataY=left[half,:,0]
# dataZ=left[half,:,1]
# dataW=left[half,:,2]

# plt.plot(dataX,dataY)
# plt.plot(dataX,dataZ)
# plt.plot(dataX,dataW)

# dataY=left[half,:,1]
# dataZ=right[half,:,1]
# plt.plot(dataX,dataY,'.')
# plt.plot(dataX,dataZ,'.')
empty = np.array(Image.new("RGB",(rows,rows)))
empty[half:rows,0:half]=[255,255,255]


for x in range(half):
    for y in range(half):
        if(x<=y):
            empty[x,y] = [255, 255, 255]

for x in range(rows)[half:]:
    for y in range(rows)[half:]:
        if(x>=y):
            empty[x,y] = [255, 255, 255]

plt.imshow(empty)

# plt.plot(dataX,dataY,"g-s")
# plt.plot(dataX,dataZ,"g-s")
#在ipython的交互环境中需要这句话才能显示出来
plt.show()