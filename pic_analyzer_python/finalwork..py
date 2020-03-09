from PIL import Image
import numpy as np
import matplotlib.pyplot as plt


pic1 = Image.open('../pics/edited_colorlevel_2.jpg')
pic2 = Image.open('../pics/edited_colorlevel_1.jpg')

w = 65
h = 64

def count_dhash(image_obj, width, height):
    image = image_obj.resize((width, height), Image.ANTIALIAS)
    gray_img = image.convert("L")
    image_np = np.array(gray_img)
    showimg(image_np)
    binary=[0] * ((width - 1) * height)
    for i in range(width-1-1):
        for j in range(height):
            if image_np[i,j] == image_np[i + 1,j]:
                binary[(len(binary) -1)  - (j * (width - 1) + i)] = 1
    binary_str = ''
    for i in range(len(binary)):
        binary_str += str(binary[i])
    octal = oct(int(binary_str, 2))
    final = str(octal).zfill(len(binary))
    return final

def hamming_dist(otcal1, octal2):
    oct1 = otcal1
    oct2 = octal2
    diff = 0
    for i in range(len(otcal1)):
        if otcal1[i] != octal2[i]:
            diff += 1
    return diff

def showimg(image):
        plt.imshow(image)
        plt.show()


if __name__ == '__main__':
    d1 = count_dhash(pic1, w, h)
    d2 = count_dhash(pic2, w, h)
    print(hamming_dist(d1,d2))