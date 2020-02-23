import numpy as np
from PIL import Image
import matplotlib.pyplot as plt
import math

FIXWIDTH=10

class Util:

    @staticmethod
    def getLikeProbality(pix1,pix2):
        return 0.5
    
    @staticmethod
    def getDistance(pix1,pix2):
        answer=0
        answer = abs (int(pix1[0])- int(pix2[0]))+abs(int(pix1[1])-int(pix2[1]))+abs(int(pix1[2])-int(pix2[2]))
        if(answer>255):
            return 255
        else:
            return answer

    @staticmethod
    def showMatchPic(Left,right):
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
                # sum=sum/3
                # if(sum>10):
                #     sum=255
                empty[y+picwidth,x+picwidth]=[sum,sum,sum]
        plt.imshow(empty)
        plt.show()
        pass

    @staticmethod
    def showProbality(pic):
        empty = np.array(Image.new("RGB", (pic.shape[0],pic.shape[1])))
        # empty[0:picwidth, 0:picwidth] = [255, 255, 255]
        # empty[picwidth:, picwidth:] = [255, 255, 255]
        empty[:,:,0]=pic
        empty[:,:,1]=pic
        empty[:,:,2]=pic
        plt.imshow(empty)
        plt.show()
        pass

    @staticmethod
    def test():
        data=np.zeros([200,200,3],dtype=int)
        # data = np.array(Image.new("RGB", (200,200)))
        # for x in range(200):
        #     for y in range(200):
        #         data[x,y,0]=x+y
        #         data[x,y,1]=x+y
        #         data[x,y,2]=x+y
        data[:,100:,:]=[100,100,100]
        plt.imshow(data)
        plt.show()
        pass


class point:
    def __init__(self):
        self.x=0
        self.y=0
        pass


class pointMatchProbality:

    def __init__(self,width):
        self.origin=point()
        self.possible=np.ones(width)#表达概率的数组
        self.leftLine=np.ones(FIXWIDTH)
        self.rightLine=np.ones(FIXWIDTH)
        pass
 
    def __setLineBaseProbality(self):

        pass
    
    def __setPointBaseProbality(self):
        p_point=point()
        line=np.ones(FIXWIDTH)
        shape=line.shape



class picProbality:

    def __init__(self,leftPath,rightPath):
        self.leftPic=np.array(Image.open(leftPath))
        self.rightPic=np.array(Image.open(rightPath))
        self.height=self.leftPic.shape[0]
        self.width=self.leftPic.shape[1]
        self.halfHeight =math.ceil(self.height/2)
        self.halfWidth = math.ceil(self.width/2)
        pass

    def beginAnalyse(self):
        self.__initeDataStruct()
        #self.__initeBaseProbality()
        self.__initBaseProbality2()
        pass

    def getPicHeight(self):
        return self.height

    def getBaseProBality(self,line):
        return self.baseProbality[line,:,:]

    def __initeDataStruct(self):
        height=self.height
        width=self.width
        #重新设定概率的表达方式，
        #self.leftProbality=np.zeros([height,width,width],dtype=float) # 图像的匹配概率是一个三维数组，首先是图片的长宽，其次是针对每一个像素，都有一个横向概率数组与之相对应
        #self.rightProbality=np.zeros([height,width,width],dtype=float) # 存的是从左到右的累计量
        self.baseProbality=np.zeros([height,width,width])
        pass

    def __initeBaseProbality(self):
        #for y in range(self.height):#纵坐标
        for y in [5,50,100,200]:#纵坐标
            for x in range( self.halfWidth):#横坐标
                curx=x+self.halfWidth
                leftpoint = self.leftPic[y,curx,:]
                rightpoint = self.rightPic[y,curx,:]
                rightline = self.rightPic[y,:,:]
                leftline = self.leftPic[y,:,:]
                lastLeftPointProbality=0.0
                lastRighePointProbality=0.0
                for pixIterator in range(self.width):
                    lastLeftPointProbality+=Util.getLikeProbality(leftpoint,rightline[pixIterator,:])
                    lastRighePointProbality+=Util.getLikeProbality(rightpoint,leftline[pixIterator,:])
                    self.leftProbality[y,curx,pixIterator]=lastLeftPointProbality
                    self.rightProbality[y,curx,pixIterator]=lastRighePointProbality
        pass

    #计算量比较大计算效率存在问题，这个以后解决
    def __initBaseProbality2(self):
        #for y in range(self.height):
        for y in [200]:
            for xi in range(self.width):
                for yi in range(self.width):
                    self.baseProbality[y,xi,yi]=Util.getDistance(self.leftPic[y,xi,:],self.rightPic[y,yi,:])
        pass

    def __matchToLowProbality(self):
        pass

    def testshow(self):
        Util.showMatchPic(self.leftPic[200,:,:],self.rightPic[200,:,:])
        pass


if __name__ == "__main__":
    leftpath="I:/code/TwoEyeDetect-master/twoEyePic/left1.png"
    rightpath="I:/code/TwoEyeDetect-master/twoEyePic/right1.png"
    possible=picProbality(leftPath=leftpath,rightPath=rightpath)
    possible.beginAnalyse()
    pic = possible.getBaseProBality(200)
    # Util.showProbality(pic)
    possible.testshow()
    # Util.test()
    pass