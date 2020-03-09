from image import input_img
import PIL
import os

class analyzer():
    def __init__(self, img_obj1, img_obj2):
        img_obj1 = img_obj1
        img_obj2 = img_obj2
        s1 = img_obj1.getrgb_np().shape
        s2 = img_obj2.getrgb_np().shape
        # if length and width are the same between two pictures
        if s1 == s2:
            self.__samesize = True
        # if length and width have the same proportion
        elif s1[0]/s1[1] == s2[0]/s2[1]:
            name1 = img_obj1.get_name()
            name2 = img_obj2.get_name()
            if not os.path('./.temppics'):
                os.mkdir('./.temppics')
            h = min(s1[0], s2[0])
            if h == s1[0]:
                w = s1[1]
                tosave = img_obj2.get_image().resize((h,w), PIL.Image.ANTIALIAS)
                path = './temppics/' + name2
                tosave.save(path)
                img_obj2 = input_img(path)
            else:
                w = s2[1]
                tosave = img_obj1.get_image().resize((h,w), PIL.Image.ANTIALIAS)
                path = './temppics/' + name1
                tosave.save(path)
                img_obj1 = input_img(path)
            self.__samesize = True
        else:
            self.__samesize = False
        self.__imgobj1 = img_obj1
        self.__imgobj2 = img_obj2
    
    def is_samesize(self):
        return self.__samesize

    def compare_rgb(self):
        '''
        rgb np array distance between two pictures(same size)
        '''
        im1 = self.__imgobj1
        im2 = self.__imgobj2
        im1_np = im1.getrgb_np()
        im2_np = im2.getrgb_np()
        dist_sum = 0
        try:
            for i in range(len(im1_np)):
                for j in range(len(im1_np[0])):
                    for k in range(3):
                        # ubyte should between 0 and 255, otherwise it will raise an error message. Use int to escape from this problem
                        dist_sum += abs(int(im1_np[i,j,k]) - int(im2_np[i,j,k]))
            total_size = im1_np.size * 255
            dif_rate = dist_sum/total_size
            return dif_rate
        except:
            return None

    # def compare_hsv(self):
    #     im1 = self.__imgobj1
    #     im2 = self.__imgobj2
    #     im1_H_np = im1.getHchannel()
    #     im1_S_np = im1.getSchannel()
    #     im1_V_np = im1.getVchannel()
    #     im2_H_np = im2.getHchannel()
    #     im2_S_np = im2.getSchannel()
    #     im2_V_np = im2.getVchannel()
    #     hsv_1 = [im1_H_np, im1_S_np, im1_V_np]
    #     hsv_2 = [im2_H_np, im2_S_np, im2_V_np]
    #     rates = []
    #     element_num = im1_H_np.size
    #     for i in range(3):
    #         dif_sum = 0
    #         element_difference_ls = []
    #         for j in range(len(hsv_1[0])):
    #             for k in range(len(hsv_1[0][0])):
    #                 element_difference = abs(int(hsv_1[i][j, k]) - int(hsv_2[i][j, k]))
    #                 element_difference_ls.append(element_difference)
    #                 dif_sum += element_difference
    #         average_dif = dif_sum/element_num
    #         single_channel_rate = sum([element_dif/average_dif for element_dif in element_difference_ls])/element_num
    #         rates.append(single_channel_rate)
    #     return rates


if __name__ == '__main__':
    p1 = input_img('../pics/edited_1.png')
    p2 = input_img('../pics/raw_1.jpg')
    a = analyzer(p1,p2)
    print(a.compare_rgb())
