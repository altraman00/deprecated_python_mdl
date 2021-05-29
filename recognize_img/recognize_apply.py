# -*- coding:utf-8 -*-
from __future__ import division
import os
from sklearn.externals import joblib
import cv2
import numpy as np
from sklearn.preprocessing import LabelBinarizer

if __name__ == '__main__':
    img_dir = './test'
    img_name = os.listdir(img_dir)
    # 加载模型
    clf = joblib.load('./knn.pkl')
    right = 0
    for i in range(len(img_name)):
        path = os.path.join(img_dir, img_name[i])
        # cv2读进来的图片是RGB3维的，转成灰度图，将图片转化成1维
        image = cv2.imread(path)
        im = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
        image = im.reshape(-1)
        # 转2维[[1,2,3...,23,4,1]]
        print image.shape
        temp = []
        temp.append(list(image))
        x = np.array(temp)
        print len(x[0])
        y_temp = img_name[i][-5]
        y_temp = int(y_temp)
        y = np.zeros(10)
        y[y_temp] = 1
        # print y_temp

        pre_y = clf.predict(x)
        # print pre_y
        pre_y = np.argmax(pre_y[0])

        if pre_y != y_temp:
            print 'label:%s' % (y_temp), 'predict:%s' % (pre_y), '\t', 'false'
        else:
            print 'label:%s' % (y_temp), 'predict:%s' % (pre_y)
            right += 1

    accuracy = right / len(img_name) *100
    print u'准确率为：%s%%' % (accuracy)






