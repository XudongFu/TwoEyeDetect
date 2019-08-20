import matplotlib.pyplot as plt
import numpy as np
from PIL import Image

def showline(data,right):
    row=100
    rows,col=data.shape
    temp = Image.new("RGB",(rows,row))
    dim=np.array(temp)
    for i in range(50):
        dim[i]=data
    for i in range(100)[50:100]:
        dim[i]=right
    return dim

def getMatchPic(X,Y):
    col=X.shape
    empty = np.array(Image.new("RGB", (col, col)))
    half=int(col/2)
    empty[half:rows, 0:half] = [255, 255, 255]
    for y in range(rows)[half:]:
        for x in range(y):
            empty[y,x]=[X[y,x]-Y[y,x],0,0]
    for x in range(half):
        for y in range(half):
            if (x <= y):
                empty[x,y] =[ X[x,y] - Y[x,y],0,0]
    plt.imshow(empty)
    pass



picleft = Image.open("/home/free/roscode/TwoEyeDetect/twoEyePic/left2.png")



plt.imshow(picleft)
left = np.array(Image.open("/home/free/roscode/TwoEyeDetect/twoEyePic/left1.png"))
right=np.array(Image.open("/home/free/roscode/TwoEyeDetect/twoEyePic/right1.png"))
rows,cols,dims=left.shape
half=int(450)
picLine=showline(left[half,:,:],right[half,:,:])
plt.imshow(picLine)
# X=range(cols)
# dataY1=left[half,:,0]
# dataY2=right[half,:,0]
# plt.plot(X,dataY1)
# plt.plot(X,dataY2)
plt.show()