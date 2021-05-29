#-*-coding:utf-8 -*-
from __future__ import division
import cv2
import math
from pytesser import *
import os
import re


def del_noise(im_cut):
    ''' variable：bins：灰度直方图bin的数目
                  num_gray:像素间隔
        method：1.找到灰度直方图中像素第二多所对应的像素，即second_max,因为图像空白处比较多所以第一多的应该是空白，第二多的才是我们想要的内容。
                2.计算mode
                3.除了在mode+-一定范围内的，全部变为空白。
    '''
    bins = 16
    num_gray = math.ceil(256 / bins)
    hist = cv2.calcHist([im_cut], [0], None, [bins], [0, 256])
    lists = []
    for i in range(len(hist)):
        # print hist[i][0]
        lists.append(hist[i][0])
    second_max = sorted(lists)[-2]
    bins_second_max = lists.index(second_max)

    mode = (bins_second_max + 0.5) * num_gray

    for i in range(len(im_cut)):
        for j in range(len(im_cut[0])):
            if im_cut[i][j] < mode - 15 or im_cut[i][j] > mode + 15:
                # print im_cut[i][j]
                im_cut[i][j] = 255
    return im_cut


def replace_text(text):
    text = text.strip()
    text = text.upper()
    rep = {'O': '0',
           'I': '1',
           'L': '1',
           'Z': '7',
           'A': '4',
           '&': '4',
           'S': '8',
           'Q': '0',
           'T': '7',
           'Y': '7',
           '}': '7',
           'J': '7',
           'F': '7',
           'E': '6',
           ']': '0',
           '?': '7',
           'B': '8',
           '@': '6',
           'G': '0',
           'H': '3',
           '$': '3',
           'C': '0',
           '(': '0',
           '[': '5',
           'X': '7',
           '`': '',
           '\\': '',
           ' ': '',
           '\n': '',
           '-': '',
           '+': '',
           '*': '',
           '.': '',
           ';': ''
           }

    #判断是否有数字，有数字直接返回第一个数字，不需要字符替换
    # print text
    if len(text) >= 1:
        pattern = re.compile(u'\d{1}')
        result = pattern.findall(text)
        if len(result) >= 1:
            text = result[0]
        else:
            # 字符替换,替换之后抽取数字返回
            for r in rep:
                text = text.replace(r, rep[r])
            pattern = re.compile(u'\d{1}')
            result = pattern.findall(text)
            if len(result) >= 1:
                text = result[0]

    return text


def predict(image, img_name):
    # image = cv2.imread('./img/8.jpg')
    im = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    # im_cut_real = im[8:47, 28:128]

    im_cut_1 = im[8:47, 28:52]
    im_cut_2 = im[8:47, 52:77]
    im_cut_3 = im[8:47, 77:103]
    im_cut_4 = im[8:47, 101:128]

    im_cut = [im_cut_1, im_cut_2, im_cut_3, im_cut_4]
    pre_text = []
    for i in range(4):
        im_temp = del_noise(im_cut[i])
        # cv2.imshow(str(i), im_temp)
        im_result = Image.fromarray(im_temp.astype('uint8'))
        text = image_to_string(im_result)
        text_rep = replace_text(text)
        pre_text.append(text_rep)
    # print pre_text
    pre_text = ''.join(pre_text)
    if pre_text != img_name:
        print('label:%s'%(img_name),'predict:%s'%(pre_text),'\t','false')
        return 0
    else:
        print('label:%s'%(img_name),'predict:%s'%(pre_text))
        return 1

if __name__ == '__main__':
    img_dir = './img_test'
    img_name = os.listdir(img_dir)  # 列出文件夹下所有的目录与文件
    right = 0
    for i in range(len(img_name)):
        path = os.path.join(img_dir, img_name[i])
        image = cv2.imread(path)
        name_list = list(img_name[i])[:4]
        name = ''.join(name_list)
        pre = predict(image, name)
        right += pre
    accuracy = (right / len(img_name)) * 100
    print(u'准确率为：%s%%,一共%s张验证码，正确：%s,错误：%s' % (accuracy, len(img_name), right, len(img_name) - right))



