import numpy as np
from PIL import Image
import matplotlib.pyplot as plt
import cv2
import os

class input_img(object):
    def __init__(self, pic_path):
        self.__path = pic_path
        self.__image = Image.open(pic_path)
        self.__rgb_np = np.array(self.__image)
        self.__name = os.path.basename(pic_path)
        self.__hsv = cv2.cvtColor(self.__rgb_np, cv2.COLOR_RGB2HSV)
        self.__hsv_np = np.array(self.__hsv)

    def get_name(self):
        return self.__name

    def get_image(self):
        return self.__image

    def getrgb_np(self):
        return self.__rgb_np

    def getpath(self):
        return self.__path

    def getRchannel(self):
        rgb_np = self.__rgb_np
        R = rgb_np[:,:,0]
        return R

    def getGchannel(self):
        rgb_np = self.__rgb_np
        G = rgb_np[:,:,1]
        return G

    def getBchannel(self):
        rgb_np = self.__rgb_np
        B = rgb_np[:,:,2]
        return B

    def gethsv(self):
        return self.__hsv

    def gethsv_np(self):
        return self.__hsv_np

    def getHchannel(self):
        hsv_np = self.__hsv_np
        return hsv_np[:,:,0]

    def getSchannel(self):
        hsv_np = self.__hsv_np
        return hsv_np[:,:,1]

    def getVchannel(self):
        hsv_np = self.__hsv_np
        return hsv_np[:,:,2]  

    def getgrayimage(self):
        img = self.__rgb_np
        gray_img = cv2.cvtColor(img, cv2.COLOR_RGB2GRAY)
        out_img = cv2.cvtColor(gray_img, cv2.COLOR_GRAY2RGB)
        return out_img

    def getbwimages(self, thresholds = [40, 80, 120, 160, 200]):
        gray_img = cv2.cvtColor(self.getgrayimage(), cv2.COLOR_RGB2GRAY)
        bw_dic = dict()
        for i in range(len(thresholds)):
            bw = cv2.threshold(gray_img, thresholds[i], 255, cv2.THRESH_BINARY)[1]
            bw_dic['bw' + str(i)] = cv2.cvtColor(bw, cv2.COLOR_GRAY2RGB)
        return bw_dic
    
def showimg(image):
        plt.imshow(image)
        plt.show()




if __name__ == '__main__':
    p = input_img('../pics/raw_1.jpg')
    G = p.getGchannel()
    B = p.getBchannel()
    R = p.getSchannel()
    showimg(R)
    