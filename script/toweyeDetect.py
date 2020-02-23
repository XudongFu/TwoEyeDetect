import matplotlib.pyplot as plt#约定俗成的写法plt
#首先定义两个函数（正弦&余弦）
import numpy as np
from PIL import Image

def getMatchPic(Left,right):
    row,col=Left.shape
    picwidth=50
    width=picwidth+row
    empty = np.array(Image.new("RGB", (width,width)))
    empty[0:picwidth, 0:picwidth] = [255, 255, 255]
    empty[picwidth:, picwidth:] = [255, 255, 255]
    for x in range(width)[picwidth:]:
        empty[x,0:picwidth]=Left[x-picwidth]
        empty[0:picwidth,x]=right[x-picwidth]
    half=int(row/2)
    for y in range(row):
        for x in range(y):
            color=Left[y]-right[x]
            sum=0
            for c in range(3):
                sum=sum+ abs(color[c])
            sum=sum/3
            # if(sum>2):
            #     sum=255
            empty[y+picwidth,x+picwidth]=[sum,sum,sum]
    plt.imshow(empty)
    pass


pic="I:/code/TwoEyeDetect-master/twoEyePic/left1.png"
picRight="I:/code/TwoEyeDetect-master/twoEyePic/right1.png"
left=np.array(Image.open(pic))
right=np.array(Image.open(picRight))
rows,cols,dims=left.shape
# half=int(rows/2)
half=200
dataX=range(rows)
# dataY=left[half,:,0]
# dataZ=left[half,:,1]
# dataW=left[half,:,2]
dataY=left[half,:,:]
dataZ=right[half,:,:]
getMatchPic(dataY,dataZ)
plt.show()